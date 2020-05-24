from django.contrib import admin
from .models import Blog,Comments
# Register your models here.

class blog_admin(admin.ModelAdmin):
    blog_admin =('username','date','subject')

admin.site.register(Blog,blog_admin)
admin.site.register(Comments)