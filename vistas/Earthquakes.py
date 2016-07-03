import datetime
import sys
import time
from misc import Globales
from vistas.datos.RealTimeUSGS import RealTimeUSGS

class EarthquakesView:
	tiempoDeEspera = 300  # Default is 5 min. because the usgs reload the data in that time
	dateTimeFormat = "%d %B %Y %H:%M:%S"

	def __init__(self,opts=None):
		self.poner_opciones(opts)
		while True:
			Globales.clean_screen() #Limpia la ventana
			print(Globales.title()) #imprime el titulo principal
			print("Revision "+ str(datetime.datetime.now().strftime(self.dateTimeFormat)) + "\n")

			data = RealTimeUSGS().filtered_data(opts)
			if data: self.printData(data)
			else:
				print("No se encontraron resultados en tu busqueda. para salir presiona ctrl+c\n")
			print("Para salir presiona ctrl+c\n")

			#Pone el sistema a dormir durante el tiempo de espera
			try: time.sleep(self.tiempoDeEspera)
			except:
				print("Suerte, nos vemos pronto...\n")
				sys.exit()

	def poner_opciones(self, opts):
		if opts:
			for opt, val in opts:
				if opt == "--wait" and int(val) > 0:
					self.tiempoDeEspera=self.minutes_to_seconds(int(val))

	def minutes_to_seconds(self, min): return 60*min

	def printData(self, data):
		for temblor in data:
			print("Place: " + str(temblor["place"]))
			print("Magnitude: " + str(temblor["mag"]))
			print("Type: " + str(temblor["type"]))
			dt = datetime.datetime.fromtimestamp((temblor["time"] / 1000))
			print("Daytime: " + str(dt.strftime(self.dateTimeFormat)))
			print("Alert Type: " + str(temblor["alert"]) + "\n")
			print("-|-|-|-|-|-|-|-|" * 3)
			print("")

if __name__ == "__main__":
	pass