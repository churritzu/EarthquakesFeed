import sys
import getopt
from vistas.Help import HelpView
from vistas.Earthquakes import EarthquakesView
# import urllib.request
# import json
# import time
# import datetime

class Main:
	def __init__(self, argv):
		if len(argv):
			try:
				opts, args = getopt.getopt(argv,"h", ["help"])
				self.put_view(opts)
			except getopt.GetoptError: HelpView()
		else: HelpView()

	def put_view(self, argv):
		if HelpView.need_help(argv): HelpView()
		else: EarthquakesView()

if __name__ == "__main__":
	Main(sys.argv[1:])