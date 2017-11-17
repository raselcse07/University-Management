from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser)
from django.core.validators import RegexValidator
from django.conf import settings
from django.db.models.signals import post_save






USERNAME_REGEX="^[a-zA-Z0-9.@+-_]*$"



class MyUserManager(BaseUserManager):

    def create_user(self, username,email,reg_number,password=None):
        
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            reg_number=reg_number

        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email,reg_number,password):
       
        user = self.create_user(
            username,
            email,
            reg_number=reg_number,
            password=password,
        )

        user.is_admin = True
        user.is_staff=True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):

    username        =models.CharField(max_length=250,
                              validators=[
                                RegexValidator(
                                    regex=USERNAME_REGEX,
                                    message='Username must be Alphanumeric and contain any of the following : ". @ + - _ "',
                                    code='invalid username'

                                )
                            ],
                              unique=True
                        )
    email           = models.EmailField(
                            verbose_name='email address',
                            max_length=255,
                        )

    reg_number      =models.CharField(max_length=250,unique=True)

    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','reg_number']

    def get_full_name(self):
       
        return self.email

    def get_short_name(self):
       
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
      
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
      
        return True



class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    city = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)



def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):

    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)