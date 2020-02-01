from django.shortcuts import render
from basicapp.forms import FormName
from basicapp.models import User

# Create your views here.


def index(request):
    return render(request, "basicapp/index.html")


def form_page(request):
    form = FormName()

    # Check to see if we get a POST request back
    if request.method == "POST":
        # In which case, we pass in that request
        form = FormName(request.POST)

        # Check to see if form is valid
        if form.is_valid():
            # Print form information in console
            print("Form Validation Success. Prints in console")
            print("Name: " + form.cleaned_data["name"])
            print("Email: " + form.cleaned_data["email"])
            print("Text: " + form.cleaned_data["text"])

    return render(request, "basicapp/form_page.html", {"form": form})
