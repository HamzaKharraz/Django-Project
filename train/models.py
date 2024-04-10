from django.db import models

# Create your models here.

class Train(models.Model) :
    trainID = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 20)
    content = models.CharField(max_length = 20)
    release = models.CharField(max_length = 4)
    cover = models.CharField(max_length = 50)
    producer = models.CharField(max_length = 30)
