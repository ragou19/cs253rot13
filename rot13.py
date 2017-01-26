import webapp2
import cgi
import string

form = """
	<form method="post">
		<h1>Enter some text to ROT13:</h1>
		<textarea name="user_input" rows="8" cols="70">%(user_input)s&#10;&#13&#10;&#13%(rot13)s</textarea>
		<br>
		<input type="submit">
	</form>
"""

class MainPage(webapp2.RequestHandler):
	def write_form(self, user_input="", rot13=""):
		self.response.out.write(form % {"user_input": user_input,
										"rot13": escape_html(rot13)})

	def get(self):
		self.write_form()

	def post(self):
		user_input = self.request.get('user_input')
		rot13 = rot13cipher(user_input)
		self.write_form(user_input, rot13)

little_alpha = list(string.ascii_lowercase)

big_alpha = list(string.ascii_uppercase)

def escape_html(s):
	return cgi.escape(s, quote=True)

def rot13cipher(str):
	for i in str:
		for j in little_alpha:
			if i == j:
				str = str.replace(i, little_alpha[(little_alpha.index(j)+13)%26])
		for k in big_alpha:
			if i == k:
				str = str.replace(i, big_alpha[(big_alpha.index(k)+13)%26])
	return str

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
		

