import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class AccountManager(UserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError("Users must have a username")
        
        if not password:
            raise ValueError("Users must have password")

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # -----------------------------------------
    phone_number = models.CharField(max_length=20, unique=True, verbose_name="تلفن")
    # -----------------------------------------
    national_code   = models.CharField(max_length=15, null=True, blank=True, verbose_name="کد ملی")
    # -----------------------------------------
    address = models.CharField(max_length=400, null=True, blank=True, verbose_name="آدرس")
    # -----------------------------------------

    
    objects = AccountManager()
    
    # -----------------------------------------
    
    REQUIRED_FIELDS = ["phone_number","email"]
    # -----------------------------------------