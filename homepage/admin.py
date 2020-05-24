from django.contrib import admin
from .models import CompanyData
# Register your models here.

class company_info(admin.ModelAdmin):
    company_info = ('name','intro','about','news')
admin.site.register(CompanyData,company_info)