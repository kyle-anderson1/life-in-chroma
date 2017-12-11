import webapp2
import os
import jinja2

from google.appengine.api import users

template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))

class upload(webapp2.RequestHandler):
    def post(self):
        photos = self.request.POST.getall('photos')
        for f in photos:
            c = f.file.read(),
            f = f.filename
        p = {
            'content': c,
            'filename': f
        }
        template = template_env.get_template('create.html')
        self.response.out.write(template.render(p))
        #_photos = [{'content': f.file.read(), 'filename':f.filename} for f in photos]
        #self.redirect('/create.html')

application = webapp2.WSGIApplication([('/upload', upload)], debug=True)
