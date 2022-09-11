from django.contrib import admin
from users.models import users
# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display=('u_name','u_image','u_email','u_phone','u_biodata','u_address','u_type','u_post','u_status');
admin.site.register(users,userAdmin);