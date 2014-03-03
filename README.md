SurfApp
=======

Hi! 

This is my first Django/Python piece of code. Comments and critiques much appreciated-
Still learning :)

Basic Structure of the app-
This app consists mostly of  a database of ReportData objects, which correspond to buoy data for a certain date and time 
everything is pulled from a buoy in San Fransisco, though most of the NBDC data is in the same format so this could be tweaked to add to different places.

The /surfdata page displays the most recent buoy information, as well as the recent days for which the Wind direction was identical. 
There is a basic search function, though it must take only numbers as input, and those must match the type of whatever is being searched for. Some objects are ints and others are floats- searching for the wrong one will throw an error.

The app reads data through two scripts, textupload.py and vidupload.py. Both of these are run through the command line with the django manaage.py script-
eg: python manage.py vidupload .

textupload scans a .txt file and adds all new data to the database.

vidupload downloads a video from a surfing site, uploads it to youtube, and saves the video information (including yoututbe key) for future lookup.
Note that vidupload is very finnicky and often fails due to internet connectivity problems.

Setup-

Run normal database setup, then run python manage.py textupload.
When you open the app with the runserver commmand, you should see some recent data displayed.
