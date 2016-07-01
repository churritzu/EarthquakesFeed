import sys
from misc import Globales

class HelpView:
	def __init__(self):
		print(Globales.title())
		print("Usage: earthFeed [Options(s)]\n")
		print("\t-h, --help\tGet this help list")
		print("")
		sys.exit()

	@staticmethod
	def need_help(opts):
		for opt, val in opts:
			if opt == "-h" or opt == "--help":
				return True

if __name__ == "__main__":
	pass