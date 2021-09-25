from django.test import TestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your tests here.

class LoginModelTests(TestCase):

    def test_password(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        user = authenticate(username = 'testuser', password='1245') #user returns None if invalid login
        if user is None: #if valid login, test fails
            assert False
        else: #if invalid login, test passes
            assert True