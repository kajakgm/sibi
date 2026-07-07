from django.db import models

# Create your models here.
class datas(models.Model):
    pid=models.CharField(max_length=30)
    pname=models.CharField()
    pimg=models.ImageField(upload_to='images/',blank=True,null=True)
    files=models.FileField(upload_to='files/',blank=True,null=True)
