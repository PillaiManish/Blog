from django.db import models

# Create your models here.
class CompanyData(models.Model):
    name = models.CharField(max_length=20)
    intro = models.TextField()
    about = models.TextField()
    news = models.TextField
    