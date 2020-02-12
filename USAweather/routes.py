from flask import Flask, render_template, request
from USAweather.weather_processing import GetWeatherData,ProcessData

app = Flask(__name__)

@app.route("/")
def index():
    # preprocessing here
    Weather_data_dic = GetWeatherData()
    Hotest_state,Hotest_temp = ProcessData(Weather_data_dic)
    
    return render_template("mainpage.html",Hotest_state = Hotest_state,Hotest_temp = Hotest_temp)
