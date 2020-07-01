import requests
import json
from collections import OrderedDict
import pandas as pd
import csv
import os
import datetime

def write_list_to_json(list, json_file_name):
    with open(json_file_name, 'w') as  f:
        json.dump(list,f)
url=' https://covidtracking.com/api/v1/states/daily.csv'
headers = {'User-Agent':'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11'}
res = requests.get(url,headers = headers)
with open('covidtracking-us_state-data.csv','wb') as fw:
    fw.write(res.content)
all_data=pd.read_csv('covidtracking-us_state-data.csv',keep_default_na=False)
def get_data(classes):
    data_relative_confirmed_json=[]
    all_date=[all_data['date'][i*56] for i in range(len(all_data)//61)]
    all_care=[all_data['positive'][i] for i in range(len(all_data))]
    
    all_state=[all_data['state'][i] for i in range(0,56)]
    all_death=[all_data['death'][i] for i in range(len(all_data))]
    for i in range(0,56):
            data_dict = {'Country': ''}
            data_dict['Country'] = all_state[i]
            if classes==0:
                death=[str(all_death[i+j*56])  for j in range(len(all_data)//56)]
                cla='death'
            else:
                death=[str(all_care[i+j*56])  for j in range(len(all_data)//56)]
                cla='confirm'   
            time=[str(all_date[j]) for j in range(len(all_date))]
            time.reverse()
            death.reverse()
            time_death = OrderedDict(zip(time, death))
            date_json = OrderedDict(data_dict,**time_death)
            data_relative_confirmed_json.append(date_json)
    write_list_to_json(data_relative_confirmed_json, '20200529.json')
    time.insert(0,'Country')
    data_csv = pd.DataFrame(json.loads(open('20200529.json', 'r+').read()))
    os.remove('20200529.json')
    data_csv.to_csv(time[-1]+'-covidtracking-us_state-'+cla+'-data.json.csv',index=time)
    df = pd.read_csv(time[-1]+'-covidtracking-us_state-'+cla+'-data.json.csv')
    new_csv = df.T
    new_csv.to_csv(time[-1]+'-covidtracking-us_state-'+cla+'-data.json.csv')
get_data(0)
get_data(1)

