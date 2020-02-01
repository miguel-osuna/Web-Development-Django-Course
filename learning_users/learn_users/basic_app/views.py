from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request, "basic_app/index.html")


def register(request):
    registered = False

    if request.method == "POST":
        # Get info from both forms
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check if forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save user form to Database
            user = user_form.save()

            # Hash the password with the algorithms
            user.set_password(user.password)

            # Now save the password
            user.save()

            # Don't save yet profile form, wait until modified
            profile = profile_form.save(commit=False)

            # Create the One to One Relationship from the models
            profile.user = user

            # Check if profile picture is provided
            if "profile_pic" in request.FILES:
                print("Found it")
                profile.profile_pic = request.FILES["profile_pic"]

            # Save profile form to Database
            profile.save()

            # Registration successful
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        #  It was not a HTTP Post request, so forms are render blank
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, "basic_app/registration.html", {"user_form": user_form, "profile_form": profile_form, "registered": registered})


@login_required
def test(request):
    return HttpResponse("You are logged in, congrats")


@login_required
def user_logout(request):
    # Logout the user
    logout(request)
    # Return to homepage
    return HttpResponseRedirect(reverse("index"))


def user_login(request):
    registered = False

    if request.method == "POST":
        # First get the username and password
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            # Check is the account is active
            if user.is_active:
                # Log the user in
                login(request, user)
                # Send the user back to some page
                return HttpResponseRedirect(reverse("index"))

            else:
                # If account is not active
                return HttpResponse("Account not active")

        else:
            print("Someone tried to login and failed")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login credentials")

    else:
        # Nothing has been provided for username or password
        return render(request, "basic_app/login.html", {})

    return render(request, "basic_app/login.html")
