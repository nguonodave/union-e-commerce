from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager # necessary for modifying the users and account models

# creating model for users
class MyAccountManager(BaseUserManager):
    # creating a normal user
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            email = self.normalize_email(email), # normalize_email changes email input from uppercase to lowercase
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # creating a superuser
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user( # the create_user() method takes all the information from the created normal user
            email=self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        # after getting the information from the normal user using the create_user() method, we add the following to make the user a superuser
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

# overiding the user model(creating custom user model)
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    # required since we have overrided the user model
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' # using email for admin login instead of the username
    REQUIRED_FIELDS =  ['username', 'first_name', 'last_name']

    # using MyAccountManager for all the operations
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    # this means that if user is admin the s/he has all the permissins in the admin dashboard
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
