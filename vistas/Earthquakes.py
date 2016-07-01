import Globales
import time
from vistas.datos.RealTimeUSGS import RealTimeUSGS

class EarthquakesView:
	def __init__(self):
		print(Globales.title()+"\n")
		#print(RealTimeUSGS().get_data())
		RealTimeUSGS().filtered_data()

if __name__ == "__main__":
	pass