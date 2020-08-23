from django.db import models
from PIL import Image
from django import forms
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model as user_model
User = user_model()


VERIFY1= (
    ('---', '---'), 
)
LOGO= (
    ('LOGO', 'LOGO'), 
)
WEB_DESIGNS= (
    ('WEB DESIGNS', 'WEB DESIGNS'), 
)
GRAPHIC= (
    ('GRAPHIC DESIGNS', 'GRAPHIC DESIGNS'), 
)
CATEGORY_TYPE= (
    ('LOGO', 'LOGO'),
    ('BANNER ADS', 'BANNER ADS'),
    ('SIGNAGE', 'SIGNAGE'),
    ('WEB DESIGNS', 'WEB DESIGNS'),
)
THEME= (
    ('MINIMALIST', 'MINIMALIST'),
    ('MODERN', 'MODERN'),
    ('INNOVATIVE', 'INNOVATIVE'),
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
STATUS= (
    ('Ongoing', 'Ongoing'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled'),
    ('---', '---'),
)
RATINGS= (
    ('☆☆☆☆☆', '☆☆☆☆☆'),
    ('★☆☆☆☆', '★☆☆☆☆'),
    ('★★☆☆☆', '★★☆☆☆'),
    ('★★★☆☆', '★★★☆☆'),
    ('★★★★☆', '★★★★☆'),
    ('★★★★★', '★★★★★'),
)
class Post(models.Model):
    title = models.CharField('Title (Name your project commission)', max_length=100)
    content = models.TextField('Content (Give a thorough project description)',)
    category = models.CharField('Choose your project category', max_length=30, choices=CATEGORY_TYPE, default='LOGO')
    theme = models.CharField('What theme best suits your style?', max_length=30, choices=THEME, default='MINIMALIST')
    rate = models.CharField('Settled Rate (How much are you willing to pay for this project?)', max_length=100,  default='')
    city = models.CharField('Enter your city residence', max_length=30, choices=CITY, default='Malolos')
    street = models.CharField('Enter your barangay', max_length=30, choices=STREET, default='Tikay')
    contract = models.ImageField('Contract Agreement', upload_to='contract', default = 'contract.png')
    certificate = models.ImageField('Ownership Certificate', upload_to='certificates', default = 'unlock.png')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    verified = models.CharField(choices=VERIFY1, default='---', max_length=100)
    status = models.CharField('Your Project Status', max_length=30, choices=STATUS, default='---')

    class Meta:
        ordering = ['-dateposted']

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Post-Detail', kwargs={'pk': self.pk})

class Portfolio(models.Model):
    Expertise = models.CharField('Expertise (Name your best skill)', max_length=100)
    Background = models.TextField('Background (Tell us about your previous works and experiences)', )
    image1 = models.ImageField('Image (Attach your previous commissions here)', upload_to='portfolio_pics', default = 'plain.png')
    description1 = models.TextField('Project Description (What can you say about this project?)', blank=True )
    image2 = models.ImageField('Image (Attach your previous commissions here)', upload_to='portfolio_pics', default = 'plain.png')
    description2 = models.TextField('Project Description (What can you say about this project?)', blank=True )
    image3 = models.ImageField('Image (Attach your previous commissions here)', upload_to='portfolio_pics', default = 'plain.png')
    description3 = models.TextField('Project Description (What can you say about this project?)', blank=True )
    category = models.CharField('Choose your project category', max_length=30, choices=CATEGORY_TYPE, default='LOGO')
    theme = models.CharField('What theme best suits your style?', max_length=30, choices=THEME, default='MINIMALIST')
    rate = models.CharField('Rate of Pay', max_length=100,  default='')
    city = models.CharField('Enter your city residence', max_length=30, choices=CITY, default='Malolos')
    street = models.CharField('Enter your barangay', max_length=30, choices=STREET, default='Tikay')
    prescreen = models.ImageField('Likhanap Pre-screening Results', upload_to='portfolio_pics', default = 'prescreen.png')
    b1image= models.ImageField('Business 1 image', upload_to='business_image_feedbacks', default = 'blank.png')
    b1 = models.CharField('Business 1', max_length=50, blank=True)
    f1=models.TextField('Feedback 1', blank=True)
    r1 = models.CharField('Choose a Rating:', max_length=30, choices=RATINGS, default='☆☆☆☆☆')
    b2image= models.ImageField('Business 2 image', upload_to='business_image_feedbacks', default = 'blank.png')
    b2 = models.CharField('Business 2', max_length=50, blank=True)
    f2=models.TextField('Feedback 2', blank=True)
    r2 =  models.CharField('Choose a Rating:', max_length=30, choices=RATINGS, default='☆☆☆☆☆')
    b3image= models.ImageField('Business 3 image', upload_to='business_image_feedbacks', default = 'blank.png')
    b3 = models.CharField('Business 3', max_length=50, blank=True)
    f3=models.TextField('Feedback 3', blank=True)
    r3 =  models.CharField('Choose a Rating:', max_length=30, choices=RATINGS, default='☆☆☆☆☆')
    overallrating = models.ImageField('Overall Rating', upload_to='rating', default = 'R-0.png')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    verified = models.CharField(choices=VERIFY1, default='---', max_length=100)

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
    theme = models.CharField('What theme best suits your style?', max_length=30, choices=THEME, default='MINIMALIST')
    image = models.ImageField('Attach your image here', upload_to='post_pics', default = 'plain.png')
    rate = models.CharField('Settled Rate (How much are you willing to pay for this project?)', max_length=100,  default='')
    city = models.CharField('Enter your city residence', max_length=30, choices=CITY, default='Malolos')
    street = models.CharField('Enter your barangay', max_length=30, choices=STREET, default='Tikay')
    artist_username = models.CharField('Commission partner', max_length=100)
    contract = models.ImageField('Contract Agreement', upload_to='contract', default = 'contract.png')
    certificate = models.ImageField('Ownership Certificate', upload_to='certificates', default = 'unlock.png')
    status = models.CharField('Your Project Status', max_length=30, choices=STATUS, default='---')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Bid-Detail', kwargs={'pk': self.pk})

class Apply(models.Model):
    Expertise = models.CharField('Expertise (Name your best skill)', max_length=100)
    Background = models.TextField('Background (Tell us about your previous works and experiences)', )
    image1 = models.ImageField('Image (Attach your previous commissions here)', upload_to='portfolio_pics', default = 'plain.png')
    image2 = models.ImageField('Image (Attach your previous commissions here)', upload_to='portfolio_pics', default = 'plain.png')
    image3 = models.ImageField('Image (Attach your previous commissions here)', upload_to='portfolio_pics', default = 'plain.png')
    category = models.CharField('Choose your project category', max_length=30, choices=CATEGORY_TYPE, default='LOGO')
    theme = models.CharField('What theme best suits your style?', max_length=30, choices=THEME, default='MINIMALIST')
    rate = models.CharField('Rate of Pay', max_length=100,  default='')
    city = models.CharField('Enter your city residence', max_length=30, choices=CITY, default='Malolos')
    street = models.CharField('Enter your barangay', max_length=30, choices=STREET, default='Tikay')
    prescreen = models.ImageField('Likhanap Pre-screening Results', upload_to='portfolio_pics', default = 'plain.png')
    Business_username = models.CharField('Commission partner', max_length=100)
    b1image= models.ImageField('Business 1 image', upload_to='business_image_feedbacks', default = 'blank.png')
    b1 = models.CharField('Business 1', max_length=50, blank=True)
    f1=models.TextField('Feedback 1', blank=True)
    r1 =  models.CharField('Choose a Rating:', max_length=30, choices=RATINGS, default='☆☆☆☆☆')
    b2image= models.ImageField('Business 2 image', upload_to='business_image_feedbacks', default = 'blank.png')
    b2 = models.CharField('Business 2', max_length=50, blank=True)
    f2=models.TextField('Feedback 2', blank=True)
    r2 = models.CharField('Choose a Rating:', max_length=30, choices=RATINGS, default='☆☆☆☆☆')
    b3image= models.ImageField('Business 3 image', upload_to='business_image_feedbacks', default = 'blank.png')
    b3 = models.CharField('Business 3', max_length=50, blank=True)
    f3=models.TextField('Feedback 3', blank=True)
    r3 = models.CharField('Choose a Rating:', max_length=30, choices=RATINGS, default='☆☆☆☆☆')
    overallrating = models.ImageField('Overall Rating', upload_to='rating', default = 'R-0.png')
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.Expertise

    def get_absolute_url(self):
        return reverse('Apply-Detail', kwargs={'pk': self.pk})

class Accept(models.Model):
    Message = models.TextField('Message (Enter your message here)', )
    Business_username = models.CharField('Commission partner', max_length=100)
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.Business_username

    def get_absolute_url(self):
        return reverse('Accept-Detail', kwargs={'pk': self.pk})

class Employ(models.Model):
    Message = models.TextField('Message (Enter your message here)', )
    artist_username = models.CharField('Commission partner', max_length=100)
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.artist_username

    def get_absolute_url(self):
        return reverse('Employ-Detail', kwargs={'pk': self.pk})

class LikhanapFeedback(models.Model):
    Feedback = models.TextField('Feedback to Likhanap', )
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.Feedback

    def get_absolute_url(self):
        return reverse('LikhanapFeedback-Detail', kwargs={'pk': self.pk})

class Report(models.Model):
    Report = models.TextField('Report your complain about this artist:', )
    artist_username = models.CharField('Reported Artist:', max_length=100)
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.Report

    def get_absolute_url(self):
        return reverse('Report-Detail', kwargs={'pk': self.pk})

class Feedback(models.Model):
    Comment = models.TextField()
    rating = models.CharField('Choose a Rating:', max_length=30, choices=RATINGS, default='☆☆☆☆☆')
    artist_username = models.CharField('Commission Artist:', max_length=100)
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    class Meta:
        ordering = ['-dateposted']

    
    def __str__(self):
        return self.artist_username

    def get_absolute_url(self):
        return reverse('Feedback-Detail', kwargs={'pk': self.pk})

class LogoContract(models.Model):
    category = models.CharField('Project Category', max_length=30, choices=LOGO, default='LOGO')
    businessname = models.CharField('Business Name', max_length=100)
    ownername = models.CharField('Business Owner Name', max_length=100)
    address = models.CharField('Business Owner Address', max_length=100)
    image = models.ImageField('Please attach your valid signature (Recommended: .png, 850 x 480 px)', upload_to='signatures', default = 'plain.png')


    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.businessname

    def get_absolute_url(self):
        return reverse('LogoContract-Detail', kwargs={'pk': self.pk})

class LogoCertificate(models.Model):
    businessname = models.CharField('Business Name', max_length=100)
    ownername = models.CharField('Business Owner Name', max_length=100)
    artistname = models.CharField('Artist Full Name', max_length=100)
    logo = models.ImageField('Please your logo image here (Recommended: 800 x 800 px)', upload_to='logos', default = 'plain.png')

    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.artistname

    def get_absolute_url(self):
        return reverse('LogoCertificate-Detail', kwargs={'pk': self.pk})

class WebCertificate(models.Model):
    businessname = models.CharField('Business Name', max_length=100)
    ownername = models.CharField('Business Owner Name', max_length=100)
    artistname = models.CharField('Artist Full Name', max_length=100)
    link = models.CharField('Business URL Link', max_length=500)
    
    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.artistname

    def get_absolute_url(self):
        return reverse('WebCertificate-Detail', kwargs={'pk': self.pk})


class ALogoContract(models.Model):
    category = models.CharField('Project Category', max_length=30, choices=LOGO, default='LOGO')
    artistname = models.CharField('Full Name', max_length=100)
    address = models.CharField('Address', max_length=100)
    image = models.ImageField('Please attach your valid signature (Recommended: .png, 850 x 480 px)', upload_to='signatures', default = 'plain.png')


    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.artistname

    def get_absolute_url(self):
        return reverse('ALogoContract-Detail', kwargs={'pk': self.pk})

class AWebContract(models.Model):
    category = models.CharField('Project Category', max_length=30, choices=WEB_DESIGNS, default='WEB DESIGNS')
    artistname = models.CharField('Full Name', max_length=100)
    address = models.CharField('Address', max_length=100)
    image = models.ImageField('Please attach your valid signature (Recommended: .png, 850 x 480 px)', upload_to='signatures', default = 'plain.png')


    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.artistname

    def get_absolute_url(self):
        return reverse('AWebContract-Detail', kwargs={'pk': self.pk})

class WebContract(models.Model):
    category = models.CharField('Project Category', max_length=30, choices=WEB_DESIGNS, default='WEB DESIGNS')
    businessname = models.CharField('Business Name', max_length=100, default ='')
    ownername = models.CharField('Business Owner Name', max_length=100, default ='')
    address = models.CharField('Business Owner Address', max_length=100, default ='')
    image = models.ImageField('Please attach your valid signature (Recommended: .png, 850 x 480 px)', upload_to='signatures', default = 'plain.png')


    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.businessname

    def get_absolute_url(self):
        return reverse('WebContract-Detail', kwargs={'pk': self.pk})

class GraphicContract(models.Model):
    category = models.CharField('Project Category', max_length=30, choices=GRAPHIC, default='GRAPHIC DESIGNS')
    businessname = models.CharField('Business Name', max_length=100, default ='')
    ownername = models.CharField('Business Owner Name', max_length=100, default ='')
    address = models.CharField('Business Owner Address', max_length=100, default ='')
    image = models.ImageField('Please attach your valid signature (Recommended: .png, 850 x 480 px)', upload_to='signatures', default = 'plain.png')


    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.businessname

    def get_absolute_url(self):
        return reverse('GraphicContract-Detail', kwargs={'pk': self.pk})

class AGraphicContract(models.Model):
    category = models.CharField('Project Category', max_length=30, choices=GRAPHIC, default='GRAPHIC DESIGNS')
    artistname = models.CharField('Full Name', max_length=100)
    address = models.CharField('Address', max_length=100)
    image = models.ImageField('Please attach your valid signature (Recommended: .png, 850 x 480 px)', upload_to='signatures', default = 'plain.png')


    dateposted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.artistname

    def get_absolute_url(self):
       return reverse('AGraphicContract-Detail', kwargs={'pk': self.pk})





































































































































    