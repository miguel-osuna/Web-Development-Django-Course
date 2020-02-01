from django import forms
from app_two.models import Users


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data["first_name"]
        last_name = cleaned_data["last_name"]
        email = cleaned_data["email"]
