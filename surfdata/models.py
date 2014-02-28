from django.db import models

# Create your models here.
class wind_data(models.Model):
	date = models.DateTimeField('date')
	wind_dir = models.IntegerField(null=True)
	wind_speed = models.FloatField(null = True)
	def __unicode__(self):
		return unicode(self.date)

class wave_data(models.Model):
	date = models.DateTimeField('date')
	wave_height = models.FloatField(null= True)
	wave_per = models.FloatField(null = True)
	wave_dir = models.IntegerField(null = True)
	#tide?

	def __unicode__(self):
		return unicode(self.date)

class video_data(models.Model):
	date = models.DateTimeField('date')
	title = models.CharField(max_length = 300)
	youtube_key = models.CharField(max_length =300)

	def __unicode__(self):
		return unicode(self.date)