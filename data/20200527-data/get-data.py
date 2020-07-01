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
##############################################
#函数作用：写入数据到json文件
def write_list_to_json(list, json_file_name, json_file_save_path):
    os.chdir(json_file_save_path)
    with open(json_file_name, 'w') as  f:
        json.dump(list, f)
#############################################

#函数作用：获取世界疫情
#函数get_world_data参数说明{
#     url为目标数据的网页
#     headers为请求服务
#     entries为所要数据的位置，
#     date为数据开始的日期的位置
#     want_data_class为获取数据的类型（active，confirm，death，cover）
# }
def get_world_confirm_data(url,headers):

    res = requests.get(url,headers = headers)
    res.encoding = "UTF-8"
    pattern = re.compile('(\'\{"(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}\}\')',re.S)
    end = re.findall(pattern,res.text)
    print(end)
    a=str(end[0])
    data_relative_confirmed_json=[]
    pattern_1 = re.compile('(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}',re.S)
    end_1=re.findall(pattern_1,a)
    country=[]
    with open('former_data.txt', 'w') as f:
        f.write(res.text)
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
        
    with open('last_data.txt', 'w') as f:
        f.write(str(data_relative_confirmed_json))
    write_list_to_json(data_relative_confirmed_json,date[-1]+'-world-confirm-data.json','E:/python_code/cov-19/world_cov19')
    data_csv=pd.DataFrame(json.loads(open(date[-1]+'-world-confirm-data.json','r+').read()))
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
    data_csv.to_csv(date[-1]+'-world-confirm-data.json.csv')
    df=pd.read_csv(date[-1]+'-world-confirm-data.json.csv')
    new_csv=df.T
    new_csv.to_csv(date[-1]+'-world-confirm-data.json.csv')
#############################################################################
def get_world_death_data(url,headers):
    res = requests.get(url,headers = headers)
    res.encoding = "UTF-8"
    pattern = re.compile('(\'\{"(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}\}\')',re.S)
    end = re.findall(pattern,res.text)
    a=str(end[0])

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
        

    write_list_to_json(data_relative_confirmed_json,date[-1]+'-world-death-data.json','E:/python_code/cov-19/world_cov19')
    data_csv=pd.DataFrame(json.loads(open(date[-1]+'-world-death-data.json','r+').read()))
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
    data_csv.to_csv(date[-1]+'-world-death-data.json.csv')
    df=pd.read_csv(date[-1]+'-world-death-data.json.csv')
    new_csv=df.T
    new_csv.to_csv(date[-1]+'-world-death-data.json.csv')



####################################################################################

#函数作用：获取世界疫情
#函数get_state_data参数说明{
#     url为目标数据的网页
#     headers为请求服务
# }
def get_state_data(url,headers):
    res = requests.get(url,headers = headers)
    res.encoding = "UTF-8"
    pattern = re.compile('state_name":(.*?),"county":(.*?),"entries":(.*?)}',re.S)
    end = list(re.findall(pattern,res.text))
    state_name='state_name'
    county='county'
    entries='entries'
    a=[]
    with open('former_us-state_data','w') as f:
        f.write(res.text)
    #过滤出州和区的名字组成字典
    for i in range(len(end)):  
        data={
            "state_name:":[],
            "county:":[],
            
        } 
        data['state_name:'].append(end[i][0])
        data["county:"].append(end[i][1])
        
        data['state_name:']=','.join(data['state_name:'])
        data["county:"]=','.join(data["county:"])
        
        data['state_name:']=list(data['state_name:'])
        data["county:"]=list(data["county:"])
        
        #过滤出日期和确诊数，通过zip拉取起来
        date=re.findall(pattern,res.text)
        date_new=date[i][2].replace('[[',',[').replace(']]','],')
        re_compile = re.compile('"(.*?)",(.*?)]')
        date_care=re.findall(re_compile,date_new)
        time=[]
        care=[]
        for i in range(len(date_care)):
            time.append(date_care[i][0])
            care.append(date_care[i][1])

        time_care=OrderedDict(zip(time,care))
    #数据清洗
        for i in range(len(data['state_name:'])):
            data['state_name:'][i]=data['state_name:'][i].replace('\"','').replace('[','').replace(']','')
        for i in range(len(data["county:"])):
            data["county:"][i]=data["county:"][i].replace('\"','').replace('[','').replace(']','')
        
        data['state_name:']=''.join(data['state_name:'])
        data["county:"]=''.join(data["county:"])
        
        b={
            "state_name:":'',
            "county:":'',
            "entries:":''
        } 
        b["state_name:"]=data['state_name:']
        b["county:"]=data["county:"]
        
        b=OrderedDict(b,**time_care)
        time.insert(0,'state_name:')
        time.insert(1,"county:")
        a.append(b)
    with open('last_us-state_data','w') as f:
        f.write(str(a))
    write_list_to_json(a,'20200515-data.json','E:/python_code/cov-19/us_state_cov19')
    data_csv=pd.DataFrame(json.loads(open('E:/python_code/cov-19/us_state_cov19/20200515-data.json','r+').read()))
    cols=time
    data_csv=data_csv.loc[:,cols]
    data_csv.to_csv('E:/python_code/cov-19/us_state_cov19/20200515-data.json.csv')
#########################################################################################
def get_GA_data():
    a=[]
    with open('E:/python_code/cov-19/us_state_cov19//20200515-data.json.csv','r') as csvfile:
        reader=csv.reader(csvfile)
        rows=[row for row in reader]
    a.append(rows[0])
    print(rows)
    for i in range(len(rows)):
        if rows[i][1]=='GA':
            a.append(rows[i])
    with open("E:/python_code/cov-19/us_state_cov19//20200515-GA.json.csv","w",newline='',encoding='utf-8') as csvfile: 
        writer = csv.writer(csvfile)
        #先写入columns_name
        #写入多行用writerows
        writer.writerows(a)


###########################################################################################

url = 'https://coronavirus.1point3acres.com/_next/static/chunks/491ecfa7d97b9edf854e09b4c67c79c6dc6c4a8f.1cb1e0a704977556386d.js'
headers = {
    'User-Agent':'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
}
get_world_confirm_data(url,headers)
get_world_death_data(url,headers)
print('请等待程序还在运行！！！！！！！！')
get_state_data(url,headers)
get_GA_data()

