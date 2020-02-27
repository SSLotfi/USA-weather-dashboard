from flask import Flask, render_template, request
import json
from USAweather.weather_processing import GetWeatherData,ProcessData,GetSevenDayForecast,GetHumidityState

app = Flask(__name__)  

@app.route("/" , methods=['GET', 'POST'])
def index(): 
        validation_text = "State exists"
        if request.method == 'POST':
                if "citynameinput" in request.form:
                        cityname = request.form['cityname']
                        cityname = cityname[0].upper() + cityname[1:]
                        print("-------------------------------------")
                        dates_dict,dates,date_max_temp,date_min_temp = GetSevenDayForecast(cityname)
                        humidity_forecast_state,validation_text = GetHumidityState(cityname)
                        dates_json = json.dumps(dates_dict)
                        print(date_max_temp)
                        print(date_min_temp)
                        print("-------------------------------------")
        else:
            dates = ["day1","day2","day3","day4","day5","day6","day7"]
            date_max_temp = [0,0,0,0,0,0,0]
            date_min_temp = [0,0,0,0,0,0,0]
            humidity_forecast_state = 0;
            cityname = ""
            dates_dict = dict()
            temp_dict = dict()
            for index in range(7):
                temp_dict["temp_max_c"] = date_max_temp[index]
                temp_dict["temp_min_c"] = date_min_temp[index]
                dates_dict[dates[index]] = temp_dict
            dates_json = json.dumps(dates_dict) 

        # preprocessing here

        Weather_data_dic = GetWeatherData()
        Data_List = ProcessData(Weather_data_dic)
        Hotest_state = Data_List['Hotest_state']
        Hotest_temp = Data_List['Hotest_temp']
        Coldest_state = Data_List['Coldest_state']
        Coldest_temp = Data_List['Coldest_temp']
        Highest_Humidity_state = Data_List['Highest_humidity_state']
        Highest_Humidity = Data_List['Highest_humidity']
        Fastest_wind = Data_List['Fastest_wind']
        Fastest_wind_state = Data_List['Fastest_wind_state']

        if validation_text == "State exists":
            validation_text = ""
        else:
            cityname = ""
        
        return render_template("mainpage.html",Hotest_state = Hotest_state,Hotest_temp = Hotest_temp,
        Coldest_state = Coldest_state,Coldest_temp = Coldest_temp,Highest_Humidity_state = Highest_Humidity_state,
        Highest_Humidity = Highest_Humidity, Fastest_wind = Fastest_wind, Fastest_wind_state = Fastest_wind_state ,
        dates = dates, date_max_temp = date_max_temp , date_min_temp = date_min_temp , forecast_state = cityname,
        humidity_forecast_state = humidity_forecast_state, validation_text = validation_text)
