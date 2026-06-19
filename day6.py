#pip install requests.....Api ko access kerane ke liye 

# import requests
# def weather_data(city):
#     url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=f5e89d59e59e437dd1aece24c1189ad5&units=metric" 
    
#     try:
#         response=requests.get(url)
#         response.raise_for_status()
#         data = response.json()
#         print(data['main']['temp'])
#     except response.exceptions.RequestException as e:

#         print(e)

# city = input("Enter your city:")
# weather_data(city)


#Doubt...........
import pywhatkit

pywhatkit.sendwhatmsg("+917300427924","Hi",11,17)

#OR
# import pywhatkit
# import datetime

# now = datetime.datetime.now()

# pywhatkit.sendwhatmsg(
#     "+919876543210",
#     "Hi",
#     now.hour,
#     now.minute + 2
# )