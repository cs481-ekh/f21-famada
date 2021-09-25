from django.test import TestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your tests here.

class LoginModelTests(TestCase):

    #tests to see if the login system prevents login upon wrong password
    #expect test to pass (login system refuses authenitcation)
    def test_password(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        user = authenticate(username = 'testuser', password='1245') #user returns None if invalid login, this password is wrong so test it shouldn't authenticate
        if user is not None: #if valid login, test fails
            assert False
        else: #if invalid login, test passes
            assert True