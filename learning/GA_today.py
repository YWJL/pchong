import pandas as pd
#coding:utf-8
import asyncio
import os
from aiohttp import TCPConnector, ClientSession
from typing import List
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Bar, Timeline
from pyecharts import options as opts
from pyecharts.charts import Grid, Line, Scatter,Map
import json
import re
import os
path='D:\Pchong\data_see\daily'
os.chdir(path)
async def get_json_data(url: str) -> dict:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url=url) as response:
            return await response.json()

Js_data = asyncio.run(
    get_json_data(url="https://coronavirus.1point3acres.com/resources/maps/us_map/GA.json")
)    #或者这样获取网页json
name='D:/Pchong/data_see/data_all/20200523-data.json.csv'
name2='countycases-GA.csv'
data=pd.read_csv(name2)
DATA=pd.read_csv(name)
day=len(DATA.columns.values)-3
# print(DATA.columns.values[-1])#列名
# print(Positive)
print(DATA.iloc[0,0])
number=[]
number_cou=[]
Country=[]
Pos=[]
print(DATA)
for i in range(391,477):
    Country.append(DATA.iloc[i,2])
    Pos.append(float(DATA.iloc[i,-1]))
for i in range(479,534):
    Country.append(DATA.iloc[i,2])
    Pos.append(float(DATA.iloc[i,-1]))
Country.append('McIntosh')
Pos.append(float(DATA.iloc[478,-1]))
Country.append('McDuffie')
Pos.append(float(DATA.iloc[477,-1]))
Country.append(DATA.iloc[2420,2])
Pos.append(float(DATA.iloc[2420,-1]))
Country.append(DATA.iloc[2417,2])
Pos.append(float(DATA.iloc[2417,-1]))
Country.append(DATA.iloc[2511,2])
Pos.append(float(DATA.iloc[2511,-1]))
Country.append(DATA.iloc[3026,2])
Pos.append(float(DATA.iloc[3026,-1]))
Country.append(DATA.iloc[2636,2])
Pos.append(float(DATA.iloc[2636,-1]))
Country.append(DATA.iloc[3055,2])
Pos.append(float(DATA.iloc[3055,-1]))
Country.append(DATA.iloc[2550,2])
Pos.append(float(DATA.iloc[2550,-1]))
Country.append(DATA.iloc[2418,2])
Pos.append(float(DATA.iloc[2418,-1]))
Country.append(DATA.iloc[2592,2])
Pos.append(float(DATA.iloc[2592,-1]))
Country.append(DATA.iloc[2788,2])
Pos.append(float(DATA.iloc[2788,-1]))
Country.append(DATA.iloc[2814,2])
Pos.append(float(DATA.iloc[2814,-1]))
Country.append(DATA.iloc[2385,2])
Pos.append(float(DATA.iloc[2385,-1]))
Country.append(DATA.iloc[2419,2])
Pos.append(float(DATA.iloc[2419,-1]))
Country.append(DATA.iloc[2619,2])
Pos.append(float(DATA.iloc[2619,-1]))
Country.append(DATA.iloc[2357,2])
Pos.append(float(DATA.iloc[2357,-1]))
Country.append(DATA.iloc[2620,2])
Pos.append(float(DATA.iloc[2620,-1]))
Country.append(DATA.iloc[2591,2])
Pos.append(float(DATA.iloc[2591,-1]))
print('Country:',Country)
print('data:',len(data))
print('Pos:',Pos)
print()
# for i in range(0,len(Country)):
#     for j in range(0,len(data)):
#         if re.match(Country[i],test1):
#             pass
#         else:
#             print(Country[i])

POS=[list(z) for z in zip(Country,Pos)]
print('POS:',POS)
time="2020/{}".format(DATA.columns.values[-1])
(
    Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
    .add_js_funcs("echarts.registerMap('HK', {});".format(Js_data))
    .add(
        series_name="Georgia州疫情情况",
        maptype="HK",
        data_pair=POS,
        # name_map=NAME_MAP_DATA,
        is_map_symbol_show=False,#红点标记
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Georgia州疫情情况",
            # subtitle="{}，若各县人口数为100，000时，各县市的感染数".format(time),
            subtitle="{}".format(time),
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b}县{c}人感染"#{a}<br/>:{c0}此为换行
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=min(Pos),
            max_=max(Pos),
            range_text=["High", "Low"],
            is_calculable=True,
            # range_color=["lightskyblue", "yellow", "orangered"],
        ),
    )
    .render("GA-5-23.html")
)
""""""











































# test1=[] 
# test2=[]
# print(data.iloc[len(data)-1,0])
# for i in range(0,len(data)):
#     test1.append(data.iloc[i,0])
#     test2.append(float(data.iloc[i,2]))
# test3=[list(z) for z in zip(test1,test2)]
# print('test3:',test3)

















