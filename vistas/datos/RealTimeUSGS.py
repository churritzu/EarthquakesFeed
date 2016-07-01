import sys
import urllib.request

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

	def get_data(self):
		#TODO: Revisar que pasa si no hay conexion a la web
		try:
			rtdata = urllib.request.urlopen(self.url)
		except:
			print("Se encontró un problema al intentar conseguir la información, favor de intentarlo mas tarde.\n")
			sys.exit()

		return rtdata.read().decode("utf-8")