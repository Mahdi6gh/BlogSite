from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text  import slugify
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Father_name=models.CharField(max_length=50)
    nationall_code=models.CharField(max_length=10)
    pfp=models.ImageField(upload_to='images/pfp')
    def __str__(self):
        return self.user.username
class category(models.Model):
    name=models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name
class blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(category)
    content = models.TextField()
    description = models.TextField(editable=True,blank=True ,help_text="its gonna be auto full")
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="images/blogs")
    views = models.IntegerField(default=0)
    slug=models.SlugField(null=True,unique=True,blank=True)
    class Meta:
        ordering=['-created_at']

    def save(self,*args,**kwargs):
        self.slug= slugify(self.title)
        if self.content and not self.description:
            words=self.content.split()
            self.description=self.content[:150]+"..."
        super().save(*args, **kwargs)
    def url(self):
        return reverse('blog_with_id',args=[self.slug])

    def __str__(self):
        return self.title