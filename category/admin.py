from django.contrib import admin
from category.models import category
# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display=('c_name','c_image','c_date','is_sub','c_status')
admin.site.register(category,categoryAdmin);
