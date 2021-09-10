from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
import uuid
# Create your models here.
class Busdetails(models.Model):
   bus_number=models.CharField(max_length=100,primary_key=True)
   bus_route=models.CharField(max_length=100,default=0)
   Amount=models.CharField(max_length=10,default=3000)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('The given student username must be set')
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)

    
class User(AbstractBaseUser,PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.CharField(max_length=250, unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    user_phone=models.CharField(max_length=10,unique=True)
    Parent_Phone=models.CharField(max_length=10,unique=True)
    email=models.EmailField()
    Address_line=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Branch=models.CharField(max_length=100)
    password = models.CharField(max_length=250)
    is_active = models.BooleanField(('active'), default=True)
    is_superuser = models.BooleanField(('active'),default=False)
    is_staff = models.BooleanField(('active'),default=False)
    is_feepaid = models.BooleanField(('active'),default=False)
    Pincode=models.TextField()

    objects = UserManager()
    REQUIRED_FIELDS = [ ]
    USERNAME_FIELD = 'username'

class Conductor(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)   
    phone=models.CharField(max_length=10)
    age=models.CharField(max_length=20)
    bus_number=models.ForeignKey(Busdetails,on_delete=models.CASCADE)


class UserBusmapping(models.Model):
    bus_number = models.ForeignKey(Busdetails,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)



class Driver(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)   
    phone=models.CharField(max_length=10)
    age=models.CharField(max_length=20)
    bus_number=models.ForeignKey(Busdetails,on_delete=models.CASCADE)


class Payment(models.Model):
    bus_number = models.ForeignKey(Busdetails,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE) 
    year = models.IntegerField()
    due_amount=models.CharField(max_length=10)




