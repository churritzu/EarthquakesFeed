import sys
import urllib.request
import json
import datetime

class RealTimeUSGS:
	'''
		PRODUCTION URL OF USGS
		http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson
		TEST URL RETURN 404
		http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojsonASADFASDF
		TEST URL RETURN EXCEPT
		http://www.churritzu.com/holaMundo
	'''
	url = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
	magnitud = 2.0
	tiempoDeEspera = 60 * 5; #Default is 5 min. because the usgs reload the data in that time
	current_latitud = 32.62453889999999
	current_longitud = -115.45226230000003
	maxLat = 160000
	minLat = 85000
	maxLong = 530000
	minLong = 280000

	def get_json_data(self):
		#TODO: Revisar que pasa si no hay conexion a la web
		try:
			urlData = urllib.request.urlopen(self.url)
		except:
			print("Se encontró un problema al intentar conseguir la información, favor de intentarlo mas tarde.\n")
			sys.exit()
		return urlData.read().decode("utf-8")

	def get_full_data(self):
		data = self.get_json_data()
		try:
			decoder = json.loads(data)
			return decoder
		except json.JSONDecodeError as e:
			return False

	def get_data(self):
		full_data = self.get_full_data()
		try:
			features = full_data["features"]
		except:
			print("No se encontraron datos disponibles\n")
			exit()
		return features

	def filtered_data(self):
		data = self.get_data()

		for gemeotria in data:
			longitud = float(gemeotria["geometry"]["coordinates"][0])
			latitud = float(gemeotria["geometry"]["coordinates"][1])
			if self.inLatitud(latitud) and self.inLongitud(longitud) and gemeotria["properties"]["mag"] >= self.magnitud:
				print("Lugar: " + str(gemeotria["properties"]["place"]))
				print("Magnitud: " + str(gemeotria["properties"]["mag"]))
				print("Tipo: " + str(gemeotria["properties"]["type"]))
				dt = datetime.datetime.fromtimestamp((gemeotria["properties"]["time"] / 1000))
				print("Dia: " + str(dt))
				print("Alerta: " + str(gemeotria["properties"]["alert"]))
				print("Url: " + str(gemeotria["properties"]["detail"]))
				print("")

	def inLatitud(self, latitud):
		if latitud <= self.get_max_latitud() and latitud > self.get_min_latitud():
			return True
		return False

	def inLongitud(self, longitud):
		if longitud < self.get_max_longitud() and longitud > self.get_min_longitud():
			return True
		return False

	def get_max_latitud(self):
		return self.current_latitud + (self.maxLat/111319)

	def get_min_latitud(self):
		return self.current_latitud - (self.minLat / 111319)

	def get_max_longitud(self):
		return self.current_longitud + (self.maxLong / 111131)

	def get_min_longitud(self):
		return self.current_longitud - (self.minLong / 111131)