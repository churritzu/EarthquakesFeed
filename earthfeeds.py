#!/usr/bin/env python3
import getopt
import sys
from misc import Globales
from vistas.Earthquakes import EarthquakesView
from vistas.Help import HelpView

class Main:
	def __init__(self, argv):
		if argv:
			try:
				optsStr = "h"
				opstList = ["help", "search=", "magnitude=", "wait=", "latitud=", "longitud=", "north=", "south=", "east=", "west="]
				opts, args = getopt.getopt(argv, optsStr, opstList)
				self.put_view(opts)
			except getopt.GetoptError: self.put_view([("--help","")])
		else: self.put_view()

	def put_view(self, opts=None):
		if HelpView.need_help(opts): HelpView()
		else: EarthquakesView(opts)

if __name__ == "__main__":
	Globales.clean_screen()
	Main(sys.argv[1:])