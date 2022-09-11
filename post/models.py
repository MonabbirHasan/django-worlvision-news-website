from operator import mod
from pyexpat import model
from re import T
from django.db import models

# Create your models here.
class post(models.Model):
    p_title=models.CharField(max_length=255);
    p_image=models.FileField(upload_to="p_image/",max_length=255,null=True,default=None);
    p_desc=models.TextField();
    p_category=models.IntegerField();
    p_author=models.IntegerField();
    p_date=models.DateField();
    p_comment=models.IntegerField();
    p_Like=models.IntegerField();
    p_status=models.IntegerField();