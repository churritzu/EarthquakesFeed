import datetime
import sys
import time
from misc import Globales
from vistas.datos.RealTimeUSGS import RealTimeUSGS

class EarthquakesView:
	tiempoDeEspera = 60*5  # Default is 5 min. because the usgs reload the data in that time
	dateTimeFormat = "%d %B %Y %H:%M:%S"

	def __init__(self):
		while True:
			Globales.clean_screen() #Limpia la ventana
			print(Globales.title()) #imprime el titulo principal
			print("Revision "+ str(datetime.datetime.now().strftime(self.dateTimeFormat)) + "\n")

			data = RealTimeUSGS().filtered_data()
			if data: self.printData(data)
			else:
				print("No se encontraron resultados en tu busqueda. para salir presiona ctrl+c\n")
			print("Para salir presiona ctrl+c\n")

			#Pone el sistema a dormir durante el tiempo de espera
			try: time.sleep(self.tiempoDeEspera)
			except:
				print("Suerte, nos vemos pronto...")
				sys.exit()

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