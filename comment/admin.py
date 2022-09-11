from django.contrib import admin

from comment.models import comment
# Register your models here.
class commentAdmin(admin.ModelAdmin):
    list_display=('cmnt_name','cmnt_email','cmnt_details','cmnt_type','cmnt_post','cmnt_status');
admin.site.register(comment,commentAdmin);