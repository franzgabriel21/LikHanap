from django.db import models
from PIL import Image
from django import forms
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model as user_model
User = user_model()

CATEGORY_TYPE= (
    ('LOGO', 'LOGO'),
    ('TARPAULIN LAYOUT', 'TARPAULIN LAYOUT'),
    ('ADVERTISEMENT LAYOUT', 'ADVERTISEMENT LAYOUT'),
    ('INVITATION LAYOUT', 'INVITATION LAYOUT'),
    ('INTERIOR DESIGN', 'INTERIOR DESIGN'),
)
LOCATION_TYPE= (
    ('Malolos, Bungahan', 'Malolos, Bungahan'),
    ('Malolos, Longos', 'Malolos, Longos'),
    ('Malolos, Caliligawan', 'Malolos, Caliligawan'),
    ('Malolos, Tikay', 'Malolos, Tikay'),
    ('Malolos, Santol', 'Malolos, Santol'),
)  
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_TYPE, default='LOGO')
    image = models.ImageField(upload_to='post_pics', default = 'plain.jpg')
    location = models.CharField(max_length=30, choices=LOCATION_TYPE, default='Malolos, Bungahan')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Post-Detail', kwargs={'pk': self.pk})
 

class Portfolio(models.Model):
    Expertise = models.CharField(max_length=100)
    Background = models.TextField()
    image1 = models.ImageField(upload_to='portfolio_pics', default = 'plain.jpg')
    image2 = models.ImageField(upload_to='portfolio_pics', default = 'plain.jpg')
    image3 = models.ImageField(upload_to='portfolio_pics', default = 'plain.jpg')
    category = models.CharField(max_length=30, choices=CATEGORY_TYPE, default='LOGO')
    location = models.CharField(max_length=30, choices=LOCATION_TYPE, default='Malolos, Bungahan')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.Expertise

    def get_absolute_url(self):
        return reverse('Portfolio-Detail', kwargs={'pk': self.pk})
 
class Bid(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_TYPE, default='LOGO')
    image = models.ImageField(upload_to='post_pics', default = 'plain.jpg')
    location = models.CharField(max_length=30, choices=LOCATION_TYPE, default='Malolos, Bungahan')
    artist_username = models.CharField(max_length=100)
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Bid-Detail', kwargs={'pk': self.pk})

class Apply(models.Model):
    Expertise = models.CharField(max_length=100)
    Background = models.TextField()
    image1 = models.ImageField(upload_to='portfolio_pics', default = 'plain.jpg')
    image2 = models.ImageField(upload_to='portfolio_pics', default = 'plain.jpg')
    image3 = models.ImageField(upload_to='portfolio_pics', default = 'plain.jpg')
    category = models.CharField(max_length=30, choices=CATEGORY_TYPE, default='LOGO')
    location = models.CharField(max_length=30, choices=LOCATION_TYPE, default='Malolos, Bungahan')
    Business_username = models.CharField(max_length=100)
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.Expertise

    def get_absolute_url(self):
        return reverse('Apply-Detail', kwargs={'pk': self.pk})

class Accept(models.Model):
    Message = models.TextField()
    Business_username = models.CharField(max_length=100, default='')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.Business_username

    def get_absolute_url(self):
        return reverse('Accept-Detail', kwargs={'pk': self.pk})

class Employ(models.Model):
    Message = models.TextField()
    artist_username = models.CharField(max_length=100, default='')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.artist_username

    def get_absolute_url(self):
        return reverse('Employ-Detail', kwargs={'pk': self.pk})
 







































































































































    