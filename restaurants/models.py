from django.db import models

# Create your models here.

class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time= models.TimeField()
	logo = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name
	class Meta:
		ordering = ["-name"]

