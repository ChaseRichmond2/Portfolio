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
        logging.info("GET")
        logging.info(self.request.path)
        try:
            path=self.request.path
            template = JINJA_ENVIRONMENT.get_template('templates%s'%path)
            if path == '/':
                self.response.write(template.render({'title':'Index'}))
            elif path == '/experience.html':
                self.response.write(template.render({'title':'Experience'}))
            elif path == '/gallery.html':
                self.response.write(template.render({'title':'Gallery'}))
            else:
                self.response.write(template.render({'title':'Index'}))
        except:
            template = JINJA_ENVIRONMENT.get_template('templates/index.html')
            self.response.write(template.render({'title':'Index'}))
class ContactHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("Contact")
        template = JINJA_ENVIRONMENT.get_template('templates/contact.html')
        self.response.write(template.render({'title':'Homepage','Home':'HOME', 'Family':'Family','School':'School', 'Login': 'Login'})) 
    def post(self):
        logging.info("POST for Login Handler")
        name = self.request.get("name") #These read everything in as a string so we must use ""
        email = self.request.get("email")
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index.html', MainHandler),
    ('/experience.html', MainHandler),
    ('/gallery.html', MainHandler),
    ('/contact.html',MainHandler)

], debug=True)
