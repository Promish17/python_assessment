from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.EmailField()
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    # password = forms.CharField(widget = forms.PasswordInput)
    # confirm_password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # print("hello ---------- %s", User.password)
        # print("hello hi  ---------- %s", user.password2)
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        # for i in user:
        print("user data ----------- %s", user)
        # print("hello ---------- %s", user.password1)
        # print("hello hi  ---------- %s", user.password2)
        # user.fullname = self.cleaned_data["fullname"]
        # user.email = self.cleaned_data["email"]
        # if commit:
        #     user.save()
        # return user

