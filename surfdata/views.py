from django.shortcuts import render

from surfdata.models import wind_data, wave_data,video_data
import datetime
# Create your views here.
def index(request):


	p = wind_data.objects.order_by('-date')
	r = wave_data.objects.order_by('-date')
	current_wind_dir= p[0].wind_dir
	current_wind_speed = p[0].wind_speed
	date = p[0].date
	current_wave_height = r[0].wave_height
	current_wave_per = r[0].wave_per
	current_wave_dir = r[0].wave_dir 

	#if win_dir or win_speed is none? go to next available current and pull from there
	q = wind_data.objects.filter(wind_dir = current_wind_dir, wind_speed = current_wind_speed)
	s = wave_data.objects.filter(wave_height = current_wave_height) #, wave_per = current_wave_per, )
	last_wind_date = q[1].date
	last_wave_date = s[1].date
	c = p[0:3]
	
	
	t = video_data.objects.order_by('date')
	youtube_key = t[0].youtube_key

	
	context = {'current_wind_speed':current_wind_speed,
				'current_wind_dir' : current_wind_dir, 
				'current_wave_height': current_wave_height,
				'current_wave_per': current_wave_per,
				'current_wave_dir': current_wave_dir,
				'date': date,
				'last_wind_date':last_wind_date,
				'last_wave_date':last_wave_date,
				'wind_data': wind_data,
				'q': q,
				'youtube_key': youtube_key,
				'c': c,



	}
	
	return render(request, 'surfdata/index.html',context)

def test(request):

	p = wind_data.objects.order_by('-date')
	r = wave_data.objects.order_by('-date')
	current_wind_dir= p[0].wind_dir
	current_wind_speed = p[0].wind_speed
	date = p[0].date
	current_wave_height = r[0].wave_height
	current_wave_per = r[0].wave_per
	current_wave_dir = r[0].wave_dir 
	c = p[0:3]


	#use range instead of exact?
	#if win_dir or win_speed is none? go to next available current and pull from there
	q = wind_data.objects.filter(wind_dir__range = (current_wind_dir -10, current_wind_dir +10), wind_speed__range = (current_wind_speed -2, current_wind_speed +2))
	q_length = len(q)
	c= []
	for b in xrange(q_length):
		c.append(wave_data.objects.get(date = q[b].date))

	d = len(c) == q_length

	c = c[0:16]

	s = wave_data.objects.filter(wave_height__range = (current_wave_height - .5, current_wave_height +.5), wave_dir__range = (current_wave_dir -20,current_wave_dir + 28)) #, wave_per = current_wave_per, )
	last_wind_date = q[1].date
	last_wind_dir = q[1].wind_dir
	last_wave_date = s[1].date
	last_wave_height = s[1].wave_height
	last_wave_per = s[1].wave_per
	last_wave_dir = s[1].wave_dir
	last_wind_speed = q[1].wind_speed
	
	t = video_data.objects.order_by('-date')
	youtube_key = t[0].youtube_key
	youtube_title = t[0].title
	youtube_date = t[0].date

	
	context = {'current_wind_speed':current_wind_speed,
				'current_wind_dir' : current_wind_dir, 
				'current_wave_height': current_wave_height,
				'current_wave_per': current_wave_per,
				'current_wave_dir': current_wave_dir,
				'date': date,
				'last_wind_date':last_wind_date,
				'last_wave_date':last_wave_date,
				'last_wave_height': last_wave_height,
				'last_wave_dir':last_wave_dir,
				'last_wave_per':last_wave_per,
				'wind_data': wind_data,
				'q': q,
				'youtube_key': youtube_key,
				'last_wind_dir': last_wind_dir,
				'last_wind_speed' : last_wind_speed,
				'c': c,
				'youtube_title':youtube_title,
				'youtube_date':youtube_date,
				'd':d,
				'n' : xrange(q_length) ,



	}
	
	return render(request, 'surfdata/test.html',context)