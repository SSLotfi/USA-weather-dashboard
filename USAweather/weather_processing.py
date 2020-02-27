import requests
import json

KEY = "be1ae457a890894c4854d1796e11012f"
FORECASTKEY = "8a0009734c094cbb3d34fe588a43fba4"

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware",
    "Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine",
    "MaryLand","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",'Nebraska',"Nevada",
    "New Hampshire","New Jersey","New Mexico","New York","North Carolina",'North Dakota',"Ohio","Oklahoma",
    "Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont",
    "Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

states_postalcode = ['35801','99501','85001','72201','90001',"80011","06101",'19901','33124','30301','96801',
'83254','60601','46201','52801','67201','41701','70112','04032','21201','02101','49036','55801','39530','63101',
'59044','68901','89501','03217','07039','87500','10001','27565','58282','44101','74101','97201','15201','02840','29020',
'57401','37201','78701','84321','05751','24517','98004','25813','53201','82941']

def GetWeatherData():
    states_dic = dict()

    for state in states:
        states_dic[state] = 99999;

    for state in states:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={state}&appid={KEY}&units=metric"
        res = requests.get(url)
        res = json.loads(res.text)
        try:
            states_dic[state] = res
        except:
            pass

    return states_dic

def GetSevenDayForecast(cityname):
    date_max_temp = []
    date_min_temp = []
    dates = []
    dates_dict = dict()
    temp_dict = dict()
    try:
        cityname = cityname[0].upper() + cityname[1:]
        index = states.index(cityname)
        postalcode = states_postalcode[index]
        url = f"http://api.weatherunlocked.com/api/forecast/us.{postalcode}?app_id=57920617&app_key={FORECASTKEY}"
        res = requests.get(url)
        res = json.loads(res.text)

        for day in res['Days']:
            dates.append(day['date'])
            date_max_temp.append(day['temp_max_c'])
            date_min_temp.append(day['temp_min_c'])
            temp_dict["temp_max_c"] = day["temp_max_c"]
            temp_dict["temp_min_c"] = day['temp_min_c'] 
            dates_dict[day['date']] = temp_dict
    except:
        pass
        
    print(dates_dict)
    return dates_dict,dates,date_max_temp,date_min_temp

def ProcessData(states_dic):
    states_temp_dic = dict()
    states_humidity_dic = dict()
    states_wind_dic = dict()

    DataList = dict()

    for state in states_dic.keys():
        try:
            states_temp_dic[state] = states_dic[state]['main']['temp']
            states_humidity_dic[state] = states_dic[state]['main']['humidity']
            states_wind_dic[state] = states_dic[state]['wind']['speed']
        except:
            states_temp_dic[state] = 99999;
            states_humidity_dic[state] = 0;
            states_wind_dic[state] = 0;

    states_temp_dic = {k: v for k, v in sorted(states_temp_dic.items(), key=lambda item: item[1],reverse = True)}
    states_humidity_dic = {k: v for k, v in sorted(states_humidity_dic.items(), key=lambda item: item[1],reverse = True)}
    states_wind_dic = {k: v for k, v in sorted(states_wind_dic.items(), key=lambda item: item[1],reverse = True)}

    # print(states_temp_dic.values())

    Hotest_state = list(states_temp_dic.keys())[0]
    Hotest_temp = list(states_temp_dic.values())[0]
    Coldest_state = list(states_temp_dic.keys())[-1]
    Coldest_temp = list(states_temp_dic.values())[-1]
    Highest_humidity_state = list(states_humidity_dic.keys())[0]
    Highest_humidity = list(states_humidity_dic.values())[0]
    Fastest_wind_state = list(states_wind_dic.keys())[0]
    Fastest_wind = list(states_wind_dic.values())[0]

    DataList['Hotest_state'] = Hotest_state
    DataList['Hotest_temp'] = Hotest_temp
    DataList['Coldest_state'] = Coldest_state
    DataList['Coldest_temp'] = Coldest_temp
    DataList['Highest_humidity_state'] = Highest_humidity_state
    DataList['Highest_humidity'] = Highest_humidity
    DataList['Fastest_wind_state'] = Fastest_wind_state
    DataList['Fastest_wind'] = Fastest_wind


    return DataList

def GetHumidityState(cityname):
    res = dict()
    temp_dict = {'humidity' : 0}
    res['main'] = temp_dict
    if cityname in states:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={KEY}&units=metric"
        res = requests.get(url)
        res = json.loads(res.text)
        validation_text = "State exists"
    else:
        validation_text = "State doesn't exist"

    return res['main']['humidity'],validation_text