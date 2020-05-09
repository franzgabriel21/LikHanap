from django.db import models
from PIL import Image
from django import forms
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model as user_model
User = user_model()

VERIFY1= (
    ('False', 'False'),  
)
VERIFY2= (
    ('True', 'True'),  
)
CATEGORY_TYPE= (
    ('LOGO', 'LOGO'),
    ('BRAND TAGLINES', 'BRAND TAGLINES'),
    ('ADVERTISEMENT LAYOUT', 'ADVERTISEMENT LAYOUT'),
    ('VISUAL ARTS', 'VISUAL ARTS'),
    ('INTERIOR DESIGN', 'INTERIOR DESIGN'),
)
CITY= (
    ('Malolos', 'Malolos'),
    )    
STREET= (
    
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
) 
class Post(models.Model):
    title = models.CharField('Title (Name your project commission)', max_length=100)
    content = models.TextField('Content (Give a thorough project description)',)
    category = models.CharField('Choose your project category', max_length=30, choices=CATEGORY_TYPE, default='LOGO')
    city = models.CharField('Enter your city residence', max_length=30, choices=CITY, default='Malolos')
    street = models.CharField('Enter your barangay', max_length=30, choices=STREET, default='Tikay')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    verified = models.CharField(choices=VERIFY1, default='False', max_length=100)

    class Meta:
        ordering = ['-dateposted']

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Post-Detail', kwargs={'pk': self.pk})

class VerifiedPost(models.Model):
    title = models.CharField('Title (Name your project commission)', max_length=100)
    content = models.TextField('Content (Give a thorough project description)',)
    category = models.CharField('Choose your project category', max_length=30, choices=CATEGORY_TYPE, default='LOGO')
    city = models.CharField('Enter your city residence', max_length=30, choices=CITY, default='Malolos')
    street = models.CharField('Enter your barangay', max_length=30, choices=STREET, default='Tikay')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    verified = models.CharField(choices=VERIFY2, default='True', max_length=100)

    class Meta:
        ordering = ['-dateposted']

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('VerifiedPost-Detail', kwargs={'pk': self.pk})
 

class Portfolio(models.Model):
    Expertise = models.CharField('Expertise (Name your best skill)', max_length=100)
    Background = models.TextField('Background (Tell us about your previous works and experiences)', )
    image1 = models.ImageField('Image (Attach your previous commissions here)', upload_to='portfolio_pics', default = 'plain.jpg')
    image2 = models.ImageField('Image (Attach your previous commissions here)', upload_to='portfolio_pics', default = 'plain.jpg')
    image3 = models.ImageField('Image (Attach your previous commissions here)', upload_to='portfolio_pics', default = 'plain.jpg')
    category = models.CharField('Choose your project category', max_length=30, choices=CATEGORY_TYPE, default='LOGO')
    city = models.CharField('Enter your city residence', max_length=30, choices=CITY, default='Malolos')
    street = models.CharField('Enter your barangay', max_length=30, choices=STREET, default='Tikay')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        ordering = ['-dateposted']


    def __str__(self):
        return self.Expertise

    def get_absolute_url(self):
        return reverse('Portfolio-Detail', kwargs={'pk': self.pk})
 
class Bid(models.Model):
    title = models.CharField('Title (Name your project commission)', max_length=100)
    content = models.TextField('Content (Give a thorough project description)',)
    category = models.CharField('Choose your project category', max_length=30, choices=CATEGORY_TYPE, default='LOGO')
    image = models.ImageField('Attach your image here', upload_to='post_pics', default = 'plain.jpg')
    city = models.CharField('Enter your city residence', max_length=30, choices=CITY, default='Malolos')
    street = models.CharField('Enter your barangay', max_length=30, choices=STREET, default='Tikay')
    artist_username = models.CharField('Please type your commission partner', max_length=100)
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Bid-Detail', kwargs={'pk': self.pk})

class Apply(models.Model):
    Expertise = models.CharField('Expertise (Name your best skill)', max_length=100)
    Background = models.TextField('Background (Tell us about your previous works and experiences)', )
    image1 = models.ImageField('Image (Attach your previous commissions here)', upload_to='portfolio_pics', default = 'plain.jpg')
    image2 = models.ImageField('Image (Attach your previous commissions here)', upload_to='portfolio_pics', default = 'plain.jpg')
    image3 = models.ImageField('Image (Attach your previous commissions here)', upload_to='portfolio_pics', default = 'plain.jpg')
    category = models.CharField('Choose your project category', max_length=30, choices=CATEGORY_TYPE, default='LOGO')
    city = models.CharField('Enter your city residence', max_length=30, choices=CITY, default='Malolos')
    street = models.CharField('Enter your barangay', max_length=30, choices=STREET, default='Tikay')
    Business_username = models.CharField('Please type your commission partner', max_length=100)
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.Expertise

    def get_absolute_url(self):
        return reverse('Apply-Detail', kwargs={'pk': self.pk})

class Accept(models.Model):
    Message = models.TextField('Message (Enter your message here)', )
    Business_username = models.CharField('Please type your commission partner', max_length=100, default='')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.Business_username

    def get_absolute_url(self):
        return reverse('Accept-Detail', kwargs={'pk': self.pk})

class Employ(models.Model):
    Message = models.TextField('Message (Enter your message here)', )
    artist_username = models.CharField('Please type your commission partner', max_length=100, default='')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.artist_username

    def get_absolute_url(self):
        return reverse('Employ-Detail', kwargs={'pk': self.pk})
 
class Feedback(models.Model):
    Comment = models.TextField()
    artist_username = models.CharField('Send this feedback to:', max_length=100, default='')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        ordering = ['-dateposted']

    
    def __str__(self):
        return self.artist_username

    def get_absolute_url(self):
        return reverse('Feedback-Detail', kwargs={'pk': self.pk})









































































































































    