
import webapp2
import cgi


def formBuilder(un='', pw='', pwm='', em=''):
    ''' This function handles building the html webpage that contains the
        user signup form.
    '''

    header = "<h1>User Signup</h1>"
    form = '''
    <form method="post">
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username"/ value={username}></td>
            </tr>
            <tr>
                <td>Passord: </td>
                <td><input type="password" name="password" value={password}></input></td>
            </tr>
            <tr>
                <td> Confirm Password: </td>
                <td><input type="password" name="pw_match" value={pw_match}></input></td>
            </tr>
            <tr>
                <td>E-mail (optional): </td>
                <td><input type="email" name="email" value={email}></input></td>
            </tr>
        </table>
        <input type="submit" value="Sign Up!">
    </form>
    '''.format(username=un, password=pw, pw_match=pwm, email=em)


    content = header + form
    return content


class MainHandler(webapp2.RequestHandler):

    def get(self):
        self.response.write(formBuilder())

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")
        pw_match = self.request.get("pw_match")
        email = self.request.get("email")




        self.response.write(formBuilder(username, password, pw_match, email))













app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
