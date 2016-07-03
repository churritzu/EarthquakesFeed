import sys
from misc import Globales

class HelpView:
	def __init__(self):
		print(Globales.title())
		print("Usage: earthFeed [Options(s)]\n")
		print("\t-h, --help\t\tGet this help list")
		print("\t--search=(all|local)\tThe type of search can be all or local (default=all)")
		print("\t--magnitude=(2.0)\tThe min magnitude of the earthquake (default=2.0)")
		print("\t--wait=(5)\t\tIs the time it takes to update the data in minutes (default=5)")
		print("")
		sys.exit()

	@staticmethod
	def need_help(opts):
		if opts:
			for opt, val in opts:
				if opt == "-h" or opt == "--help": return True

if __name__ == "__main__": pass