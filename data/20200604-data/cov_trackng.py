import re
import requests
import numpy as np
import json
import os
from collections import OrderedDict
import pandas as pd
import json
import datetime
import time
import csv
def write_list_to_json(list, json_file_name):
    with open(json_file_name, 'w') as  f:
        json.dump(list,f)
url=' https://covidtracking.com/api/v1/states/daily.csv'
headers = {
   'User-Agent':'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
}
res = requests.get(url,headers = headers)
res.encoding = "UTF-8"
with open('2020-05-30-covidtracking-us_state-data.csv','wb') as fw:
    fw.write(res.content)
with open('20200603-covidtracking-former_state-data.txt','wb') as fw:
    fw.write(res.content)
all_data=pd.read_csv('2020-05-30-covidtracking-us_state-data.csv')
all_date=[]
all_care=[]
all_state=[]
all_death=[]
data_json=[]
state=[]
data_relative_confirmed_json=[]
for i in range(len(all_data)):
    all_care.append(all_data['positive'][i])
    all_death.append(all_data['death'][i])
for i in range(0,56):
    all_state.append(all_data['state'][i])
    state.append('state')
for i in range(0,30):
    all_date.append(all_data['date'][i*57])
print(all_date)
for i in range(0,56):
        data_dict = {
            'Country': '',
        }
        data_dict['Country'] = all_state[i]
        care=[]
        time=[]
        # 确诊人数
        for j in range(0,30):
            care.append(int(all_care[i+j*56]))
            time.append(int(all_date[j]))

        time_care = OrderedDict(zip(time, care))
        date_json = OrderedDict(data_dict,**time_care)
        data_relative_confirmed_json.append(date_json)    
print(time)
print(write_list_to_json)
write_list_to_json(data_relative_confirmed_json, '20200529.json')
data_csv = pd.DataFrame(json.loads(open('20200529.json', 'r+').read()))

time.insert(0, 'Country')
print(time)
for i in range(len(time)):
    time[i]=str(time[i])
cols = time
data_csv = data_csv.loc[:, cols]
data_csv.T
data_csv.to_csv(time[1]+'-covidtracking-us_state-confirm-data.json.csv')
df = pd.read_csv(time[1]+'-covidtracking-us_state-confirm-data.json.csv')
new_csv = df.T
new_csv.to_csv(time[1]+'-covidtracking-us_state-confirm-data.json.csv')
with open(time[1]+'-covidtracking-last-us_state-confirm-data.txt', 'w') as f:
    f.write(str(data_relative_confirmed_json))

################################################################################################
all_data=pd.read_csv('2020-05-30-covidtracking-us_state-data.csv')
all_date=[]
all_care=[]
all_state=[]
all_death=[]
data_json=[]
state=[]
data_relative_confirmed_json=[]
for i in range(len(all_data)):
    all_care.append(all_data['positive'][i])
    all_death.append(all_data['death'][i])
for i in range(0,56):
    all_state.append(all_data['state'][i])
    state.append('state')
for i in range(0,30):
    all_date.append(all_data['date'][i*57])
print(all_date)
for i in range(0,56):
        data_dict = {
            'Country': '',
        }
        data_dict['Country'] = all_state[i]
        death=[]
        time=[]
        # 确诊人数
        for j in range(0,30):
            death.append(int(all_death[i+j*56]))
            time.append(int(all_date[j]))

        time_death = OrderedDict(zip(time, death))
        date_json = OrderedDict(data_dict,**time_death)
        data_relative_confirmed_json.append(date_json)    
print(time)
print(write_list_to_json)
write_list_to_json(data_relative_confirmed_json, '20200529.json')
data_csv = pd.DataFrame(json.loads(open('20200529.json', 'r+').read()))

time.insert(0, 'Country')
print(time)
for i in range(len(time)):
    time[i]=str(time[i])
cols = time
data_csv = data_csv.loc[:, cols]
data_csv.T
data_csv.to_csv(time[1]+'-covidtracking-us_state-death-data.json.csv')
df = pd.read_csv(time[1]+'-covidtracking-us_state-death-data.json.csv')
new_csv = df.T
new_csv.to_csv(time[1]+'-covidtracking-us_state-death-data.json.csv')
with open(time[1]+'-covidtracking-last-us_state-death-data.txt', 'w') as f:
    f.write(str(data_relative_confirmed_json))
os.remove('20200529.json')
os.remove('2020-05-30-covidtracking-us_state-data.csv')
def csv_dropline(filename):
    data = pd.read_csv(filename)
    data_new=data.drop([0,1]) #删除0行数据
    data_new.to_csv(filename,index=0)
csv_dropline(time[1]+'-covidtracking-us_state-death-data.json.csv')
csv_dropline(time[1]+'-covidtracking-us_state-confirm-data.json.csv')