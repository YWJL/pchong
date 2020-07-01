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
async def get_json_data(url: str) -> dict:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url=url) as response:
            return await response.json()
Js_data = asyncio.run(
    get_json_data(url="https://coronavirus.1point3acres.com/resources/maps/us_map/GA.json")
)    #或者这样获取网页json
name='20200515-data.json.csv'
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
    Country.append(DATA.iloc[i+388,2])
    Pos.append(float(DATA.iloc[i+388,-1]))
    for j in range(0,len(data)):
        if DATA.iloc[i + 388, 2] ==data.iloc[j,0]:
            number.append(data.iloc[j, 1])
            number_cou.append(data.iloc[j,0])
MAP_data=[list(z) for z in zip(Country,Pos)]
Standard_num=[]          #GA州10W人口时，各县人口数
Posi=[]
Standard_data=[]
test1=[]
test2=[]
aaa1=[]
aaa2=[]
print('Country',Country)
print('number_cou',number_cou)
# account_pos='%.2f%%' % (account_pos * 100)
# account_dea='%.2f%%' % (account_dea * 100)
for i in range(0,len(number_cou)):
    for j in range(0,len(Country)):
        if number_cou[i]==Country[j]:
            test1.append(number_cou[i])
            test2.append(number[i])
            aaa1.append(Country[j])
            aaa2.append(Pos[j])
            Standard_num.append(int(100000*Pos[j]/number[i]))
Standard_data=[list(z) for z in zip(test1,Standard_num)]
bbb1=[list(z) for z in zip(test1,test2)]
bbb2=[list(z) for z in zip(aaa1,aaa2)]
print('bbb1',bbb1)
print('bbb2',bbb2)
print('MAP',MAP_data)
print('人口',bbb2[130])
print('感染',bbb1[130])
print(Standard_data)


ss1=[]
# for i in range(1,len(Standard_data)):
#     a = float(Pos[i] / number[i]) * 100000
#     ss1.append(a)
# print(max(ss1))
time="2020/{}".format(DATA.columns.values[-1])
(
    Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
    .add_js_funcs("echarts.registerMap('HK', {});".format(Js_data))
    .add(
        series_name="Georgia州疫情情况",
        maptype="HK",
        data_pair=Standard_data,
        # name_map=NAME_MAP_DATA,
        is_map_symbol_show=False,#红点标记
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Georgia州疫情情况",
            subtitle="各县人口数为100，000时，感染数,{}".format(time),
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b0}县{c0}人感染"#{a}<br/>:{c0}此为换行
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=min(Standard_num),
            max_=max(Standard_num),
            range_text=["High", "Low"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
        ),
    )
    .render("Standard-GA-100,000.html")
)


