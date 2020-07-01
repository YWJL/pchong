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
with open('GA.json', 'r') as f:
    Js_2data=json.loads(f.read())
name='20200522-data.json.csv'
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
    Country.append(DATA.iloc[i+388,2])
    Pos.append(float(DATA.iloc[i+388,-1]))
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
pos_account1=[]
pos_account3=[]
pos_account5=[]
pos_account7=[]
for i in range(1,144):
    Posi_1.append(float(DATA.iloc[i+388,-1]))
    Posi_2.append(float(DATA.iloc[i + 388, -2]))
    Posi_3.append(float((int(DATA.iloc[i+388,-1]))-int(DATA.iloc[i+388,-3]))/3/(int(DATA.iloc[i + 388, -1])))
    Posi_4.append(float(DATA.iloc[i + 388, -4]))
    Posi_5.append(float((int(DATA.iloc[i+388,-1]))-int(DATA.iloc[i+388,-5]))/5/(int(DATA.iloc[i + 388, -1])))
    Posi_6.append(float(DATA.iloc[i + 388, -6]))
    Posi_7.append(float((int(DATA.iloc[i+388,-1]))-int(DATA.iloc[i+388,-7]))/7/(int(DATA.iloc[i + 388, -1])))
    pos_account1.append(int(DATA.iloc[i+388,-1]))
    pos_account3.append(int(DATA.iloc[i+388,-3]))
    pos_account5.append(int(DATA.iloc[i+388,-5]))
    pos_account7.append(int(DATA.iloc[i+388,-7]))
account3=float((sum(pos_account1)-sum(pos_account3))/3/(sum(pos_account1)))
account5=(sum(pos_account1)-sum(pos_account5))/5/(sum(pos_account1))
account7=(sum(pos_account1)-sum(pos_account7))/7/(sum(pos_account1))
print(sum(pos_account1))
# account_pos='%.2f%%' % (account_pos * 100)
account3='%.2f%%' % (account3 * 100)
account5='%.2f%%' % (account5 * 100)
account7='%.2f%%' % (account7 * 100)
POS3=[]
POS5=[]
POS7=[]
num=[]
for i in range(0,143):
    a=Posi_3[i]*100
    POS3.append('%.4f' % a)
    b=Posi_5[i]*100
    POS5.append('%.4f' % b)
    c=Posi_7[i]*100
    POS7.append('%.4f' % c)
    num.append(a)
    num.append(b)
    num.append(c)

Standard_data_7=[list(z) for z in zip(Country,Posi_7)]
pos={}
pos[0]=[list(z) for z in zip(Country,Posi_1)]
pos[1]=[list(z) for z in zip(Country,Posi_2)]
pos[2]=[list(z) for z in zip(Country,POS3)]
pos[3]=[list(z) for z in zip(Country,Posi_4)]
pos[4]=[list(z) for z in zip(Country,POS5)]
pos[5]=[list(z) for z in zip(Country,Posi_6)]
pos[6]=[list(z) for z in zip(Country,POS7)]
print('Posi_7',Posi_7)
print(pos[6])
test3=[list(z) for z in zip(Country,Posi_3)]
test5=[list(z) for z in zip(Country,Posi_5)]
test7=[list(z) for z in zip(Country,Posi_7)]
print(test7)
print(float(DATA.iloc[387,-1])/(DATA.iloc[387, -7])-1)
print(DATA.iloc[389,2])
time="2020/{}Georgia疫情情况".format(DATA.columns.values[-1])
tl = Timeline()
i=1
a=0
a=(int(DATA.iloc[i+388,-1])+int(DATA.iloc[i+388,-2]))
# print(float((DATA.iloc[i+388,-1])+(DATA.iloc[i+388,-2])+(DATA.iloc[i+388,-3]))/(DATA.iloc[i + 388, -3]))
print(a)

map_ga = (
        Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
            .add_js_funcs("echarts.registerMap('GA', {});".format(Js_2data))
           .add(
            series_name="至{}天前确诊病例数".format(2+1),
            maptype="GA",
            data_pair=pos[2],
            # name_map=NAME_MAP_DATA,
            is_map_symbol_show=False,  # 红点标记
            # itemstyle_opts={Timeline
            #     },
        )
            .add(
            series_name="至{}天前确诊病例数".format(4+1),
            maptype="GA",
            data_pair=pos[4],
            # name_map=NAME_MAP_DATA,
            is_map_symbol_show=False,  # 红点标记
            # itemstyle_opts={Timeline
            #     },
        )
         .add(
            series_name="至{}天前确诊病例数".format(7),
            maptype="GA",
            data_pair=pos[6],
            # name_map=NAME_MAP_DATA,
            is_map_symbol_show=False,  # 红点标记
            # itemstyle_opts={Timeline
            #     },
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title=time,
                subtitle="近七天感染人数增长比:{}   近五天:{}  近三天:{}".format(account7,account5,account3),
                pos_top="4%",
                pos_left="45%"
            ),
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{b0}:{c0}%"  # {a}<br/>:{c0}此为换行
            ),
            visualmap_opts=opts.VisualMapOpts(
                min_=min(num),
                max_=max(num),
                range_text=["High", "Low"],
                is_calculable=True,
                range_color=["lightskyblue", "yellow", "orangered"],
            ),
        )
    .render("Georgia州近七天感染状况.html"))
# print(max(Posi_7))