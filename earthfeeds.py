import getopt
import sys
from misc import Globales
from vistas.Earthquakes import EarthquakesView
from vistas.Help import HelpView

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