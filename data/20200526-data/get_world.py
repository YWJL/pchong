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


def write_list_to_json(list, json_file_name, json_file_save_path):
    os.chdir(json_file_save_path)
    with open(json_file_name, 'w') as  f:
        json.dump(list, f)

#函数get_world_data参数说明{
#     url为目标数据的网页
#     headers为请求服务
#     entries为所要数据的位置，
#     date为数据开始的日期的位置
#     want_data_class为获取数据的类型（active，confirm，death，cover）
# }
def get_world_data(url,headers,entires,date,want_data_class):

    res = requests.get(url, headers=headers)
    res.encoding = "UTF-8"
    pattern = re.compile(
        '(\'\{"(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}\}\')',
        re.S)
    end = re.findall(pattern, res.text)
    a = str(end[0])
    with open('former_data.txt', 'w') as f:
        f.write(res.text)

    data_relative_confirmed_json = []
    pattern_1 = re.compile('(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}',re.S)
    end_1 = re.findall(pattern_1, a)
    country = []
    for i in range(len(end_1)):
        data = {
            'Country': '',
        }
        data['Country'] = end_1[i][0]
        # 确诊人数
        country.append(end_1[i][0])
        care = end_1[i][entires].replace('[', '').replace(']', '').split(',')
        try:
            time = end_1[i][date].replace('/', ',').replace('/', ',').replace('"', '').split(',')
            print(time)
            time[2] = '2020'
            date = []
            in_date = time[2] + '-' + time[0] + '-' + time[1]
            dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
            for k in range(len(end_1[i][entires].replace('[', '').replace(']', '').split(','))):
                out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                dt = datetime.datetime.strptime(out_date, "%Y-%m-%d")
                date.append(out_date)
            print(date)
            time_care = OrderedDict(zip(date, care))
            print(time_care)
            date_json = OrderedDict(data, **time_care)
            data_relative_confirmed_json.append(date_json)

        except:
            pass

    with open('last_world_data.txt', 'w') as f:
        f.write(str(data_relative_confirmed_json))
    write_list_to_json(data_relative_confirmed_json, '20200517-world-'+want_data_class+'-data.json','E:/python_code/cov-19/world_cov19')
    data_csv = pd.DataFrame(json.loads(open('20200517-world-'+want_data_class+'-data.json', 'r+').read()))
    print(end_1[36][0])
    care = end_1[36][entires].replace('[', '').replace(']', '').split(',')
    try:
        time = end_1[36][date].replace('/', ',').replace('/', ',').replace('"', '').split(',')
        print(time)
        time[2] = '2020'
        date = []
        in_date = time[2] + '-' + time[0] + '-' + time[1]
        dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
        for k in range(len(end_1[36][entires].replace('[', '').replace(']', '').split(','))):
            out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            dt = datetime.datetime.strptime(out_date, "%Y-%m-%d")
            date.append(out_date)
        print(date)
        time_care = OrderedDict(zip(date, care))
        print(time_care)
    except:
        pass

    date.insert(0, 'Country')
    cols = date
    data_csv = data_csv.loc[:, cols]
    data_csv.T
    data_csv.to_csv('20200517-world-'+want_data_class+'-data.json.csv')
    df = pd.read_csv('20200517-world-'+want_data_class+'-data.json.csv')
    new_csv = df.T
    new_csv.to_csv('20200517-world-'+want_data_class+'-data.json.csv')


    ####################################

url = 'https://coronavirus.1point3acres.com/_next/static/chunks/c16cc2d75bca1e6a934a38b16acb5832e9f4c56d.742616c3ed15ad3de243.js'
headers = {
    'User-Agent':'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
}
end_1=get_world_data(url,headers,5,6,'active')
end_2=get_world_data(url,headers,7,8,'confirm')
end_3=get_world_data(url,headers,9,10,'death')
end_4=get_world_data(url,headers,11,12,'cover')
