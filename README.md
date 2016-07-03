###Earthquakes Feed

This is an application to take all global and/or local ground motion with updated "real time data", still in development so feel free to comment or support

##How to use
For the moment is only in Command Interface for windows, mac and linux and it is necessary to have installed python (windows)
 
###Windows:
    Doble click on earthfeed.py
    
###MacOs/Linux:
    1.-Open a terminal/Bash go to the proyect folder and type:
    'python earthfeeds.py'
    
##Options
To get all command's available type:

    `python earthfeeds.py --help`
    
    `python earthfeeds.py -h`
    
To change a limit of earthquakes magnituded (ej. 3.0)
    `python earthfeeds.py --magnitude=3.0`
    
To change the time of the program refresh the data type (ej. 1 min.):
    `python earthfeeds.py --wait=1`
    
To change search type from global to local:
>At this time te local search only search south california and part of north of mexico, this will change soon, for the moment the latitud and longitud are in 32.62 and -115.45 and search a radius of 200 km.
    
    python earthfeeds.py --seach=local

##Coming Soon:
    1.-Update the latitud and longitud of te local position
    2.-Update the radius of the local search to making bigger or lower
    3.-GUI base on Tk for easy configuration
    4.-Add the unix directive '!#'
    5.-And more so stay tuned

    

    