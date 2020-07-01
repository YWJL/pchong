import asyncio
from aiohttp import TCPConnector, ClientSession
import json
import pyecharts.options as opts
from pyecharts.charts import Map,Line,Timeline
import pandas as pd
from pyecharts.commons.utils import JsCode
import os
import math
import csv
path='D:\Pchong\data_see\daily'
os.chdir(path)
with open('USA.json', 'r') as f:
    data=json.loads(f.read())
Pos_name='2020-06-04-1point3acres-us_state-confirmed-data.json.csv'
Dea_name='2020-06-04-1point3acres-us_state-death-data.json.csv'
name2='USA_population'
Population=pd.read_csv('D:/Pchong/data_see/data_all/US-population.csv')
US_Pos=pd.read_csv(Pos_name)
US_Dea=pd.read_csv(Dea_name)
NAME_MAP_DATA = {
    # "key": "value"
    # "name on the hong kong map": "name in the MAP DATA",
    "Alaska": "AS",
    "Alabama": "AL",
    "Arkansas": "AR",
    "Arizona": "AZ",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Washington.D.C": "DC",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Iowa": "IA",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Massachusetts": "MA",
    "Maryland": "MD",
    "Maine": "ME",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Missouri": "MO",
    "Mississippi": "MS",
    "Montana": "MT",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Nebraska": "NE",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "Nevada": "NV",
    "New York": "NY",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Virginia": "VA",
    "Vermont": "VT",
    "Washington": "WA",
    "Wisconsin": "WI",
    "West Virginia": "WV",
    "Wyoming": "WY",
    "Puerto Rico": "PR",
    "Guam": "GU",
    "AS": "AS",
    "Northern Mariana Islands": "MP",
}
time="截止至{}美国疫情数据".format(US_Pos.iloc[len(US_Pos)-1,0])
count=60
country=[]
Today_POS=[]
# print(US_Pos.iloc[len(US_Pos)-1,count-1])

for i in range(1,len(US_Pos)):
    for j in range(1,count):
            if type(US_Pos.iloc[i,j])!=str:
                if math.isnan(US_Pos.iloc[i,j]):
                    US_Pos.iloc[i,j]=0

for i in range(1,count):
    if US_Pos.iloc[0,i]!='US':
        country.append(US_Pos.iloc[0,i])
        Today_POS.append(float(US_Pos.iloc[len(US_Pos)-1,i]))
    if US_Pos.iloc[0,i]=='US':
        sum_today=int(float(US_Pos.iloc[len(US_Pos)-1,i]))
US_Today_Pos=[list(z) for z in zip(country,Today_POS)]
print(max(Today_POS))
print(US_Today_Pos)
(
    Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
    .add_js_funcs("echarts.registerMap('HK', {});".format(data))
        .add(
        series_name="Positive",
        data_pair=US_Today_Pos,
        maptype="HK",
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="美国至今确诊人数总和{}人".format(sum_today),
            subtitle=time,
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b}<br/>{c}",
        ),
        visualmap_opts=opts.VisualMapOpts(
            max_=max(Today_POS),
            range_text=["high", "low"],
            is_calculable=True,
        ),
    )
    .render("USA-20200604.html")
)

