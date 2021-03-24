from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	#rate = models.IntegerField(default=0)
	def __str__(self):
		return f'{self.user}'


class Post(models.Model):
    title=models.CharField(max_length=200)
    auther = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
	    return self.title
    def save(self, *args, **kwargs):
	   
	    super(Post, self).save(*args, **kwargs)

