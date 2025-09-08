#this is an api infull . Its package is """""" requests """""" -this allows you to use web requests using python code as though you were a browser yourself
#API - Application Programming Interface

#python also has a json library that enables us to read json files and make them more readable 

#use the library 
import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()#guarantee that the user has placed in the name of the file and the name of a song 

#using the get function from the package 
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="+sys.argv[1]) #allowing the user to input the song 

#print(response.json()) #printing out the information as json but python request library will turn it into a dictionary from json 
print(json.dumps(response.json(), indent=2))  #indent - indents the information more cleanly but not too readable yet lmao
#dumpstring is dumps
