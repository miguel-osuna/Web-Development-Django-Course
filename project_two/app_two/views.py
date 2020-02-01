from django.shortcuts import render
from django.http import HttpResponse
from app_two.models import Users
from app_two.forms import UsersForm

# Create your views here.


def index(request):
    return render(request, "app_two/index.html")


def help(request):
    return HttpResponse("I need your help")


def users(request):
    users_list = Users.objects.all()
    users_dict = {"users": users_list}
    return render(request, "app_two/users.html", context=users_dict)


def users_form(request):
    form = UsersForm()

    if request.method == "POST":
        form = UsersForm(request.POST)

        if form.is_valid():
            print("Form validation success")
            form.save(commit=True)
            return index(request)
        else:
            print("Error: Form Invalid")

    return render(request, "app_two/users_form.html", {"form": form})
