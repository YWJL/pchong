import pandas as pd
#coding:utf-8
import asyncio
import os
from aiohttp import TCPConnector, ClientSession
from typing import List
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Line
import json
async def get_json_data(url: str) -> dict:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url=url) as response:
            return await response.json()
Js_data = asyncio.run(
    get_json_data(url="https://coronavirus.1point3acres.com/resources/maps/us_map/GA.json")
)    #或者这样获取网页json
name='20200517-data.json.csv'
name2='countycases-GA.csv'
data=pd.read_csv(name2)
print(data)
DATA=pd.read_csv(name)
print(len(DATA.columns.values))
day=len(DATA.columns.values)-3
print(DATA.columns.values[-1])#列名
# print(Positive)
print(DATA.iloc[0,0])
number=[]
number_cou=[]
Country=[]
Pos=[]
print(DATA)
for i in range(1,144):
    Country.append(DATA.iloc[i+383,2])
    Pos.append(float(DATA.iloc[i+383,-1]))
    for j in range(1,len(data)):
        if DATA.iloc[i + 383, 2] ==data.iloc[j,0]:
            number.append(data.iloc[j, 5])
            number_cou.append(data.iloc[j,0])
MAP_data=[list(z) for z in zip(Country,Pos)]
print(MAP_data)
print(Country[0])
print(data.iloc[0,0])
print('number:',number)
print(len(number))
print(sum(number))
Standard_num=[]          #GA州10W人口时，各县人口数
for i in range(1,len(number)):
    Standard_num.append(int(100000*number[i]/sum(number)))

# with open('20200508-GA-data.json', 'r') as f:
#     data2=json.loads(f.read())
# print(data2)
print(sum(Pos))
Posi=[]
Standard_data=[]
a=0
for i in range(1,len(number_cou)):
    for j in range(1,len(number_cou)):
        if number_cou[i]==Country[j]:
            a=int(Standard_num[i]*sum(Pos)/sum(number))
            if a==0:
                a=a+1
            Posi.append(a)

Standard_data=[list(z) for z in zip(number_cou,Posi)]
print('sum_Posi/100000',sum(Posi)/100000)
print('sum_Pos/sum_number',sum(Pos)/sum(number))
time="2020/{}".format(DATA.columns.values[-1])
(
    Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
    .add_js_funcs("echarts.registerMap('HK', {});".format(Js_data))
    # .add(
    #     series_name="Georgia州每10万人口的确诊病例数",
    #     maptype="HK",
    #     data_pair=Standard_data,
    #     # name_map=NAME_MAP_DATA,
    #     is_map_symbol_show=False,#红点标记
    # )
    .add(
        series_name="Georgia州确诊的病例数",
        maptype="HK",
        data_pair=MAP_data,
        # name_map=NAME_MAP_DATA,
        is_map_symbol_show=False,  # 红点标记
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Georgia州疫情情况",
            subtitle=time,
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b0}:{c0}"#{a}<br/>:{c0}此为换行
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=min(Pos),
            max_=max(Pos),
            range_text=["High", "Low"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
        ),
    )
    .render("GA-5-14.html")
)
