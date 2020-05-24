from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    username = models.ForeignKey(User,to_field="username",on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=15)
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='static/')
    likes = models.IntegerField(default=0)


    def __str__(self):
        return str(self.id)
    

class Category(models.Model):
    category_type = models.CharField(max_length=15)
    total_number = models.IntegerField()

class Comments(models.Model):
    username = models.ForeignKey(User,to_field="username",on_delete=models.CASCADE)
    blog_id = models.ForeignKey(Blog,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()