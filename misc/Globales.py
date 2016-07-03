import os

__appName__ = "Earthquakes Feed"
__url__ = "https://github.com/churritzu/EarthquakesFeed"
__version__ = "0.2.0"
__author__ = "Churritzu <churritzu@yahoo.com>"

def title():
	return __appName__+" "+__version__+" ("+__url__+")"

def clean_screen():
	os.system('cls' if os.name == 'nt' else 'clear')