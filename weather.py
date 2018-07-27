import requests
d={}
print("Enter city")
city=input()
url='http://api.openweathermap.org/data/2.5/weather?q='
n='&APPID=dc8380611c92e497d3eb7eae25bc62ea'
requrl=url+city+n
a=requests.get(requrl)
d=a.json()["main"]
print("Maximum temperature of ",city)
print(d["temp_max"])
print("Minimum temerature of",city)
print(d["temp_min"])

