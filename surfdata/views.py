from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from surfdata.models import ReportData
# Create your views here.
def index(request):
	some_objects = ReportData.objects.order_by('-date')[0:4]
	today = some_objects[0].date.day
	some_other_objects = ReportData.objects.order_by('-date').exclude(date__day = today)
	total_objects = len(ReportData.objects.all())


	# write functions to do custom queries, including changing degrees to account for negative
	similar_conditions = ReportData.objects.filter(WDIR__range = (some_objects[0].WDIR - 30, some_objects[0].WDIR + 30)).exclude(date__day = today).order_by('-date')

	
	context = {'some_objects':some_objects,
				'some_other_objects': some_other_objects,
				'total_objects' : total_objects,
				'today' : today,
				'similar_conditions' : similar_conditions,
	}
	
	return render(request, 'surfdata/index.html',context)

def search(request):
	if 'q' in request.GET and request.GET['q'] and 'search_parameter' in request.GET and request.GET['search_parameter']:
		q = request.GET['q']
		search_parameter = request.GET['search_parameter']
		if search_parameter == 'WDIR':
			objects = ReportData.objects.filter(WDIR = q).order_by('-date')
		if search_parameter == 'WSPD':
			objects = ReportData.objects.filter(WSPD = q).order_by('-date')
		if search_parameter == 'WVHT':
			objects = ReportData.objects.filter(WVHT= q).order_by('-date')
		if search_parameter == 'MWD':
			objects = ReportData.objects.filter(MWD = q).order_by('-date')
		return render(request, 'surfdata/search_results.html', { 'objects':objects, 'search_parameter' : search_parameter})
		
	else:
		message = 'You submitted an empty form. DOG is u trippin?'
		return HttpResponse(message)

def test(request):

	

	
	context = {"""'current_wind_speed':current_wind_speed,
				'current_wind_dir' : current_wind_dir, """
				



	}
	
	return render(request, 'surfdata/test.html',context)