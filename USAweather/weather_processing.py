import requests
import json

KEY = "be1ae457a890894c4854d1796e11012f"

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware",
    "Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Lowa","Kansas","Kentucky","Louisiana","Maine",
    "MaryLand","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",'Nebraska',"Nevada",
    "New Hampshire","New Jersey","New Mexico","New York","North Carolina",'North Dakota',"Ohio","Oklahoma",
    "Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont",
    "Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

def GetWeatherData():
    states_dic = dict()

    for state in states:
        states_dic[state] = 99999;

    for state in states:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={state}&appid={KEY}&units=metric"
        res = requests.get(url)
        res = json.loads(res.text)
        try:
            states_dic[state] = res['main']['temp']
        except:
            res = dict()

    return states_dic

def ProcessData(res):
    Hotest_state = list(res.keys())[0]
    Hotest_temp = list(res.values())[0]
    # states_dic = dict()

    # for state in states:
    #     states_dic[state] = 99999;

    # try:
    #     states_dic[state] = res['main']['temp']
    # except:
    #     res = dict()

    # states_dic = {k: v for k, v in sorted(states_dic.items(), key=lambda item: item[1])}

    # Hotest_state = list(states_dic.keys())[0]
    # Hotest_temp = list(states_dic.values())[0]

    return Hotest_state,Hotest_temp