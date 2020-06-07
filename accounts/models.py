from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyAccountManager(BaseUserManager):
	def create_user(self, username, email, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(username=username,
			email=self.normalize_email(email),
			
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
            username=username,
			email=self.normalize_email(email),
			password=password,
			
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		
		user.save(using=self._db)
        
		return user


class User(AbstractBaseUser):
    username 				= models.CharField(max_length=30, unique=True)
    email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
    name 				    = models.CharField(max_length=30, unique=True)
    usertype 				= models.CharField(max_length=30)
    city 					= models.CharField(max_length=30)
    street	 				= models.CharField(max_length=30)
    verified				= models.CharField(max_length=30, default='False')	
    date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin				= models.BooleanField(default=False)
    is_active				= models.BooleanField(default=True)
    is_staff				= models.BooleanField(default=False)
    is_superuser			= models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True



