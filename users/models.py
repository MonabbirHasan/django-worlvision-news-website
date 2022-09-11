from re import M
from django.db import models

# Create your models here.
class users(models.Model):
    u_name=models.CharField(max_length=255)
    u_image=models.FileField(upload_to="u_img/",max_length=255,null=True,default=None);
    u_email=models.EmailField()
    u_phone=models.CharField(max_length=12)
    u_biodata=models.TextField()
    u_address=models.CharField(max_length=255)
    u_type=models.IntegerField()
    u_post=models.IntegerField()
    u_status=models.IntegerField()