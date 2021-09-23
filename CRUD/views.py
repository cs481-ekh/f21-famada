from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.

def user_login(request):
    # if request.user.is_authenticated:
    #     # redirect here to main landing page
    #     return
    if request.method == 'GET':
        return render(request, 'login.html')
    # else:
    #     user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    #
    #     if user is None:
    #         return render(request, 'pagenamehere', {'form': AuthenticationForm(), 'error': 'Invalid Credentials'})
    #     else:
    #         login(request, user)
    #         if 'next' in request.POST:
    #             # check for case next is logout? else redirect to next
    #             return
    #         return  # redirect to landing page
