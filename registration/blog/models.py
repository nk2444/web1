
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug= models.SlugField()
    intro=models.TextField()
    body=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/',blank=True, null=True)

    class Meta:
       ordering=('-created_at',)

       
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name



