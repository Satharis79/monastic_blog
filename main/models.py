from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from .choices import TITLE_CHOICES

class CustomAccountManager(BaseUserManager):
    def create_user(self, user_name, password=None, **kwargs):
        monk = self.model(user_name=user_name, **kwargs)
        monk.set_password(password)
        monk.save(using=self._db)
        return monk

    def create_superuser(self, user_name, password=None, **kwargs):
        monk = self.create_user(user_name, password, **kwargs)
        monk.is_staff = True
        monk.is_superuser = True                                
        monk.save(using=self._db)
        return monk

class Monk(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField('Username', max_length=100, unique=True)
    first_name = models.CharField('First name', max_length=100, default='John')
    city_of_origin = models.CharField('City of origin', max_length=100, default='Doe')
    start_date = models.DateTimeField('Date of joining', auto_now_add=True)
    userpic = models.ImageField('Userpic', upload_to='media/img', default='media/img/undefined_monk.jpg')    

    title = models.CharField(
        'Title of address',
        max_length=30,
        choices=TITLE_CHOICES,
        default='Brother',
    )
    
    about = models.TextField('Your confession', max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_literate = models.BooleanField('Litteratus', default=False)
    is_ordained = models.BooleanField('Ordinatus', default=False)    

    objects = CustomAccountManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['first_name', 'city_of_origin']    

    def __str__(self):
        return self.user_name

    def full_address(self):
        return f'{self.title} {self.first_name} of {self.city_of_origin}'