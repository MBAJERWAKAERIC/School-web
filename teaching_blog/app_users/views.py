from django.shortcuts import render
from django.http import HttpResponse
from app_users.forms import UserForm, UserProfileInfoForm
# Create your views here.

def index(request):
    return HttpResponse('this is my first page')

    
def register(request):

        registered = False

        if request.method == "POST":
            userform = UserForm(data=request.POS)
            profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

  
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

        return render(request, 'app_users/registration.html',
                             {'registered':registered,
                              'user_form':user_form,
                             'profile_form':profile_form})




