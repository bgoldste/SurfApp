from django.db import models

# TODOS - add location for buoy. 
#Account for negative numbers in range calculations, eg degrees: 10 degrees - 30 should be 340.


class ReportData(models.Model):
	
	
	date = models.DateTimeField('date', unique = True)

	#Wind speed and direction m/s, degrees clockwise from true N
	WDIR = models.IntegerField(null=True)
	WSPD = models.FloatField(null=True)

	#significant wave height (m), dominant period (s), average period (s), direction of dominant per (degrees) from N clockwise
	WVHT = models.FloatField(null=True)
	DPD  = models.IntegerField(null=True)
	APD = models.FloatField(null=True)
	MWD = models.IntegerField(null=True)
	
	#air and water temp
	ATMP = models.FloatField(null=True)
	WTMP =models.FloatField(null=True)

	#in ft
	TIDE = models.FloatField(null = True)

	def __unicode__(self):
		return unicode(self.date)





class video_data(models.Model):
	date = models.DateTimeField('date')
	title = models.CharField(max_length = 300)
	youtube_key = models.CharField(max_length =300)

	def __unicode__(self):
		return unicode(self.date)




