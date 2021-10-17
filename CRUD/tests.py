from django.test import TestCase, Client
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.test.client import RequestFactory

from CRUD.views import crud_read, user_logout

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
    
    #tests to see if a user is loggged out upon using logout
    #expect response.status_code to be 302, and thus assert true
    def test_logout(self):
        c = Client() #client for testing
        c.login(username='testuser', password='12345') #login the user
        response = c.get('/logout/') #logout 
        self.assertEqual(response.status_code, 302) #if status code is 302, user is logged out

class ViewModelTests(TestCase):

    def setUp(self):
        #creates a user that is required to be logged in
        #to test the database functions
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        user = authenticate(username = 'testuser', password='1245')

    def test_add_to_database(self):
        print("todo")


    def test_view_database(self):
        
        c = Client() #client for testing
        c.login(username='testuser', password='12345') #login the user

        #create a GET request
        response = c.get('/search/')
        #get request from the search method
        request = response.wsgi_request
        request = crud_read(request)
        self.assertEqual(request.status_code, 200) #if status code is 200, the view worked as intended