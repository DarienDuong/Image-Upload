from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topics(models.Model):
	name = models.CharField(max_length=500)
	topic_id = models.IntegerField()

	def __str__(self):
		return self.name

class Images(models.Model):
	name = models.CharField(max_length=500)
	topic = models.ForeignKey(Topics, on_delete=models.CASCADE, related_name='image')
	image = models.ImageField(upload_to='topic_images/', blank=False)

	def __str__(self):
		return self.name