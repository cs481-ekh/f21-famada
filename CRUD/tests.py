from django.test import TestCase, Client
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.test.client import RequestFactory

from CRUD.views import crud_read, user_logout, crud_add_rows

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


    def test_view_database(self):
        
        c = Client() #client for testing
        c.login(username='testuser', password='12345') #login the user

        #create a GET request
        response = c.get('/search/')
        #get request from the search method
        request = response.wsgi_request
        request = crud_read(request)
        self.assertEqual(request.status_code, 200) #if status code is 200, the view worked as intended

    def test_add_to_database(self):
        c = Client()
        c.login(username='testuser', password='12345')

        response = c.get('/add/')
        #checking to see if response went to proper page
        self.assertEqual(response.status_code, 200)

        #create a test data entry to be entered into database
        #use implemetation of adding to database
        #check to see if that entry is in database
        #assert true if so else assert false
        a_f_eaf_c_crs_list = ""
        semester = "fa19"
        first_name = "Test"
        last_name = "Tester"
        #date_of_birth = "2021/18/10"
        employeeID = 123456789
        step_rate = "step 1"
        I9_completed = "2021/18/20"
        I9_greater_than_3_years = 1
        background_passed = "Y"
        cv_resume = 2021
        masters = "Yes"
        CTL_notified = "2021/18/10"
        address = "Test address"
        city = "Test city"
        state = "Test state"
        zip = 123456
        primary_email = "test@test.com"
        primary_phone = "555-555-5555"

        request = [a_f_eaf_c_crs_list, semester, first_name, last_name, employeeID, step_rate, I9_completed, I9_greater_than_3_years, background_passed,
            cv_resume, masters, CTL_notified, address, city, state, zip, primary_email, primary_phone]

        # response = crud_add_rows(request)
        # #if adding did not fail, should have response code of 200 which means adding was successful
        # self.assertEqual(response.status_code, 200)
    
    #same test as testing add, but expect test to fail due to duplicate ID
    def test_duplicate_id(self):
        c = Client()
        c.login(username='testuser', password='12345')

        response = c.get('/add/')
        #checking to see if response went to proper page
        self.assertEqual(response.status_code, 200)

        #create a test data entry to be entered into database
        #use implemetation of adding to database
        #check to see if that entry is in database
        #assert true if so else assert false
        a_f_eaf_c_crs_list = ""
        semester = "fa19"
        first_name = "Test"
        last_name = "Tester"
        #date_of_birth = "2021/18/10"
        employeeID = 123456789
        step_rate = "step 1"
        I9_completed = "2021/18/20"
        I9_greater_than_3_years = 1
        background_passed = "Y"
        cv_resume = 2021
        masters = "Yes"
        CTL_notified = "2021/18/10"
        address = "Test address"
        city = "Test city"
        state = "Test state"
        zip = 123456
        primary_email = "test@test.com"
        primary_phone = "555-555-5555"

        request = [a_f_eaf_c_crs_list, semester, first_name, last_name, employeeID, step_rate, I9_completed, I9_greater_than_3_years, background_passed,
            cv_resume, masters, CTL_notified, address, city, state, zip, primary_email, primary_phone]

        # response = crud_add_rows(request)
        # #if adding failed, should have response code of 406 which means a mistake was made
        # self.assertEqual(response.status_code, 406)

    def test_delete(self):
        c = Client()
        c.login(username='testuser', password='12345')
        response = c.get('/search/')
        #checking to see if response went to proper page
        self.assertEqual(response.status_code, 200)

        #request = []    
        #response = crud_read(response)
        
        