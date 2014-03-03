from django.core.management.base import BaseCommand, CommandError
from surfdata.models import ReportData
import urllib
from django.utils import timezone
import datetime
from django.utils.timezone import utc



class reader2(object):
	#reads data from .txt file into parameters , and saves to db
	#todo - stop hardcoding url in
	file2 = urllib.urlretrieve('http://www.ndbc.noaa.gov/data/5day2/42012_5day.txt','textfile2.txt')
	file = open('textfile2.txt', 'r')
	#read first 2 lines -- data does not start until ln3
	headings = file.readline()
	parameters = file.readline()
	objects_added = 0
	
	while True:
		#why does this work
		#reads 1 line, while there are lines to read
		data = file.readline()
		if not data: break

		#convert string into list
		data = data.split()

		#iterate through list and turn any missing values of MM into None 
		for d  in range(len(data)):
			if data[d] == 'MM':
				data[d] = None
		#convert to datetime object
		date1 =  datetime.datetime(year = int(data[0]), month = int(data[1]), day = int(data[2]), hour = int(data[3]), minute = int(data[4]) ).replace(tzinfo=utc)	
		#why can i save this as a string if model calls for integer

		#only write new date if doesn't aready exist
		if ReportData.objects.filter(date = date1):
			print "Object already exists for this date"
		#YY0  MM DD hh mm WDIR WSPD GST  WVHT   DPD   APD MWD   PRES  ATMP  WTMP  DEWP  VIS PTDY  TIDE
		else:			
			y = ReportData(date = date1, WDIR = data[5], WSPD = data[6], WVHT = data[8], DPD = data[9], APD = data[10], MWD = data[11], ATMP = data[12], WTMP = data[13], TIDE = data[18])
			y.save()	
			print "Object added:", y.date, y.WDIR, y.WSPD	
			objects_added += 1																																																				
	
	file.close()
	print ("%d objects added to database" % objects_added)
   
		
	
class Command(BaseCommand):
    
    help = 'Read in most recent data from noaa site, and add to database.'

    def handle(self, **options):
    	print "Custom Command Run Succesfully. Booyah!"
		
