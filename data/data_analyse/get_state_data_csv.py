import re
import requests
import numpy as np
import json
import os
from collections import OrderedDict
import pandas as pd
import json
#将数组写入json文件方便pandas的读取
json_file_save_path='D:/Pchong/data_see/data_all'
state_csv='D:/Pchong/data_see/data_all/20200525-data.json.csv'
state_json='D:/Pchong/data_see/data_all/20200525-data.json'
def write_list_to_json(list, json_file_name, json_file_save_path):
    os.chdir(json_file_save_path)
    with open(json_file_name, 'w') as  f:
        json.dump(list, f)

url = 'https://coronavirus.1point3acres.com/_next/static/chunks/e37e607229e0228dedf6abb9f1e4f817577e9313.54f97d03ef4258f621c5.js'
headers = {
    'User-Agent':'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
}
res = requests.get(url,headers = headers)
res.encoding = "UTF-8"
pattern = re.compile('state_name":(.*?),"county":(.*?),"entries":(.*?)}',re.S)
end = list(re.findall(pattern,res.text))
state_name='state_name'
county='county'
entries='entries'
a=[]
# with open('former_us-state_data','w') as f:
#     f.write(res.text)
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
# with open('last_us-state_data.','w') as f:
#     f.write(str(a))
write_list_to_json(a,state_json,json_file_save_path)

data_csv=pd.DataFrame(json.loads(open(state_json,'r+').read()))
cols=time
data_csv=data_csv.loc[:,cols]
data_csv.to_csv(state_csv)