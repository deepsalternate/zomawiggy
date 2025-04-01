from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.




class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")


        user=self.model(
            email=self.normalize_email(email),  #normalize_email is a method that comes with BaseUserManager
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)#set_password is a method that hashes the password to save into the database.and is a method of abstractbaseuser
        user.save(using=self._db) #using=self._db is used to save the user in the database
        return user
    
    def create_superuser(self,first_name,last_name,username,email,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    RESTURANT=1
    CUSTOMER=2
    ROLE_CHOICES=(
        (RESTURANT,'Resturant Owner'),
        (CUSTOMER,'Customer'),
    )
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.CharField(max_length=100,blank=True)
    role=models.PositiveSmallIntegerField(choices=ROLE_CHOICES,blank=True,null=True)
    
    #required fields for django
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    objects=UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
    


class userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to='users/profile_pictures',blank=True,null=True)
    cover_picture=models.ImageField(upload_to='users/cover_pictures',blank=True,null=True)
    address_line_1=models.CharField(max_length=100 ,blank=True ,null=True)
    address_line_2=models.CharField(max_length=100 ,blank=True ,null=True)
    city=models.CharField(max_length=100 ,blank=True ,null=True)
    state=models.CharField(max_length=100 ,blank=True ,null=True)
    country=models.CharField(max_length=100 ,blank=True ,null=True)
    pincode=models.CharField(max_length=10 ,blank=True ,null=True)
    latitude=models.FloatField(blank=True ,null=True)
    longitude=models.FloatField(blank=True ,null=True)
    phone=models.CharField(max_length=100 ,blank=True ,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.email


