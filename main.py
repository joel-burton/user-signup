
import webapp2
import cgi
import re



username_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
password_RE = re.compile(r"^.{3,20}$")
email_RE    = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def usernameValid(username):
    return username_RE.match(username)


def passwordValid(password):
    return password_RE.match(password)


def matcher(var1, var2):
    # intention for use to check that password entries match
    return var1 == var2


def emailValid(address):
    return email_RE.match(address)





def formBuilder(username="", password="", pw_match="", email="",
                username_error="", password_error="",
                pw_match_error="", email_error=""):
    ''' This function handles building the html webpage that contains the
        user signup form.
    '''

    head = '''
    <head>
        <style>
            .error {
                color: red;
            }
        </style>
    </head>
    '''
    header = "<h1>User Signup</h1>"
    form = '''
    <form method="post">
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username"/ value={username}></td>
                <td class="error">{un_invalid}</td>
            </tr>
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" value={password}></input></td>
                <td class="error">{pw_invalid}</td>
            </tr>
            <tr>
                <td> Confirm Password: </td>
                <td><input type="password" name="pw_match" value={pw_match}></input></td>
                <td class="error">{not_matching}</td>
            </tr>
            <tr>
                <td>E-mail (optional): </td>
                <td><input type="email" name="email" value={email}></input></td>
                <td class ="error">{em_invalid}</td>
            </tr>
        </table>
        <input type="submit" value="Sign Up!">
    </form>
    '''.format(
    username = cgi.escape(username, quote=True),
    password = cgi.escape(password, quote=True),
    pw_match = cgi.escape(pw_match, quote=True),
    email = cgi.escape(email, quote=True),
    un_invalid = username_error,
    pw_invalid = password_error,
    not_matching = pw_match_error,
    em_invalid = email_error,
    )


    content = head + header + form
    return content


class MainHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write(formBuilder())

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        pw_match = self.request.get("pw_match")
        email = self.request.get("email")

        username_error = ""
        password_error = ""
        pw_match_error = ""
        email_error    = ""



        if len(username) == 0:
            username_error = "Please enter a username."

        elif not usernameValid(username):
            username = ""
            username_error = "That is not a valid username. Please try a new username."


        if len(password) == 0:
            password_error = "Please enter a password."

        elif not passwordValid(password):
            password_error = "That is not a valid password. Please enter a new password."

        elif len(pw_match) == 0:
            pw_match_error = "You didn't confirm your password. Please re-enter and confirm."

        elif not matcher(password, pw_match):
            pw_match_error = "Your passwords did not match. Please try again."


        if email and not emailValid(email):
            email_error = "That is not a vaild email address."


        # reset the passwords to blank for security
        password = ""
        pw_match = ""


        if username_error == "" and password_error == "" and pw_match_error == "" and email_error =="":
            self.redirect("/welcome?username={username}".format(username=username))

        else:
            self.response.write(formBuilder(username, password, pw_match, email,
                                            username_error, password_error,
                                            pw_match_error, email_error))





class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        header = '''<h1>Welcome, {user}!</h1>'''.format(user = username)
        body = '''<h3>Thanks for signing up today!</h3>'''

        content = header + body

        self.response.write(content)









app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler),
], debug=True)
