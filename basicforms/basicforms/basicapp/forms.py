from django import forms
from django.core import validators


class FormName(forms.Form):
    name = forms.CharField(max_length=256, required=True)
    email = forms.EmailField(
        max_length=256, required=True, widget=forms.EmailInput)
    verify_email = forms.EmailField(
        required=False, widget=forms.EmailInput, label="Re-enter your email")
    text = forms.CharField(max_length=256, required=True,
                           widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        name = all_clean_data["name"]
        email = all_clean_data["email"]
        verify_email = all_clean_data["verify_email"]
        text = all_clean_data["text"]

        if email != verify_email:
            raise forms.ValidationError("Please confirm your email")
