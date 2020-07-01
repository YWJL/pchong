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
async def get_json_data(url: str) -> dict:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url=url) as response:
            return await response.json()

Js_data = asyncio.run(
    get_json_data(url="https://coronavirus.1point3acres.com/resources/maps/us_map/GA.json")
)    #或者这样获取网页json
name='20200527-data.json.csv'
name2='countycases-GA.csv'
data=pd.read_csv(name2)
DATA=pd.read_csv(name)
day=len(DATA.columns.values)-3
# print(DATA.columns.values[-1])#列名
# print(Positive)
print(DATA.iloc[0,0])
number=[]
Country=[]
Pos=[]
Pos_3=[]
Pos_5=[]
Pos_7=[]
print(DATA)
data_num=[2420,2417,2511,3026,2636,3055,2550,2418,2592,2788,2814,2385,2419,2619,2357,2620,2591]
for i in range(391,477):
    Country.append(DATA.iloc[i,2])
    Pos.append(float(DATA.iloc[i,-1]))
    Pos_3.append(float(DATA.iloc[i,-3]))
    Pos_5.append(float(DATA.iloc[i,-5]))
    Pos_7.append(float(DATA.iloc[i,-7]))
for i in range(479,534):
    Country.append(DATA.iloc[i,2])
    Pos.append(float(DATA.iloc[i,-1]))
    Pos_3.append(float(DATA.iloc[i,-3]))
    Pos_5.append(float(DATA.iloc[i,-5]))
    Pos_7.append(float(DATA.iloc[i,-7]))
Country.append('McIntosh')
Pos.append(float(DATA.iloc[478,-1]))
Pos_3.append(float(DATA.iloc[478,-1]))
Pos_5.append(float(DATA.iloc[478,-1]))
Pos_7.append(float(DATA.iloc[478,-1]))
Country.append('McDuffie')
Pos.append(float(DATA.iloc[477,-1]))
Pos_3.append(float(DATA.iloc[477,-1]))
Pos_5.append(float(DATA.iloc[477,-1]))
Pos_7.append(float(DATA.iloc[477,-1]))
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

for i in range(0,len(data_num)):
    Pos_3.append(float(DATA.iloc[data_num[i],-3]))
    Pos_5.append(float(DATA.iloc[data_num[i],-5]))
    Pos_7.append(float(DATA.iloc[data_num[i],-7]))
print(Pos_3)

number_cou=[]
for j in range(0,len(Country)):
    for i in range(0,len(data)):
        if Country[j]==data.iloc[i,0]:
            number.append(data.iloc[i,1])
            number_cou.append(data.iloc[i,0])

# print('Country:',Country)
# print('data:',len(data))
# print('Pos:',Pos)
# print('Number_cou:',number_cou)
# print('Number—cou:',len(number))
del Country[125]
del Pos[125]
del Pos_3[125]
del Pos_5[125]
del Pos_7[125]
for i in range(0,len(number)):
    if Country[i]!=number_cou[i]:
        print(i)
Stand_Pos=[]
num=0
P3=[]
P5=[]
P7=[]
for i in range(0,len(Pos)):
    num=Pos[i]/number[i]*100000
    Stand_Pos.append(int(num))
Stand_POS=[list(z) for z in zip(Country,Stand_Pos)]
for i in range(0,len(Pos)):
    P3.append(int((Pos[i]-Pos_3[i])/3/Pos[i]*100000))
    P5.append(int((Pos[i]-Pos_5[i])/5/Pos[i]*100000))
    P7.append(int((Pos[i]-Pos_7[i])/7/Pos[i]*100000))
MAX=[]
for i in range(0,len(Pos)):
    if P3[i]<0:
        P3[i]=-1
    if P5[i]<0:
        P5[i]=-1
    if P7[i]<0:
        P7[i]=-1
    MAX.append(P3[i])
    MAX.append(P5[i])
    MAX.append(P7[i])
    

account3=float((sum(Pos)-sum(Pos_3))/3/sum(Pos))
account5=float((sum(Pos)-sum(Pos_5))/5/sum(Pos))
account7=float((sum(Pos)-sum(Pos_7))/7/sum(Pos))
account3='%.2f%%' % (account3 * 100)
account5='%.2f%%' % (account5 * 100)
account7='%.2f%%' % (account7 * 100)
POS=[list(z) for z in zip(Country,Pos)]
POS_3=[list(z) for z in zip(Country,P3)]
POS_5=[list(z) for z in zip(Country,P5)]
POS_7=[list(z) for z in zip(Country,P7)]
print('POS:',POS)
print('stand:',Stand_POS)
time="2020/{}".format(DATA.columns.values[-1])
title_GA_num="2020/{}Georgia感染增加数（设定各县当天感染人数均达到100,000人）".format(DATA.columns.values[-1])
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
    .render("GA-20200527.html")
)
(
    Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
    .add_js_funcs("echarts.registerMap('HK', {});".format(Js_data))
    .add(
        series_name="Georgia州疫情情况",
        maptype="HK",
        data_pair=Stand_POS,
        # name_map=NAME_MAP_DATA,
        is_map_symbol_show=False,#红点标记
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Georgia州疫情情况",
            subtitle="{}，若各县人口数为100，000时，各县市的感染数".format(time),
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b}县{c}人感染"#{a}<br/>:{c0}此为换行
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=min(Stand_Pos),
            max_=max(Stand_Pos),
            range_text=["High", "Low"],
            is_calculable=True,
            # range_color=["lightskyblue", "yellow", "orangered"],
        ),
    )
    .render("GA-100000.html")
)

map_ga = (
        Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
            .add_js_funcs("echarts.registerMap('GA', {});".format(Js_data))
           .add(
            series_name="至{}天前确诊病例数".format(2+1),
            maptype="GA",
            data_pair=POS_3,
            # name_map=NAME_MAP_DATA,
            is_map_symbol_show=False,  # 红点标记
            # itemstyle_opts={Timeline
            #     },
        )
            .add(
            series_name="至{}天前确诊病例数".format(4+1),
            maptype="GA",
            data_pair=POS_5,
            # name_map=NAME_MAP_DATA,
            is_map_symbol_show=False,  # 红点标记
            # itemstyle_opts={Timeline
            #     },
        )
         .add(
            series_name="至{}天前确诊病例数".format(7),
            maptype="GA",
            data_pair=POS_7,
            # name_map=NAME_MAP_DATA,
            is_map_symbol_show=False,  # 红点标记
            # itemstyle_opts={Timeline
            #     },
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title=title_GA_num,
                subtitle="近七天感染人数增长比:{}   近五天:{}  近三天:{}".format(account7,account5,account3),
                pos_top="4%",
                pos_left="45%"
            ),
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{b0}:{c0}"  # {a}<br/>:{c0}此为换行
            ),
            visualmap_opts=opts.VisualMapOpts(
                min_=min(MAX),
                max_=max(MAX),
                range_text=["High", "Low"],
                is_calculable=True,
                # range_color=["lightskyblue", "yellow", "orangered"],
            ),
        )
    .render("Georgia州近七天感染状况.html"))
""""""











































# test1=[] 
# test2=[]
# print(data.iloc[len(data)-1,0])
# for i in range(0,len(data)):
#     test1.append(data.iloc[i,0])
#     test2.append(float(data.iloc[i,2]))
# test3=[list(z) for z in zip(test1,test2)]
# print('test3:',test3)

















