from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'w-full p-3 rounded-md','placeholder':'Username...'}))
    password=forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'w-full p-3 rounded-md','placeholder':'Username...'}))

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email address...'}))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'w-full mt-3 p-3'
        self.fields['username'].widget.attrs['placeholder'] = 'User name...'
        self.fields['username'].help_text = '<span class="form-text text-sm text-gray-400"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        
        self.fields['email'].widget.attrs['class'] = 'w-full mt-3 p-3'
        self.fields['email'].widget.attrs['placeholder'] = 'User name...'
        self.fields['email'].help_text = '<span class="form-text text-sm text-gray-400"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'w-full mt-3 p-3'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].help_text = '<ul class="form-text text-sm text-gray-400 small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'w-full mt-3 p-3'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].help_text = '<span class="form-text text-sm text-gray-400"><small>Enter the same password as before, for verification.</small></span>'	
