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
#将数组写入json文件方便pandas的读取
active_name_csv='20200605-world-active-data.json.csv'
active_name_json='20200605-world-active-data.json'

confirm_name_csv='20200605-world-confirm-data.json.csv'
confirm_name_json='20200605-world-confirm-data.json'

cover_name_csv='20200605-world-cover-data.json.csv'
cover_name_json='20200605-world-cover-data.json'

death_name_csv='20200605-world-death-data.json.csv'
death_name_json='20200605-world-death-data.json'

json_file_save_path='C:/Users/hp/Desktop/疫情分析项目/Epidemic_project/TimeLine'
def write_list_to_json(list, json_file_name, json_file_save_path):
    os.chdir(json_file_save_path)
    with open(json_file_name, 'w') as  f:
        json.dump(list, f)

url = 'https://coronavirus.1point3acres.com/_next/static/chunks/583d4f045a99b8de9311c9acb731f8dcf7fb439c.9678b541642e3633627c.js'
headers = {
    'User-Agent':'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
}
res = requests.get(url,headers = headers)
res.encoding = "UTF-8"
pattern = re.compile('(\'\{"(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}\}\')',re.S)
end = re.findall(pattern,res.text)
a=str(end[0])
with open('test.txt','w') as f:
    f.write(a)

data_relative_confirmed_json=[]
pattern_1 = re.compile('(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}',re.S)
end_1=re.findall(pattern_1,a)
country=[]
for i in range(len(end_1)):
    data={
        'Country':'',
    }
    data['Country']=end_1[i][0]
    #确诊人数
    country.append(end_1[i][0])
    care=end_1[i][5].replace('[','').replace(']','').split(',')
    try:
        time=end_1[i][6].replace('/',',').replace('/',',').replace('"','').split(',')
        print(time)
        time[2]='2020'
        date=[]
        in_date = time[2]+'-'+time[0]+'-'+time[1]
        dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
        for k in range(len(end_1[i][5].replace('[','').replace(']','').split(','))):
            out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            dt=datetime.datetime.strptime(out_date, "%Y-%m-%d")
            date.append(out_date)
        print(date)
        time_care=OrderedDict(zip(date,care))
        print(time_care)
        date_json=OrderedDict(data,**time_care)
        data_relative_confirmed_json.append(date_json)
        
    except:
        pass
    

write_list_to_json(data_relative_confirmed_json,active_name_json,json_file_save_path)
data_csv=pd.DataFrame(json.loads(open(active_name_json,'r+').read()))
print(end_1[36][0])
care=end_1[36][5].replace('[','').replace(']','').split(',')
try:
    time=end_1[36][6].replace('/',',').replace('/',',').replace('"','').split(',')
    print(time)
    time[2]='2020'
    date=[]
    in_date = time[2]+'-'+time[0]+'-'+time[1]
    dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
    for k in range(len(end_1[36][5].replace('[','').replace(']','').split(','))):
        out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        dt=datetime.datetime.strptime(out_date, "%Y-%m-%d")
        date.append(out_date)
    print(date)
    time_care=OrderedDict(zip(date,care))
    print(time_care)
except:
    pass


date.insert(0,'Country')
cols=date
data_csv=data_csv.loc[:,cols]
data_csv.T
data_csv.to_csv(active_name_csv)
df=pd.read_csv(active_name_csv)
new_csv=df.T
new_csv.to_csv(active_name_csv)


##################################################################################

print(1)

res = requests.get(url,headers = headers)
res.encoding = "UTF-8"
pattern = re.compile('(\'\{"(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}\}\')',re.S)
end = re.findall(pattern,res.text)
print(end)
a=str(end[0])
with open('test.txt','w') as f:
    f.write(a)
data_relative_confirmed_json=[]
pattern_1 = re.compile('(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}',re.S)
end_1=re.findall(pattern_1,a)
country=[]
for i in range(len(end_1)):
    data={
        'Country':'',
    }
    data['Country']=end_1[i][0]
    #确诊人数
    country.append(end_1[i][0])
    care=end_1[i][7].replace('[','').replace(']','').split(',')
    try:
        time=end_1[i][8].replace('/',',').replace('/',',').replace('"','').split(',')
        print(time)
        time[2]='2020'
        date=[]
        in_date = time[2]+'-'+time[0]+'-'+time[1]
        dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
        for k in range(len(end_1[i][7].replace('[','').replace(']','').split(','))):
            out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            dt=datetime.datetime.strptime(out_date, "%Y-%m-%d")
            date.append(out_date)
        print(date)
        time_care=OrderedDict(zip(date,care))
        print(time_care)
        date_json=OrderedDict(data,**time_care)
        data_relative_confirmed_json.append(date_json)
        
    except:
        pass
    

write_list_to_json(data_relative_confirmed_json,confirm_name_json,json_file_save_path)
data_csv=pd.DataFrame(json.loads(open(confirm_name_json,'r+').read()))
print(end_1[36][0])
care=end_1[36][7].replace('[','').replace(']','').split(',')
try:
    time=end_1[36][8].replace('/',',').replace('/',',').replace('"','').split(',')
    print(time)
    time[2]='2020'
    date=[]
    in_date = time[2]+'-'+time[0]+'-'+time[1]
    dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
    for k in range(len(end_1[36][7].replace('[','').replace(']','').split(','))):
        out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        dt=datetime.datetime.strptime(out_date, "%Y-%m-%d")
        date.append(out_date)
    print(date)
    time_care=OrderedDict(zip(date,care))
    print(time_care)
except:
    pass


date.insert(0,'Country')
cols=date
data_csv=data_csv.loc[:,cols]
data_csv.T
data_csv.to_csv(confirm_name_csv)
df=pd.read_csv(confirm_name_csv)
new_csv=df.T
new_csv.to_csv(confirm_name_csv)




########################################################################################

print(2)






res = requests.get(url,headers = headers)
res.encoding = "UTF-8"
pattern = re.compile('(\'\{"(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}\}\')',re.S)
end = re.findall(pattern,res.text)
a=str(end[0])
with open('test.txt','w') as f:
    f.write(a)
data_relative_confirmed_json=[]
pattern_1 = re.compile('(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}',re.S)
end_1=re.findall(pattern_1,a)
country=[]
for i in range(len(end_1)):
    data={
        'Country':'',
    }
    data['Country']=end_1[i][0]
    #确诊人数
    country.append(end_1[i][0])
    care=end_1[i][11].replace('[','').replace(']','').split(',')
    try:
        time=end_1[i][12].replace('/',',').replace('/',',').replace('"','').split(',')
        print(time)
        time[2]='2020'
        date=[]
        in_date = time[2]+'-'+time[0]+'-'+time[1]
        dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
        for k in range(len(end_1[i][11].replace('[','').replace(']','').split(','))):
            out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            dt=datetime.datetime.strptime(out_date, "%Y-%m-%d")
            date.append(out_date)
        print(date)
        time_care=OrderedDict(zip(date,care))
        print(time_care)
        date_json=OrderedDict(data,**time_care)
        data_relative_confirmed_json.append(date_json)
        
    except:
        pass
    

write_list_to_json(data_relative_confirmed_json,cover_name_json,json_file_save_path)
data_csv=pd.DataFrame(json.loads(open(cover_name_json,'r+').read()))
print(end_1[36][0])
care=end_1[36][11].replace('[','').replace(']','').split(',')
try:
    time=end_1[36][12].replace('/',',').replace('/',',').replace('"','').split(',')
    print(time)
    time[2]='2020'
    date=[]
    in_date = time[2]+'-'+time[0]+'-'+time[1]
    dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
    for k in range(len(end_1[36][11].replace('[','').replace(']','').split(','))):
        out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        dt=datetime.datetime.strptime(out_date, "%Y-%m-%d")
        date.append(out_date)
    print(date)
    time_care=OrderedDict(zip(date,care))
    print(time_care)
except:
    pass


date.insert(0,'Country')
cols=date
data_csv=data_csv.loc[:,cols]
data_csv.T
data_csv.to_csv(cover_name_csv)
df=pd.read_csv(cover_name_csv)
new_csv=df.T
new_csv.to_csv(cover_name_csv)



#######################################################################################

print(3)






res = requests.get(url,headers = headers)
res.encoding = "UTF-8"
pattern = re.compile('(\'\{"(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}\}\')',re.S)
end = re.findall(pattern,res.text)
a=str(end[0])
with open('test.txt','w') as f:
    f.write(a)
data_relative_confirmed_json=[]
pattern_1 = re.compile('(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}',re.S)
end_1=re.findall(pattern_1,a)
country=[]
for i in range(len(end_1)):
    data={
        'Country':'',
    }
    data['Country']=end_1[i][0]
    #确诊人数
    country.append(end_1[i][0])
    care=end_1[i][9].replace('[','').replace(']','').split(',')
    try:
        time=end_1[i][10].replace('/',',').replace('/',',').replace('"','').split(',')
        print(time)
        time[2]='2020'
        date=[]
        in_date = time[2]+'-'+time[0]+'-'+time[1]
        dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
        for k in range(len(end_1[i][9].replace('[','').replace(']','').split(','))):
            out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            dt=datetime.datetime.strptime(out_date, "%Y-%m-%d")
            date.append(out_date)
        print(date)
        time_care=OrderedDict(zip(date,care))
        print(time_care)
        date_json=OrderedDict(data,**time_care)
        data_relative_confirmed_json.append(date_json)
        
    except:
        pass
    

write_list_to_json(data_relative_confirmed_json,death_name_json,json_file_save_path)
data_csv=pd.DataFrame(json.loads(open(death_name_json,'r+').read()))
print(end_1[36][0])
care=end_1[36][9].replace('[','').replace(']','').split(',')
try:
    time=end_1[36][10].replace('/',',').replace('/',',').replace('"','').split(',')
    print(time)
    time[2]='2020'
    date=[]
    in_date = time[2]+'-'+time[0]+'-'+time[1]
    dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
    for k in range(len(end_1[36][9].replace('[','').replace(']','').split(','))):
        out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        dt=datetime.datetime.strptime(out_date, "%Y-%m-%d")
        date.append(out_date)
    print(date)
    time_care=OrderedDict(zip(date,care))
    print(time_care)
except:
    pass


date.insert(0,'Country')
cols=date
data_csv=data_csv.loc[:,cols]
data_csv.T
data_csv.to_csv(death_name_csv)
df=pd.read_csv(death_name_csv)
new_csv=df.T
new_csv.to_csv(death_name_csv)