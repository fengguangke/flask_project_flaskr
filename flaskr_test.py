import unittest
import flaskr

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flaskr.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        assert 'python dictionary object' in rv.data

    def test_login_error(self):
        rv = self.app.post('/login',data={'username':'fengguangke','password':'123123'},follow_redirects=True)
        print(rv.data)
        assert 'invalid password' in rv.data

    def test_logout(self):
        rv = self.app.post('/login', data={'username': 'fengguangke', 'password': '123456'}, follow_redirects=True)
        rv = self.app.get('/logout',follow_redirects=True)
        assert 'You were logged out' in rv.data

    def test_add_message(self):
        rv = self.app.post('/login',data={'username': 'fengguangke', 'password': '123456'}, follow_redirects=True)
        rv = self.app.post('/add',data = {'title':'<Hello>','text':'<strong>HTML</strong> allowed here'}, follow_redirects=True)
        assert 'New entry was successfully posted' in rv.data
        assert '<strong>HTML</strong> allowed here' in rv.data

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main



