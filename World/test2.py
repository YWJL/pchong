import pandas as pd
#coding:utf-8
import asyncio
import os
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline
from pyecharts.faker import Faker
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
with open('GA.json', 'r') as f:
    Js_2data=json.loads(f.read())
name='daily.csv'
name='20200510-data.json.csv'
DATA=pd.read_csv(name)
print(len(DATA.columns.values))
day=len(DATA.columns.values)-3
print(DATA.columns.values[-1])#列名
# print(Positive)
print(DATA.iloc[0,0])
Country=[]
Pos=[]
print(DATA)
for i in range(1,144):
    Country.append(DATA.iloc[i+383,2])
    Pos.append(float(DATA.iloc[i+383,-1]))
MAP_data=[list(z) for z in zip(Country,Pos)]
print(MAP_data)
# with open('20200508-GA-data.json', 'r') as f:
#     data2=json.loads(f.read())
# print(data2)
print(sum(Pos))
rate=100000/sum(Pos)
Posi_7=[]
Posi_6=[]
Posi_5=[]
Posi_4=[]
Posi_3=[]
Posi_2=[]
Posi_1=[]

for i in range(1,144):
    Posi_1.append(int(float(rate*float(DATA.iloc[i+383,-1]))))
    Posi_2.append(int(float(rate*float(DATA.iloc[i+383,-2]))))
    Posi_3.append(int(float(rate*float(DATA.iloc[i+383,-3]))))
    Posi_4.append(int(float(rate*float(DATA.iloc[i+383,-4]))))
    Posi_5.append(int(float(rate*float(DATA.iloc[i+383,-5]))))
    Posi_6.append(int(float(rate*float(DATA.iloc[i+383,-6]))))
    Posi_7.append(int(float(rate*float(DATA.iloc[i+383,-7]))))
Standard_data_7=[list(z) for z in zip(Country,Posi_7)]
pos={}
pos[0]=[list(z) for z in zip(Country,Posi_1)]
pos[1]=[list(z) for z in zip(Country,Posi_2)]
pos[2]=[list(z) for z in zip(Country,Posi_3)]
pos[3]=[list(z) for z in zip(Country,Posi_4)]
pos[4]=[list(z) for z in zip(Country,Posi_5)]
pos[5]=[list(z) for z in zip(Country,Posi_6)]
pos[6]=[list(z) for z in zip(Country,Posi_7)]
print(sum(Posi_7))
time="2020/{}".format(DATA.columns.values[-1])
tl = Timeline()
for i in range(0,7):
    map_ga = (
        Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
            .add_js_funcs("echarts.registerMap('GA', {});".format(Js_2data))
            .add(
            series_name="Georgia州每10万人口的确诊病例数",
            maptype="GA",
            data_pair=pos[i],
            # name_map=NAME_MAP_DATA,
            is_map_symbol_show=False,  # 红点标记
            itemstyle_opts={Timeline
                },
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Georgia州疫情情况",
                subtitle=time,
            ),
            # tooltip_opts=opts.TooltipOpts(
            #     trigger="item", formatter="{a0}:{c0}"  # {a}<br/>:{c0}此为换行
            # ),
            visualmap_opts=opts.VisualMapOpts(
                min_=1,
                max_=7000,
                range_text=["High", "Low"],
                is_calculable=True,
                range_color=["lightskyblue", "yellow", "orangered"],
            ),
        )
    )

tl.render("test{}.html").format(i)
