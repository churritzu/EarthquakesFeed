import sys
import urllib.request
import json

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
			return features
		except:
			print("No se encontraron datos disponibles\n")
			exit()

	def get_raw_data(self):
		data = self.get_data()
		toReturn = list()
		for temblor in data:
			toReturn.append(temblor["properties"])
		return toReturn

	def filtered_data(self, opts):
		data = self.get_data()
		toReturn = list()
		for temblor in data:
			if(opts["tipo"]=="all" and temblor["properties"]["mag"]>=opts["magnitud"]):
				toReturn.append(temblor["properties"])
			else:
				longitud = float(temblor["geometry"]["coordinates"][0])
				latitud = float(temblor["geometry"]["coordinates"][1])
				if self.inLatitud(latitud, opts["latitud"], opts["maxLat"], opts["minLat"]) and \
					 self.inLongitud(longitud, opts["longitud"], opts["maxLong"], opts["minLong"]) and \
					 temblor["properties"]["mag"] >= opts["magnitud"]:
					toReturn.append(temblor["properties"])
		return toReturn

	def inLatitud(self, latitud, current, max, min):
		if latitud <= self.get_max_latitud(current, max) and latitud > self.get_min_latitud(current, min):
			return True
		return False

	def inLongitud(self, longitud, current, max, min):
		if longitud < self.get_max_longitud(current, max) and longitud > self.get_min_longitud(current, min):
			return True
		return False

	def get_max_latitud(self, latitud, max):
		return latitud + (max/111.12)

	def get_min_latitud(self, latitud, min):
		return latitud - (min / 111.12)

	def get_max_longitud(self, longitud, max):
		return longitud + (max / 111.32)

	def get_min_longitud(self, longitud, min):
		return longitud - (min / 111.32)