import sys
import urllib.request
import json
import time
import datetime

#Templores significativos -> http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_hour.geojson

class Main:
    
    '''
        Regresa una json de parte del servidor
        @return <json>
    '''    
    def __init__(self):
        #self.urls = ["http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson"]
        self.urls = ["http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"]
        self.magnitud = 2.0
        self.tiempoDeEspera = 60*5;
        
        while True:
            print("REVISION: "+str(datetime.datetime.now()))
            url = urllib.request.urlopen(self.urls[0])
            if url.getcode() == 200: self.procesarInformacion(url.read().decode("utf-8"))
            print("-------------------------------------------------------------------")
            try:
                time.sleep(self.tiempoDeEspera)
            except:
                print("Adios....")
        
    def inLatitud(self, latitud):
        mxliLatitud = 32.62453889999999
        if latitud < 34.0522342 and latitud > 31.8667427:
            return True
        return False
    
    def inLongitud(self, longitud):
        mxliLongitud = -115.45226230000003
        if longitud < -112.84886310000002 and longitud > -120.2436849:
            return True
        return False
        
    def procesarInformacion(self, info):
        decoder = json.loads(info)
        try:
            features = decoder["features"]
            for gemeotria in features:               
                longitud = gemeotria["geometry"]["coordinates"][0];
                latitud = gemeotria["geometry"]["coordinates"][1]
                if self.inLatitud(latitud) and self.inLongitud(longitud) and gemeotria["properties"]["mag"] >= self.magnitud:
                    print("Lugar: "+str(gemeotria["properties"]["place"]))
                    print("Magnitud: "+str(gemeotria["properties"]["mag"]))
                    print("Tipo: "+str(gemeotria["properties"]["type"]))
                    dt = datetime.datetime.fromtimestamp((gemeotria["properties"]["time"]/1000))
                    print("Dia: "+str(dt))
                    print("Alerta: "+str(gemeotria["properties"]["alert"]))
                    print("Url: "+str(gemeotria["properties"]["detail"]))
                    print("")
                    print("")              
        except KeyError as e:
            print("Ups!!! No encontramos datos en el diccionario")
           
    
if __name__ == "__main__":
    total = len(sys.argv)
    cmdargs = str(sys.argv)
    print(total)
    print(cmdargs)
    
    #Main()