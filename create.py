from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext import ndb
from google.appengine.api import images
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
import os
import jinja2
import logging
# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')

template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))

class Photo(ndb.Model):
    blob_key = ndb.BlobKeyProperty()

class Album(ndb.Model):
    name = ndb.StringProperty()
    num_photos = ndb.IntegerProperty()
    photos = ndb.KeyProperty(kind='Photo',repeated=True)

class User(ndb.Model):
    user = ndb.StringProperty()
    num_albums = ndb.IntegerProperty()
    albums = ndb.KeyProperty(kind='Album',repeated=True)

class CreatePage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            user_id = user.user_id()
            query = User.query(User.user == user_id).count()
            if query is 0:
                new_user = User(user=user_id)
                new_user.num_albums = 0
                new_user.put()

        login_url = users.create_login_url('/create.html')
        logout_url = users.create_logout_url('/create.html')
        albums_viewable = False
        # changing upload_url to be '/new_album'
        upload_url = blobstore.create_upload_url('/new_album')
        view_hide_form = """
            <form action='/view_albums' method='GET'>
                <input name='view_albums' type='submit' value='View Albums'>
            </form>"""
        template = template_env.get_template('create.html')
        context = {
            'user': user,
            'logout_url': logout_url,
            'login_url': login_url,
            'upload_url': upload_url,
            'view_hide_form': view_hide_form,
            'albums_viewable': albums_viewable
        }
        self.response.out.write(template.render(context))

class NewAlbumHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        # QUERY for user
        user_id = users.get_current_user().user_id()
        query = User.query(User.user == user_id)
        user = query.get()
        num_albums = user.num_albums
        user.num_albums = num_albums + 1

        album_n = self.request.get('album_name')
        logging.critical('Num Albums: %s' % str(num_albums))
        album = Album(name=str(album_n))
        uploads = self.get_uploads()
        for upload in uploads:
            photo = Photo(blob_key=upload.key())
            photo.put()
            album.photos.append(photo.key)
        album.put()
        user.albums.append(album.key)
        user.put()
        self.redirect('/create.html')

class ViewAlbumsHandler(webapp2.RequestHandler):
    def get(self):
        # QUERY for user
        logging.critical('Top of: ViewAlbumsHandler')
        user_ = users.get_current_user()
        user_id = user_.user_id()
        query = User.query(User.user == user_id)
        user = query.get()

        albums_info = {}
        for album in user.albums:
            _album = album.get()
            try:
                for photo in _album.photos:
                    # Get first image in each album]
                    try:
                        blob = photo.get().blob_key
                        name = _album.name
                        url = images.get_serving_url(blob,size=100,crop=True,secure_url=True)
                        logging.critical("Adding Name: %s, url: %s" % (str(name),str(url)))
                        albums_info.update({name:url})
                    except:
                        logging.critical("Photo not found")
                    #albums_info[name] = url
                    break
            except:
                logging.critical("Album has not photos")
            #logging.critical("Iteration through albums")
        #upload_url is still active so don't need to include
        for key, value in albums_info.iteritems():
            logging.critical("Key: %s, Value: %s" % (str(key), str(value)))
        albums_viewable = True
        view_hide_form = """
			<form action='/hide_albums' method='GET'>
  				<input name='hide_albums' type='submit' value='Hide Albums'>
  			</form>
		"""
        template = template_env.get_template('create.html')
        context = {
            'albums_viewable': albums_viewable,
            'albums_info': albums_info,
            'view_hide_form': view_hide_form,
            'user': user_
        }
        #logging.critical('Photos Viewable? %r' % photos_viewable)
        #logging.critical('ViewPhotosHandler')
        self.response.out.write(template.render(context))

class HideAlbumsHandler(webapp2.RequestHandler):
    def get(self):
        # QUERY user
        user_id = users.get_current_user().user_id()
        query = User.query(User.user == user_id)
        user = query.get()
        for album in user.albums:
            _album = album.get()
            try:
                for photo in _album.photos:
                    # Get first image in each album
                    blob = photo.get().blob_key
                    images.delete_serving_url(blob)
                    break
            except:
                logging.critical("Album link is broken")

        #view_hide_form should reset I think
        logging.critical('HidePhotoHandler')
        self.redirect('/create.html')

class ViewAlbumPhotosHandler(webapp2.RequestHandler):
    def post(self, album_key):
        user_ = users.get_current_user()
        user_id = user_.user_id()
        query = User.query(User.user == user_id)
        user = query.get()
        photo_urls = []
        display_album_photos = True
        for album in user.albums:
            try:
                _album = album.get()
                if (_album.name == album_key):
                    for photo in _album.photos:
                        blob = photo.get().blob_key
                        url = images.get_serving_url(blob,size=100,crop=True,secure_url=True)
                        photo_urls.append(url)
                    break
            except:
                logging.critical("Album link is broken")
        template = template_env.get_template('create.html')
        context = {
            'photo_urls': photo_urls,
            'user': user_,
            'display_album_photos': display_album_photos,
            'album_name': album_key
        }
        self.response.out.write(template.render(context))

class HideAlbumPhotosHandler(webapp2.RequestHandler):
    def post(self, album_key):
        user_ = users.get_current_user()
        user_id = user_.user_id()
        query = User.query(User.user == user_id)
        user = query.get()
        for album in user.albums:
            _album = album.get()
            try:
                if (_album.name == album_key):
                    for photo in _album.photos:
                        blob = photo.get().blob_key
                        images.delete_serving_url(blob)
                    break
            except:
                logging.critical("Album link is broken")
        self.redirect('/view_albums')

class DeleteAlbumHandler(webapp2.RequestHandler):
    def post(self, album_key):
        user_ = users.get_current_user()
        user_id = user_.user_id()
        query = User.query(User.user == user_id)
        user = query.get()
        album_found = False
        for album in user.albums:
            _album = album.get()
            try:
                if (_album.name == album_key):
                    ndb.delete_multi(ndb.Query(ancestor=album).iter(keys_only = True))
                    album_found = True
            except:
                logging.critical("Album link is broken")
        if not album_found:
            self.error(404)
        self.redirect('/view_albums')

application = webapp2.WSGIApplication([
    ('/create.html', CreatePage),
    ('/new_album', NewAlbumHandler),
    ('/view_albums', ViewAlbumsHandler),
    ('/hide_albums', HideAlbumsHandler),
    ('/view_photos/([^/]+)?', ViewAlbumPhotosHandler),
    ('/hide_photos/([^/]+)?', HideAlbumPhotosHandler),
    ('/delete_album/([^/]+)?', DeleteAlbumHandler)
    ], debug=True)
