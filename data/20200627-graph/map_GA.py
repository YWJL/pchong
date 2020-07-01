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
name='2020-06-05-1point3acres-GA.json.csv'
name2='countycases-GA.csv'
data=pd.read_csv(name2)
DATA=pd.read_csv(name)
day=len(DATA.columns.values)-2
# print(DATA.columns.values[-1])#列名
# print(Positive)
number=[]
Country=[]
Pos=[]
Pos_3=[]
Pos_5=[]
Pos_7=[]
testt=[]
print(DATA.iloc[0,0])
print(data.iloc[0,0])
for i in range(0,len(data)):
    a=0
    for j in range(0,len(DATA)):
        # for k in range(0,len(Country)):
        #     if Country[k]==DATA.iloc[j,1]:
        #         del Country[k]
        if DATA.iloc[j,1]=='Mcduffie':
            DATA.iloc[j,1]='McDuffie'
        if DATA.iloc[j,1]=='Mcintosh':
            DATA.iloc[j,1]='McIntosh'
        if data.iloc[i,0]==DATA.iloc[j,1]:
            Country.append(DATA.iloc[j,1])
            Pos.append(float(DATA.iloc[j,-1]))
            Pos_3.append(float(DATA.iloc[j,-3]))
            Pos_5.append(float(DATA.iloc[j,-5]))
            Pos_7.append(float(DATA.iloc[j,-7]))
            a=a+1
    if a>1:
        del Country[-1]
        del Pos[-1]
        del Pos_3[-1]
        del Pos_5[-1]
        del Pos_7[-1]
print('Pos',len(Pos))
print('Country',len(Country))
# for i in range(0,len(DATA)):
#     for j in range(i+1,len(DATA)):
#         if DATA.iloc[i,1]==DATA.iloc[j,1]:
#             DATA.iloc[j,1]=DATA.iloc[j,1]+'x'

# for i in range(0,len(Country)):
#     a=0
#     for j in range(0,len(DATA)):
#         if Country[i]==DATA.iloc[j,1]:
#             Pos.append(float(DATA.iloc[j,-1]))
#             Pos_3.append(float(DATA.iloc[j,-3]))
#             Pos_5.append(float(DATA.iloc[j,-5]))
#             Pos_7.append(float(DATA.iloc[j,-7]))
#             testt.append(DATA.iloc[j,1])
#             a=a+1
#     if a>1:
#         del Pos[-1]
#         del Pos_3[-1]
#         del Pos_5[-1]
#         del Pos_7[-1]
# print('testt',len(testt))
print('Country',len(Country))
for i in range(0,len(testt)):
    for j in range(i+1,len(testt)):
        if testt[i]==testt[j]:
            print(testt[i],i)
number_cou=[]
for j in range(0,len(Country)):
    for i in range(0,len(data)):
        if Country[j]==data.iloc[i,0]:
            number.append(data.iloc[i,1])
            number_cou.append(data.iloc[i,0])
print(len(number))
# print('Country:',Country)
# print('data:',len(data))
# print('Pos:',Pos)
# print('Number_cou:',number_cou)
# print('Number—cou:',len(number))
for i in range(0,len(number)):
    if Country[i]!=number_cou[i]:
        print('111',i)
Stand_Pos=[]
num=0
P3=[]
P5=[]
P7=[]
print(len(Pos))
print(Pos)
print(len(number))
for i in range(0,len(Pos)):
    num=Pos[i]/number[i]*100000
    Stand_Pos.append(int(num))
Stand_POS=[list(z) for z in zip(Country,Stand_Pos)]
for i in range(0,len(Pos)):
    if Pos[i]==0:
        P3.append(0)
        P5.append(0)
        P7.append(0)
    if Pos[i]!=0:
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
title_GA_num="2020/{}Georgia感染增加数（设各县感染人数均为10万人。）".format(DATA.columns.values[-1])
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
    .render("GA-20200601.html")
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
            subtitle="{}，各县每10万人口的平均感染人数".format(time),
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
            series_name="{}天内确诊病例数".format(2+1),
            maptype="GA",
            data_pair=POS_3,
            # name_map=NAME_MAP_DATA,
            is_map_symbol_show=False,  # 红点标记
            # itemstyle_opts={Timeline
            #     },
        )
            .add(
            series_name="{}天内确诊病例数".format(4+1),
            maptype="GA",
            data_pair=POS_5,
            # name_map=NAME_MAP_DATA,
            is_map_symbol_show=False,  # 红点标记
            # itemstyle_opts={Timeline
            #     },
        )
         .add(
            series_name="{}天内确诊病例数".format(7),
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
                subtitle="近七天感染人数增长比:{}   近五天:{}  近三天:{}  在这种情况下，若各县近3天实际确诊人数增长比为10%，则图中近3天增长人数为1万人".format(account7,account5,account3),
                pos_top="4%",
                pos_left="20%"
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





























































