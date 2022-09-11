from django.contrib import admin
from post.models import post
# Register your models here.
class postAdmin(admin.ModelAdmin):
    list_display=("p_title","p_image","p_desc","p_category","p_author","p_date","p_comment","p_Like","p_status");
admin.site.register(post,postAdmin);