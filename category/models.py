from operator import mod
from django.db import models

# Create your models here.
class category(models.Model):
    c_name=models.CharField(max_length=255);
    c_image=models.FileField(upload_to="c_img/",max_length=255,null=True,default=None);
    c_date=models.DateField();
    is_sub=models.IntegerField();
    c_status=models.IntegerField();