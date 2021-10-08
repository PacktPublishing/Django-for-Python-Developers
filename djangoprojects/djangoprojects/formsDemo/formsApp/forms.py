from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):
    GENDER = [('male','MALE'),('female','FEMALE')]
    firstName = forms.CharField(required=False,validators=
    [validators.MinLengthValidator(5),validators.MaxLengthValidator(20)])
    lastName = forms.CharField()
    email = forms.EmailField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    password= forms.CharField(widget=forms.PasswordInput)
    ssn=forms.IntegerField

"""
    def clean(self):
        user_cleaned_data = super().clean()
        inputFirstName = user_cleaned_data['firstName']
        if len(inputFirstName)>20:
            raise forms.ValidationError('The max length of firstName is 20 characters')

    def clean_firstName(self):
        inputFirstName = self.cleaned_data['firstName']
        if len(inputFirstName)>20:
            raise forms.ValidationError('The max length of firstName is 20 characters')
        return inputFirstName

    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@')==-1:
            raise forms.ValidationError('The email should contain @')
        return inputEmail
"""
