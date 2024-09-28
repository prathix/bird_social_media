from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 40)
    Description = models.CharField(max_length = 400)
    image = models.ImageField(upload_to='app/images/')