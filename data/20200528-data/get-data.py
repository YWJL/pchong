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
def write_list_to_json(list, json_file_name):
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
    with open('20200527_data_1point3acres.txt', 'w') as f:
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
    write_list_to_json(data_relative_confirmed_json,date[-1]+'-world-confirm-data.json')
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
    os.remove(date[-1] + '-world-confirm-data.json')
    return date[-1]
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
        

    write_list_to_json(data_relative_confirmed_json,date[-1]+'-world-death-data.json',)
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
    os.remove(date[-1]+'-world-death-data.json')
    return date[-1]

####################################################################################

#函数作用：获取世界疫情
#函数get_state_data参数说明{
#     url为目标数据的网页
#     headers为请求服务
# }
def get_state_data(url,headers,csv_date):
    res = requests.get(url,headers = headers)
    res.encoding = "UTF-8"
    pattern = re.compile('state_name":(.*?),"county":(.*?),"entries":(.*?)}',re.S)
    end = list(re.findall(pattern,res.text))
    state_name='state_name'
    county='county'
    entries='entries'
    a=[]
    with open('former_us-state_data.txt','w') as f:
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
    with open('last_us-state_data.txt','w') as f:
        f.write(str(a))
    write_list_to_json(a,csv_date+'-data.json')
    data_csv=pd.DataFrame(json.loads(open(csv_date+'-data.json','r+').read()))
    cols=time
    data_csv=data_csv.loc[:,cols]
    data_csv.to_csv(csv_date+'-data.json.csv')
    os.remove(csv_date+'-data.json')
#########################################################################################
def get_GA_data(csv_date):
    a=[]
    with open(csv_date+'-data.json.csv','r') as csvfile:
        reader=csv.reader(csvfile)
        rows=[row for row in reader]
    a.append(rows[0][1:-1])
    print(rows)
    for i in range(len(rows)):
        if rows[i][1]=='GA':
            a.append(rows[i][1:-1])
    with open(csv_date+"-GA.json.csv","w",newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        #先写入columns_name
        #写入多行用writerows
        writer.writerows(a)
##########################################################################
def get_us_state_data(csv_date):
    url = 'https://covidtracking.com/api/states'
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    res = requests.get(url,headers=headers)
    a = res.text
    with open('20200528_data_covidtracking.txt','w') as f:
        f.write(a)
    pattern=r'state":"(.*?)"'
    state = re.findall(pattern, a)
    for i in np.arange(len(state)):
        if state[i]=='AK':
            state[i]='Alask'
        if state[i]=='AL':
            state[i]='Alabama'
        if state[i]=='AR':
            state[i]='Arkansas'
        if state[i]=='AZ':
            state[i]='Arizona'
        if state[i]=='CA':
            state[i]='california'
        if state[i]=='CO':
            state[i]='colorado'
        if state[i]=='CT':
            state[i]='Connecticut'
        if state[i]=='DC':
            state[i]='Washington.D.C'
        if state[i]=='DE':
            state[i]='Delaware'
        if state[i]=='FL':
            state[i]='Florida'
        if state[i]=='GA':
            state[i]='Georgia'
        if state[i]=='HI':
            state[i]='Hawaii'
        if state[i]=='IA':
            state[i]='Iowa'
        if state[i]=='ID':
            state[i]='Idaho'
        if state[i]=='IL':
            state[i]='Illinois'
        if state[i]=='IN':
            state[i]='Indiana'
        if state[i]=='KS':
            state[i]='Kansas'
        if state[i]=='KY':
            state[i]='Kentucky'
        if state[i]=='LA':
            state[i]='Louisiana'
        if state[i]=='MA':
            state[i]='Massachusetts'
        if state[i]=='MD':
            state[i]='Maryland'
        if state[i]=='ME':
            state[i]='Maine'
        if state[i]=='MI':
            state[i]='Michigan'
        if state[i]=='MN':
            state[i]='Minnesota'
        if state[i]=='MO':
            state[i]='Missouri'
        if state[i]=='MS':
            state[i]='Mississippi'
        if state[i]=='MT':
            state[i]='Montana'
        if state[i]=='NC':
            state[i]='North Carolina'
        if state[i]=='ND':
            state[i]='North Dakota'
        if state[i]=='NE':
            state[i]='Nebraska'
        if state[i]=='NH':
            state[i]='New Hampshire'
        if state[i]=='NJ':
            state[i]='New Jersey'
        if state[i]=='NM':
            state[i]='New Mexico'
        if state[i]=='NV':
            state[i]='Nevada'
        if state[i]=='NY':
            state[i]='New York'
        if state[i]=='OH':
            state[i]='Ohio'
        if state[i]=='OK':
            state[i]='Oklahoma'
        if state[i]=='OR':
            state[i]='Oregon'
        if state[i]=='PA':
            state[i]='Pennsylvania'
        if state[i]=='RI':
            state[i]='Rhode Island'
        if state[i]=='SC':
            state[i]='South Carolina'
        if state[i]=='SD':
            state[i]='South Dakota'
        if state[i]=='TN':
            state[i]='Tennessee'
        if state[i]=='TX':
            state[i]='Texas'
        if state[i]=='UT':
            state[i]='Utah'
        if state[i]=='VA':
            state[i]='Virginia'
        if state[i]=='VT':
            state[i]='Vermont'
        if state[i]=='WA':
            state[i]='Washington'
        if state[i]=='WI':
            state[i]='Wisconsin'
        if state[i]=='WV':
            state[i]='West Virginia'
        if state[i]=='WY':
            state[i]='Wyoming'
        if state[i]=='PR':
            state[i]='Puerto Rico'
        if state[i]=='AS':
            state[i]='AS'
        if state[i]=='GU':
            state[i]='Guam'
        if state[i]=='MP':
            state[i]='Northern Mariana Islands'
        if state[i]=='VI':
            state[i]='US Virgin Islands'


    pattern=r'positive":(.*?),'
    positive=re.findall(pattern,a)
    pattern=r'positiveScore":(.*?),'
    positiveScore=re.findall(pattern,a)
    pattern=r'negativeScore":(.*?),'
    negativeScore=re.findall(pattern,a)
    pattern=r'negativeRegularScore":(.*?),'
    negativeRegularScore=re.findall(pattern,a)
    pattern=r'commercialScore":(.*?),'
    commercialScore=re.findall(pattern,a)
    pattern=r'grade":(.*?),'
    grade=re.findall(pattern,a)
    pattern=r'score":(.*?),'
    score=re.findall(pattern,a)
    pattern=r'"negative":(.*?),'
    negative=re.findall(pattern,a)
    pattern=r'pending":(.*?),'
    pending=re.findall(pattern,a)
    pattern=r'"hospitalizedCurrently":(.*?),'
    hospitalizedCurrently=re.findall(pattern,a)
    pattern=r'"hospitalizedCumulative":(.*?),'
    hospitalizedCumulative=re.findall(pattern,a)
    pattern=r'inIcuCurrently":(.*?),'
    inIcuCurrently=re.findall(pattern,a)
    pattern=r'inIcuCumulative":(.*?),'
    inIcuCumulative=re.findall(pattern,a)
    pattern=r'onVentilatorCurrently":(.*?),'
    onVentilatorCurrently=re.findall(pattern,a)
    pattern=r'onVentilatorCumulative":(.*?),'
    onVentilatorCumulative=re.findall(pattern,a)
    pattern=r'recovered":(.*?),'
    recovered=re.findall(pattern,a)
    pattern=r'lastUpdateEt":(.*?),'
    lastUpdateEt=re.findall(pattern,a)
    pattern=r'checkTimeEt":(.*?),'
    checkTimeEt=re.findall(pattern,a)
    pattern=r'death":(.*?),'
    death=re.findall(pattern,a)
    pattern=r'hospitalized":(.*?),'
    hospitalized=re.findall(pattern,a)
    pattern=r'total":(.*?),'
    total=re.findall(pattern,a)
    pattern=r'totalTestResults":(.*?),'
    totalTestResults=re.findall(pattern,a)
    pattern=r'posNeg":(.*?),'
    posNeg=re.findall(pattern,a)
    pattern=r'fips":(.*?),'
    fips=re.findall(pattern,a)
    pattern=r'dateModified":(.*?),'
    dateModified=re.findall(pattern,a)
    pattern=r'dateChecked":(.*?),'
    dateChecked=re.findall(pattern,a)
    with open(csv_date+'_data_covidtracking.csv','w',newline='')as f:
        csv_write=csv.writer(f,dialect='excel')
        csv_write.writerow(['state','positive','negative','pending','hospitalizedCurrently','hospitalizedCumulative','inIcuCurrently','inIcuCumulative','onVentilatorCurrently','onVentilatorCumulative','recovered','lastUpdateEt','checkTimeEt','death','hospitalized','total','totalTestResults','posNeg','fips','dateModified','dateChecked'])
        try:
            for i in np.arange(len(state)):
                csv_write.writerow([state[i],positive[i],negative[i],pending[i],hospitalizedCurrently[i],hospitalizedCumulative[i],inIcuCurrently[i],inIcuCumulative[i],onVentilatorCurrently[i],onVentilatorCumulative[i],recovered[i],lastUpdateEt[i],checkTimeEt[i],death[i],hospitalized[i],total[i],totalTestResults[i],posNeg[i],fips[i],dateModified[i],dateChecked[i]])
        except:
            pass        


###########################################################################################

url = 'https://coronavirus.1point3acres.com/_next/static/chunks/48438d725742a261beca44db99d4583d039a2a23.8933b481c35fc17d450f.js'
headers = {
    'User-Agent':'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
}
csv_date=get_world_confirm_data(url,headers)
get_world_death_data(url,headers)
print('请等待程序还在运行！！！！！！！！')
get_state_data(url,headers,csv_date)
get_GA_data(csv_date)
get_us_state_data(csv_date)
