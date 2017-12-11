import webapp2
import models

class AlbumsPage(webapp2.RequestHandler):
	def post(self):
		useralbums = models.get_useralbums()
		try:
			#album = blob(self.request.get(‘photos’))
			#useralbums.album = album
			photo = blob(self.request.get(‘photos’))
			useralbums.photo = photo
			useralbums.put()
		except ValueError:
			logging.info('Error in albums.py uploading photos from create.html')
			pass
		self.redirect(‘/create.html’)

application = webapp2.WSGIApplication([(‘/albums’,AlbumsPage)],debug=True)
