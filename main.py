
import webapp2
import cgi


def formBuilder(input=''):
    ''' This function handles building the html webpage that contains the 
        user signup form.
    '''

    header = "<h1>User Signup</h1>"
    form = '''
    <table>
        <tr>
            <td>Username: </td>
            <td><input type="text" name="username"/></td>
        </tr>
        <tr>
            <td>Passord: </td>
            <td><input type="text" name="password"></input></td>
        </tr>
        <tr>
            <td> Confirm Password: </td>
            <td><input type="text" name="pw_match"></input></td>
        </tr>
        <tr>
            <td>E-mail (optional): </td>
            <td><input type="text" name="email"></input></td>
        </tr>
    </table>
    '''


    content = header + form
    return content


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(formBuilder())








app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
