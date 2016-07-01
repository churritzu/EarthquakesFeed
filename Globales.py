import os

appName = "Earthquakes Feed"
url = "http://www.churritzu.com"
version = "0.0.1"

def title():
	return appName+" "+version+" ("+url+")"

def clean_screen():
	os.system('cls' if os.name == 'nt' else 'clear')