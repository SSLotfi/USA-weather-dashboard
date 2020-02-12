# from flask import request, Flask
# import requests
# import json

# app = Flask(__name__)

# KEY = "be1ae457a890894c4854d1796e11012f"

# @app.route("/weather/", methods=['GET'])
# def weather():
#     """get city name and show weather
#     """
#     # get username from the url params
#     cityname = request.args.get('cityname', default=None, type=str)

#     response = ""

#     if cityname:
#         url = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={KEY}&units=metric"
#         res = requests.get(url)
#         res = json.loads(res.text)
#         try:
#             response = f"<h1>The current weather in {cityname} is {res['main']['temp']} °C</h1>"
#         except:
#             response = "<h1>city wasn't found :(</h1>"
#     else:
#         response = "<h1>city not found</h1>"

#     # return the response
#     return response


# @app.route('/')
# def index():
# 	return ('<h1>All is working !</h1>')

# if __name__ == "__main__":
# 	app.run()

# # while True:
# #         city_name = input("enter city name: ").strip()
# #         if city_name == 'q':
# #                 break
# #         params = {
# #         "city_name":city_name
# #         }
# #         url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={KEY}&units=metric"
# #         res = requests.get(url)
# #         res = json.loads(res.text)
# #         print(str(res['main']["temp"]) + " °C")


from USAweather import app

if __name__ == "__main__":
	app.run(threaded=True)