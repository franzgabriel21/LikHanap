from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

User = get_user_model()
USER_TYPE= [
    ('freelance', 'Freelancer'),
    ('business', 'Business Owner'),
    
    ]
CITY= [
    ('malolos', 'Malolos'),
    ]    
STREET= [
    ('bungahan', 'Bungahan'),
    ('longos', 'Longos'),
    ('caliligawan', 'Caliligawan'),
    ('tikay', 'Tikay'),
    ('santol', 'Santol'),
    ]    
class UserRegisterForm(UserCreationForm):
     email = forms.EmailField()
     usertype= forms.CharField(label='I am a', widget=forms.Select(choices=USER_TYPE))
     city= forms.CharField(label='Residence city', widget=forms.Select(choices=CITY))
     street= forms.CharField(label='Residential street', widget=forms.Select(choices=STREET))     
     name = forms.CharField(label='Full Name/Name of Business', max_length=30, required = False)
     image = forms.ImageField(label='Profile Picture', required = False)
    
     class Meta:
        model = User
        fields = ['username', 'email', 'name', 'usertype', 'city','street', 'password1', 'password2']
     def save(self, commit=True):
             user= super(UserRegisterForm, self).save(commit=False)
             user.name = self.cleaned_data['name']
             user.usertype = self.cleaned_data['usertype']
             user.city = self.cleaned_data['city']
             user.street = self.cleaned_data['street']
             
             if commit:
                     user.save()
             return user

class UserUpdateForm(forms.ModelForm):
      email = forms.EmailField()
      class Meta:
        model = User
        fields = ['username', 'email']
class ProfileUpdateForm(forms.ModelForm):
      class Meta:
        model = Profile
        fields = ['image']
