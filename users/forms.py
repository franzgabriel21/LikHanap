from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from captcha.fields import CaptchaField

User = get_user_model()
USER_TYPE= [
    ('freelance', 'Freelancer'),
    ('business', 'Business Owner'),
    
    ]
CITY= [
    ('Malolos', 'Malolos'),
    ]    
STREET= [
    
('Anilao', 'Anilao'),	
('Atlag', 'Atlag'),	
('Babatnin', 'Babatnin'),
('Bagna', 'Bagna'),	
('Bagong Bayan', 'Bagong Bayan'),	
('Balayong', 'Balayong'),	
('Balite', 'Balite'),	
('Bangkal', 'Bangkal'),	
('Barihan', 'Barihan'),
('Bulihan', 'Bulihan'),
('Bungahan', 'Bungahan'),	
('Caingin', 'Caingin'),
('Calero', 'Calero'),	
('Caliligawan', 'Caliligawan'),	
('Canalate', 'Canalate'),	
('Caniogan', 'Caniogan'),	
('Catmon', 'Catmon'),	
('Cofradia', 'Cofradia'),
('Dakila', 'Dakila'),	
('Guinhawa', 'Guinhawa'),
('Ligas', 'Ligas'),		
('Liyang', 'Liyang'),		
('longos', 'Longos'),	
('Look 1st', 'Look 1st'),	
('Look 2nd', 'Look 2nd'),	
('Lugam', 'Lugam'),	
('Mabolo', 'Mabolo'),	
('Mambog', 'Mambog'),	
('Masile', 'Masile'),
('Matimbo', 'Matimbo'),	
('Mojon', 'Mojon'),	
('Namayan', 'Namayan'),	
('Niugan', 'Niugan'),	
('Pamarawan', 'Pamarawan'),	
('Panasahan', 'Panasahan'),	
('Pinagbakahan', 'Pinagbakahan'),	
('San Agustin', 'San Agustin'),	
('San Gabriel', 'San Gabriel'),	
('San Juan', 'San Juan'),	
('San Pablo', 'San Pablo'),	
('Santiago', 'Santiago'),	
('Santisima Trinidad', 'Santisima Trinidad'),	
('Santo Cristo', 'Santo Cristo'),		
('Santor', 'Santor'),	
('Santo Niño', 'Santo Niño'),	
('Santo Rosario', 'Santo Rosario'),	
('San Vicente', 'San Vicente'),	
('Sumapang Bata', 'Sumapang Bata'),	
('Sumapang Matanda', 'Sumapang Matanda'),	
('Taal', 'Taal'),
('Tikay', 'Tikay'),
    ]    
class UserRegisterForm(UserCreationForm):
     email = forms.EmailField()
     usertype= forms.CharField(label='I am a', widget=forms.Select(choices=USER_TYPE))
     city= forms.CharField(label='Residence city', widget=forms.Select(choices=CITY))
     street= forms.CharField(label='Barangay', widget=forms.Select(choices=STREET))     
     name = forms.CharField(label='Full Name/Name of Business', max_length=30, required = False)
     image = forms.ImageField(label='Profile Picture', required = False)
     captcha = CaptchaField()
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
      city = forms.CharField(label='Residence city', widget=forms.Select(choices=CITY))
      street= forms.CharField(label='Barangay', widget=forms.Select(choices=STREET))  
      class Meta:
        model = User
        fields = ['username', 'email', 'city', 'street']
class ProfileUpdateForm(forms.ModelForm):
      class Meta:
        model = Profile
        fields = ['image']
