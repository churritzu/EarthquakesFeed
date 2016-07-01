import os
import sys
import getopt
import Globales
from vistas.Help import HelpView
from vistas.Earthquakes import EarthquakesView

class Main:
	def __init__(self, argv):
		if len(argv):
			try:
				opts, args = getopt.getopt(argv,"h", ["help"])
				self.put_view(opts)
			except getopt.GetoptError: HelpView()
		else: EarthquakesView()

	def put_view(self, argv):
		if HelpView.need_help(argv): HelpView()
		else: EarthquakesView()

if __name__ == "__main__":
	Globales.clean_screen()
	Main(sys.argv[1:])