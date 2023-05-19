import requests
import json
import pyttsx3
readAloud = pyttsx3.init()  #this is initialisation of pyttsx3 with readaloud any name we could have given inm place of readaloud

city = input('Enter the name of city you want to know the Weather:')

url = f"https://api.weatherapi.com/v1/current.json?key=776f54d161f8460798f133713231905&q={city}"        #fetching the api


r = requests.get(url)

# print(r.text)
 
weatherdictionary = json.loads(r.text)   #converting into dictionarty of python for fetching or gettinng particular data for example here current temp

w = weatherdictionary["current"]["temp_c"]

readAloud.say(f"the current weather of ther city {city} is {w}")
readAloud.runAndWait()  #this is just a funtion with say for waiting after A reading aloud


