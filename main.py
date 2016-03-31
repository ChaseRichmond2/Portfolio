import webapp2
import os
import logging
import jinja2

# Lets set it up so we know where we stored the template files
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info(self.request.path)
    	template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    	self.response.write(template.render({'title':'Index','Greeting':'Hello, My name is'}))
class ExperienceHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/experience.html')
        self.response.write(template.render({'title':'Experience'}))
class GalleryHandler(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/gallery.html')
        self.response.write(template.render({'title':'Gallery'}))
class ContactHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
		self.response.write(template.render({'title':'Contact'}))
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index.html', MainHandler),
    ('/experience.html', ExperienceHandler),
    ('/gallery.html', GalleryHandler),
    ('/contact.html',ContactHandler)

], debug=True)
