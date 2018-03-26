from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Scan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    datestamp = models.DateTimeField()
   
