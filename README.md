#Earthquakes Feed

This is an application to take all global and/or local ground motion with updated "real time data", still in development so feel free to comment or support

##How to use
For the moment is only in Command Interface for windows, mac and linux and it's necessary to have installed python 3.5 or above.
 
###Windows:
1.- if you are using the file explorer only doble clicked on the file earthfeed.py. (if a popup appear select the python option)

2.- if you are in the command prompt or in the new power shell only go to the directory containing the downloaded files and type: `C:\yourfiles\EarthquakesFeed\>earthfeeds.py`
    
###MacOs/Linux:
1. Open a terminal/Bash go to the proyect folder and type:
2. `$ chmod +x earthfeeds.py`
3. `$ ./earthfeeds.py`
    
##Options
|     Option    | Default |                                   Description                                  |
|:-------------:|:-------:|:------------------------------------------------------------------------------:|
| -h, --help    |   none  | Get the list of options and a few examples                                     |
| --search=     |   all   | The type of search you can do, the values can be *local* or *all*              |
| --margnitude= |   2.0   | Te min magnituded of the earthquakes, the value must by a number               |
| --wait=       |    5    | The time of minutes the program wait for retrive new information from the USGS |
| --latitud=    |  32.62  | Your latitud for a local search                                                |
| --longitud=   | -115.45 | Your longitud for a local search                                               |
| --north=      |   200   | Number of kilometers North of your posision where he will start looking        |
| --south=      |   200   | Number of kilometers South of your posision where he will start looking        |
| --west=       |   200   | Number of kilometers West of your posision where he will start looking         |
| --east=       |   200   | Number of kilometers East of your posision where he will start looking         |

##Examples
* If you live in Tokio for example and you want to search for a 200 km around tokio you type:
    `$ ./earthfeeds.py --search=local --latitud=35.6895000 --longitud=139.6917100`

* If you live in Los Angeles and you want a 500 km around search you type:
    `$ ./earthfeeds.py --search=local --latitud=34.0522 --longitud=-118.2436 --north=500 --east=500 --south=500 --west=500`
    
##Reference
To get your Coordenates: http://www.coordenadas-gps.com/


##Coming Soon:
    1.-GUI base on Tk for easy configuration
    2.-And more so stay tuned

    

    
