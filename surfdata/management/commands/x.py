from django.core.management.base import BaseCommand, CommandError
from surfdata.models import wind_data, wave_data
import urllib
from django.utils import timezone
import datetime
from django.utils.timezone import utc

# To do- close files. Add precautions if

"""class reader(object):
	#reads data from .txt file into parameters , and saves to db
	#todo - stop hardcoding url in
	print "error"
	file2 = urllib.urlretrieve('http://www.ndbc.noaa.gov/data/realtime2/ICAC1.txt','textfile.txt')
	file = open('textfile.txt', 'r')
	headings = file.readline()
	parameters = file.readline()
	
	while True:
		data = file.readline()
		if not data: break

		data = data.split()
		date =  datetime.datetime(year = int(data[0]), month = int(data[1]), day = int(data[2]), hour = int(data[3]), minute = int(data[4]) ).replace(tzinfo=utc)	
		
		if (data[5]=='MM' ):
			data[5] = None
		if (data[6] =='MM'):
			data[6] = None											
		x = wind_data(date = date, wind_dir = data[5], wind_speed = data[6])
		x.save()
		print x
		"""

class reader2(object):
	#reads data from .txt file into parameters , and saves to db
	#todo - stop hardcoding url in
	file2 = urllib.urlretrieve('http://www.ndbc.noaa.gov/data/5day2/42012_5day.txt','textfile2.txt')
	file = open('textfile2.txt', 'r')
	headings = file.readline()
	parameters = file.readline()
	print "hello"
	
	while True:
		data = file.readline()
		if not data: break

		data = data.split()
		date =  datetime.datetime(year = int(data[0]), month = int(data[1]), day = int(data[2]), hour = int(data[3]), minute = int(data[4]) ).replace(tzinfo=utc)	
		#why can i save this as a string if model calls for integer
		if (data[8]=='MM' ):
			data[8] = None
		if (data[9] =='MM'):
			data[9] = None	
		if (data[10] =='MM'):
			data[10] = None	
		if (data[11] =='MM'):
			data[11] = None	

		if (data[5]=='MM' ):
			data[5] = None
		if (data[6] =='MM'):
			data[6] = None											
		y = wind_data(date = date, wind_dir = data[5], wind_speed = data[6])
		y.save()																																																								
		#Model.objects.get_or_create(field="")
		x = wave_data(date = date, wave_height = data[8], wave_per = data[10], wave_dir= data[11])
		x.save()
		

		print x.wave_per

		
	
class Command(BaseCommand):
    
    help = 'Help text goes here'

    def handle(self, **options):
    	print "start"
		
print len(wind_data.objects.all())