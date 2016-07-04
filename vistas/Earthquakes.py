import datetime
import sys
import time
from misc import Globales
from vistas.datos.RealTimeUSGS import RealTimeUSGS

class EarthquakesView:
	tiempoDeEspera = 300  # Default is 5 min. because the usgs reload the data in that time
	dateTimeFormat = "%d %B %Y %H:%M:%S"
	tipo_busqueda = "all"
	magnitud = 2
	current_latitud = 32.62453889999999
	current_longitud = -115.45226230000003
	maxLat = 200
	minLat = 200
	maxLong = 200
	minLong = 200

	def __init__(self,opts=None):
		self.poner_opciones(opts)
		while True:
			Globales.clean_screen() #Limpia la ventana
			print(Globales.title()) #imprime el titulo principal
			print("Revision "+ str(datetime.datetime.now().strftime(self.dateTimeFormat)) + "\n")

			data = RealTimeUSGS().filtered_data(self.tomar_opciones())
			if data: self.printData(data)
			else: print("No se encontraron resultados en tu busqueda.\n")

			#Pone el sistema a dormir durante el tiempo de espera
			try:
				print("Para salir presiona ctrl+c\n")
				time.sleep(self.tiempoDeEspera)
			except:
				print("Suerte, nos vemos pronto...\n")
				sys.exit()

	def poner_opciones(self, opts):
		if opts:
			for opt, val in opts:
				if opt == "--wait" and int(val) > 0:
					self.tiempoDeEspera=self.minutes_to_seconds(int(val))
				elif opt == "--magnitude" and float(val) >= 1:
					self.magnitud = float(val)
				elif opt == "--search":
					self.tipo_busqueda = val

	def tomar_opciones(self):
		opciones = dict()
		opciones["tipo"] = self.tipo_busqueda
		opciones["magnitud"] = self.magnitud
		opciones["latitud"] = self.current_latitud
		opciones["longitud"] = self.current_longitud
		opciones["maxLat"] = self.maxLat
		opciones["minLat"] = self.minLat
		opciones["maxLong"] = self.maxLong
		opciones["minLong"] = self.minLong
		return opciones

	def minutes_to_seconds(self, min): return 60*min

	def printData(self, data):
		for temblor in data:
			print("Place: " + str(temblor["place"]))
			print("Magnitude: " + str(temblor["mag"]))
			print("Type: " + str(temblor["type"]))
			dt = datetime.datetime.fromtimestamp((temblor["time"] / 1000))
			print("Daytime: " + str(dt.strftime(self.dateTimeFormat)))
			print("-|-|-|-|-|-|-|-|" * 3)
			print("")

if __name__ == "__main__":
	pass