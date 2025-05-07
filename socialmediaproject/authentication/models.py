from django.db import models
from django.contrib.auth.hashers import make_password  # وارد کردن make_password
# Create your models here.

class authentication(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=150) 
    email = models.CharField(max_length=150, unique=True) 



    def save(self, *args, **kwargs):
        # اگر پسوورد تغییر کرده باشه، اون رو هش می‌کنیم
        if self.password:
            self.password = make_password(self.password)  # هش پسوورد
        super().save(*args, **kwargs)  # ذخیره مدل در دیتابیس  