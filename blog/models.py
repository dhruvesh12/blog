from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  null=True)
	name = models.CharField(max_length=200)
	content = models.TextField()
	img=models.ImageField(upload_to='', default='no-photo.png')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	view_count = models.IntegerField(default=0)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name

class comment(models.Model):
	com_name=models.ForeignKey(Post,on_delete=models.CASCADE,  null=True)
	comments=models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)

