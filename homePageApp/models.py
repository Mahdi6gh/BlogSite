from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name
class blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(category,on_delete=models.SET_NULL,null=True,blank=True)
    content = models.TextField()
    description = models.TextField(editable=True,blank=True ,help_text="its gonna be auto full")
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="images/blogs")
    views = models.IntegerField(default=0)
    def save(self,*args,**kwargs):
        if self.content and not self.description:
            words=self.content.split()
            self.description=self.content[:150]+"..."
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title