from django.db import models

# Create your models here.
class comment(models.Model):
    cmnt_name=models.CharField(max_length=255)
    cmnt_email=models.EmailField()
    cmnt_details=models.TextField()
    cmnt_type=models.IntegerField()
    cmnt_post=models.IntegerField()
    cmnt_status=models.IntegerField()