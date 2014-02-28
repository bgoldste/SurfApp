
from django.core.management.base import BaseCommand, CommandError
from surfdata.models import wind_data, wave_data, video_data
import urllib
from django.utils import timezone
import datetime
from django.utils.timezone import utc

import subprocess
import re
import urllib
import os
import shlex
import datetime
import shutil


"""youtube keys that work 9MDiCuvhg1Y Wvjce8BUHjg xh3i78r7pAI"""
keys = ['xh3i78r7pAI'. 'Wvjce8BUHjg', '9MDiCuvhg1Y']



def title_creator(day, month, year):

	title = "New_surf_vid_%d_%d_%d" % (month, day, year)
	video_name = '%s.mp4' % title
	return title, video_name


def url_creator(day, month, year):
	if day > 9:
		if month > 9:
			url = 'http://s3.amazonaws.com/live-cam-archive/elportocam/elportocam.%d.%d-%d-%d.mp4' % (time, year, month, day)
		else:
			url = 'http://s3.amazonaws.com/live-cam-archive/elportocam/elportocam.%d.%d-0%d-%d.mp4' % (time, year, month, day)
	else :
		if month > 9:
			url = 'http://s3.amazonaws.com/live-cam-archive/elportocam/elportocam.%d.%d-%d-0%d.mp4' % (time, year, month, day)
		else:	
			url = 'http://s3.amazonaws.com/live-cam-archive/elportocam/elportocam.%d.%d-0%d-0%d.mp4' % (time, year, month, day)
	
	return url

def download(url, video_name):
	print 'starting download now'
	urllib.urlretrieve(url, video_name)
	print 'download complete'

def upload(title, video_name):
	input1 = 'python youtube_upload.py --email=surfappio@gmail.com --password=chicken99 --title="%s" --description="surf as seen at %s "  --category=Music --keywords=surf %s' % (title, title, video_name)
	args = shlex.split(input1)
	p = subprocess.Popen(args, stdout=subprocess.PIPE)
	out, err = p.communicate()
	print 'upload complete, commencing deleting local file'
	#delete file after succesful upload
	#os.remove(video_name)
	print 'deletion complete'
	print out.split("=")[1]
	return out.split("=")[1]



date = datetime.date.today()
print date
day = datetime.datetime.now().day 
month = datetime.datetime.now().month
year = datetime.datetime.now().year
time = 1100
#add a time var and feed it to url_Creator

title, video_name= title_creator(day, month, year)
url = url_creator(day, month, year)

print 'vid name =',video_name
#for x in xrange(0,22):


#download(url, video_name)
#youtube_key = upload(title, video_name)
youtbe_key =
print 'youtube key = ' , youtube_key


x = video_data(date = (year+'-'+ month+ '-' +day) , title = title, youtube_key = youtube_key)
x.save()

class Command(BaseCommand):
    
    help = 'Help text goes here'

    def handle(self, **options):
    	print "start"

