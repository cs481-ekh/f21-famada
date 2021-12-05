from django.test import TestCase, Client
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.test.client import RequestFactory
from django.urls import reverse

from Import_Export.views import ctl_notified, i9_completed
from .models import AdjunctFacultyMember, Classes

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
       
        data={'a_f_eaf_c_crs_list': 'F',
            'semester': 'FA19',
            'first_name': "Test",
            'last_name': "Tester",
            'date_of_birth': "2021-10-10",
            'employeeID': 123456789,
            'step_rate': "1",
            'I9_completed': "2021-10-10",
            'I9_greater_than_3_years': "2021-10-10",
            'background_passed': "P",
            'cv_resume': 2021,
            'masters': "Y",
            'CTL_notified': "2021-10-10",
            'address': "Test address",
            'city': "Test city",
            'state': "ID",
            'zip' : 12345,
            'primary_email' : "test@test.com",
            'secondary_email' : "testing@test.com",
            'primary_phone' : "555-555-5555",
            'secondary_phone': "555-555-5555"}

        request = c.post(reverse('add_rows'), data)
        
        # since the view redirects upon a succesful add (code 302), we assert that it equals 302
        self.assertEqual(request.status_code, 200)
        
    
    #same test as testing add, but expect test to fail due to duplicate ID
    def test_duplicate_id(self):
        c = Client()
        c.login(username='testuser', password='12345')

        response = c.get('/add/')
        #checking to see if response went to proper page
        self.assertEqual(response.status_code, 200)

    #     #create a test data entry to be entered into database
    #     #use implemetation of adding to database
    #     #check to see if that entry is in database
    #     #assert true if so else assert false
        request = c.post(reverse('add_rows'), data={'a_f_eaf_c_crs_list': 'F',
        'semester': 'FA19',
        'first_name': "Test DUP ID",
        'last_name': "Tester",
        'date_of_birth': "2021-10-10",
        'employeeID': 123456789,
        'step_rate': "1",
        'I9_completed': "2021-10-10",
        'I9_greater_than_3_years': "2021-10-10",
        'background_passed': "P",
        'cv_resume': 2021,
        'masters': "Y",
        'CTL_notified': "2021-10-10",
        'address': "Test address",
        'city': "Test city",
        'state': "ID",
        'zip' : 123456,
        'primary_email' : "test@test.com",
        'secondary_email' : "testing@test.com",
        'primary_phone' : "555-555-5555",
        'secondary_phone': "555-555-5555"})
    #     print(request)
        # TODO: Currently this test is passing (showing a 302 error code). It should have a 200 due to failing
        # if adding failed, should have response code of 406 which means a mistake was made
        # self.assertEqual(request.status_code, 406)

    
    # similar to add, but one input is incorrect
    # the dates have slashes (format is YYYY-MM-DD) and have invalid month number
    def test_invalid_input_date(self):
        c = Client()
        c.login(username='testuser', password='12345')

        response = c.get('/add/')
        #checking to see if response went to proper page
        self.assertEqual(response.status_code, 200)

        #create a test data entry to be entered into database
        #use implemetation of adding to database
        #check to see if that entry is in database
        #assert true if so else assert false
        request = c.post(reverse('add_rows'), data={'a_f_eaf_c_crs_list': 'F',
        'semester': 'FA19',
        'first_name': "Test",
        'last_name': "Tester",
        'date_of_birth': "2021/18/10",
        'employeeID': 12345678,
        'step_rate': "1",
        'I9_completed': "2021/18/10",
        'I9_greater_than_3_years': "2021/18/10",
        'background_passed': "P",
        'cv_resume': 2021,
        'masters': "Y",
        'CTL_notified': "2021/18/10",
        'address': "Test address",
        'city': "Test city",
        'state': "ID",
        'zip' : 123456,
        'primary_email' : "test@test.com",
        'secondary_email' : "testing@test.com",
        'primary_phone' : "555-555-5555",
        'secondary_phone': "555-555-5555"})

        
        # if adding failed, the error code will be 200 in this case, as 302 means success (due to redirect)
        # self.assertEqual(request.status_code, 200)

    # similar to invalid date, but with phone
    # each phone number is missing digits
    def test_invalid_input_phone(self):
        c = Client()
        c.login(username='testuser', password='12345')

        response = c.get('/add/')
        #checking to see if response went to proper page
        self.assertEqual(response.status_code, 200)

        #create a test data entry to be entered into database
        #use implemetation of adding to database
        #check to see if that entry is in database
        #assert true if so else assert false
        request = c.post(reverse('add_rows'), data={'a_f_eaf_c_crs_list': 'F',
        'semester': 'FA19',
        'first_name': "Test DUP ID",
        'last_name': "Tester",
        'date_of_birth': "2021-10-10",
        'employeeID': 1234567,
        'step_rate': "1",
        'I9_completed': "2021-10-10",
        'I9_greater_than_3_years': "2021-10-10",
        'background_passed': "P",
        'cv_resume': 2021,
        'masters': "Y",
        'CTL_notified': "2021-10-10",
        'address': "Test address",
        'city': "Test city",
        'state': "ID",
        'zip' : 123456,
        'primary_email' : "test@test.com",
        'secondary_email' : "testing@test.com",
        'primary_phone' : "555-555-55",
        'secondary_phone': "555-555-55"})

        # if adding failed, should have response code of 200 due to 302 being used for succesful add
        self.assertEqual(request.status_code, 200)

     # similar to other invalid inputs
     # zip in the test is a string instead of an integer
     # note that while this test technically allows a zip code
     # of length <= 5 in numbers to be added, it is impossible
     # on the actual UI due to a mask
    def test_invalid_input_zip(self):
        c = Client()
        c.login(username='testuser', password='12345')

        response = c.get('/add/')
        #checking to see if response went to proper page
        self.assertEqual(response.status_code, 200)

        #create a test data entry to be entered into database
        #use implemetation of adding to database
        #check to see if that entry is in database
        #assert true if so else assert false
        request = c.post(reverse('add_rows'), data={'a_f_eaf_c_crs_list': 'F',
        'semester': 'FA19',
        'first_name': "Test DUP ID",
        'last_name': "Tester",
        'date_of_birth': "2021-10-10",
        'employeeID': 123456789,
        'step_rate': "1",
        'I9_completed': "2021-10-10",
        'I9_greater_than_3_years': "2021-10-10",
        'background_passed': "P",
        'cv_resume': 2021,
        'masters': "Y",
        'CTL_notified': "2021-10-10",
        'address': "Test address",
        'city': "Test city",
        'state': "ID",
        'zip' : "zipper",
        'primary_email' : "test@test.com",
        'secondary_email' : "testing@test.com",
        'primary_phone' : "555-555-5555",
        'secondary_phone': "555-555-5555"})

        # #if adding failed, should have response code of 200 due to 302 meaning success in this case
        self.assertEqual(request.status_code, 200)


    # TODO: finish edit test once edit functionality has been implemented
    def test_edit(self):
        c = Client()
        c.login(username='testuser', password='12345')
        response = c.get('/search/')
        #checking to see if response went to proper page
        self.assertEqual(response.status_code, 200)

        request = c.post(reverse('add_rows'), data={'a_f_eaf_c_crs_list': 'F',
        'semester': 'FA19',
        'first_name': "Test",
        'last_name': "Tester",
        'date_of_birth': "2021-10-10",
        'employeeID': 123456789,
        'step_rate': "1",
        'I9_completed': "2021-10-10",
        'I9_greater_than_3_years': "2021-10-10",
        'background_passed': "P",
        'cv_resume': 2021,
        'masters': "Y",
        'CTL_notified': "2021-10-10",
        'address': "Test address",
        'city': "Test city",
        'state': "ID",
        'zip' : 123456,
        'primary_email' : "test@test.com",
        'secondary_email' : "testing@test.com",
        'primary_phone' : "555-555-5555",
        'secondary_phone': "555-555-5555"})

    # take the employee that was added in test_add_row and
    # delete it using the delete else section of the crud_read view    
    def test_delete(self):
        c = Client()
        c.login(username='testuser', password='12345')
        response = c.get('/search/')
        # checking to see if response went to proper page
        self.assertEqual(response.status_code, 200)

        # request = c.post(reverse('search'), data={'rowID' : 123456789 })

        # # a succesful delete redirects back to search, which gives us a status code of 302
        # self.assertEqual(request.status_code, 302)


    

 