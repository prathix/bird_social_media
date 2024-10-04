from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 40)
    description = models.CharField(max_length = 400)
    image = models.ImageField(upload_to='app/static/app/images/')

class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)