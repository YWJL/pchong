from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Collector, Faker
from pyecharts.datasets import register_url
import pandas as pd
import asyncio
import math
from aiohttp import TCPConnector, ClientSession
import pyecharts.options as opts
from pyecharts.charts import Map
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from pyecharts import options as opts
from pyecharts.charts import Grid, Line, Scatter
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
from pyecharts.charts import Geo
import json
import os
path='D:\Pchong\可视化\daily'
os.chdir(path)
name='daily.csv'
US=pd.read_csv(name)
Date=pd.read_csv(name,usecols=[15])
state=pd.read_csv(name,usecols=[1])
positive=pd.read_csv(name,usecols=[2])
recovered=pd.read_csv(name,usecols=[11])
death=pd.read_csv(name,usecols=[16])
x=['positive','death','recovered']
print(Date.iloc[0,0])
tl = Timeline()
date=[]
day=int(len(state)/56)-18  #前26天数据代表性不强，不考虑
# day=day+4     #三天预测
print(day)
positive_all=[]
recovered_all=[]
death_all=[]
for i in range(day):
    num1=0
    num2=0
    num3=0
    a = Date.iloc[i*56, 0].split('T')
    a = a[0]
    a = a.split('-', 1)[1]
    for j in range(56):
        if math.isnan(positive.iloc[i*56+j,0]):
            positive.iloc[i*56+j,0]=0
        if math.isnan(recovered.iloc[i*56+j,0]):
            recovered.iloc[i*56+j,0]=0
        if math.isnan(death.iloc[i*56+j,0]):
            death.iloc[i*56+j,0]=0
        num1 =num1 + positive.iloc[i*56+j,0]
        num2 =num2 + recovered.iloc[i*56+j,0]
        num3 =num3 + death.iloc[i*56+j,0]
    positive_all.append(num1)
    recovered_all.append(num2)
    death_all.append(num3)
    date.append(a)
print('date',date)
DATE=[]   #逆序输出
POSITIVE_ALL=[]
RECOVERED_ALL=[]
DEATH_ALL=[]
# for i in range(3):
#     b = date[0].split('-')
#     b[1] = int(b[1]) + 1
#     date.insert(0,b[0]+'-'+str(b[1]))

for i in range(day):
    DATE.append(date[day-i-1])
    POSITIVE_ALL.append(positive_all[day-i-1])
    RECOVERED_ALL.append(recovered_all[day-i-1])
    DEATH_ALL.append(death_all[day-i-1])

b = date[0].split('-')
b[1] = int(b[1]) + 1
DATE.append(b[0]+'-'+str(b[1]))
print('POSITIVVE_ALL:',POSITIVE_ALL)
print('RECOVERED_ALL:',RECOVERED_ALL)
print('recovered_all:',recovered_all)
POSITIVE_ALL.insert(len(POSITIVE_ALL)-1,POSITIVE_ALL[len(POSITIVE_ALL)-1])
DEATH_ALL.insert(len(DEATH_ALL)-1,DEATH_ALL[len(DEATH_ALL)-1])

# if math.isnan(death.iloc[115,0]):
#     print(1)       把nan赋值0
#计算人数增长比
account_pos=[]
new_case=[]
for i in range(len(POSITIVE_ALL)-2):
    new_case.append(POSITIVE_ALL[i+1]-POSITIVE_ALL[i])
    account_pos.append((POSITIVE_ALL[i+1]-POSITIVE_ALL[i])/POSITIVE_ALL[i])

account_dea=[]
new_dea=[]
for i in range(len(POSITIVE_ALL)-2):
    new_dea.append(DEATH_ALL[i+1]-DEATH_ALL[i])
    account_dea.append((DEATH_ALL[i+1]-DEATH_ALL[i])/DEATH_ALL[i])

account_pos=0
account_dea=0
account_pos=sum(new_case)/sum(POSITIVE_ALL)
account_dea=sum(new_dea)/sum((DEATH_ALL))
account_pos='%.2f%%' % (account_pos * 100)
account_dea='%.2f%%' % (account_dea * 100)
# print(account_pos)
# print('account_dea:',account_dea)
# print('new_dea:',new_dea)
# print('account_pos:',account_pos)
# print('new_case:',new_case)
# print('DATE:',DATE)
#
#POSITIVE_situation
for i in range(len(date)-1):
    if new_case[i]==0:
        new_case[i]=1
    if new_dea[i]==0:
        new_dea[i]=1
# for i in range(len(date)):
#     POSITIVE_ALL[i]=math.log(POSITIVE_ALL[i])
#     new_case[i]=math.log(new_case[i])
#     DEATH_ALL[i]=math.log(DEATH_ALL[i])
#     RECOVERED_ALL[i]=math.log(RECOVERED_ALL[i])
#     new_dea[i]=math.log(new_dea[i])
for i in range(len(date)-1):
    if new_case[i]==0:
        new_case[i]=1
    if new_dea[i]==0:
        new_dea[i]=1
# POSITIVE_ALL[day]=math.log(POSITIVE_ALL[day])
# DEATH_ALL[day]=math.log(DEATH_ALL[day])
print('account_dea:',account_dea)
print('new_dea:',new_dea)
print('account_pos:',account_pos)
print('new_case:',new_case)
print('DATE:',DATE)
print('POSITIVVE_ALL:',POSITIVE_ALL)
print('RECOVERED_ALL:',RECOVERED_ALL)
print('recovered_all:',recovered_all)
print('DEATH_ALL:',DEATH_ALL)
new_recovered=[]  #当日治愈人数
for i in range(0,len(RECOVERED_ALL)-1):
    a=RECOVERED_ALL[i+1]-RECOVERED_ALL[i]
    if a<0:
        a=-a
    new_recovered.append(a)

time="截止至{}美国疫情数据".format(US.iloc[0,0])
print('new_recovered:',new_recovered)
print(RECOVERED_ALL[1])
print(RECOVERED_ALL[0])
POSITIVE_situation=(
    Line()
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Cases",
        y_axis=POSITIVE_ALL,
        yaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#CC6600'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Cases",
        y_axis=new_case,
        yaxis_index=1,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#379B9F'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="New Cases",
            name_location="end",
            type_="log",
            min_=10000,
            # max_=50000,
            position="right",
            # is_inverse=True,
            axistick_opts=opts.AxisTickOpts(is_show=False),
            splitline_opts=opts.SplitLineOpts(is_show=False),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Positive_situation", pos_left="23%",pos_top="top",),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),  #, axis_pointer_type="cross"
        legend_opts=opts.LegendOpts(pos_left="left"),
        datazoom_opts=[
        opts.DataZoomOpts(range_start=0, range_end=100,pos_bottom="49%",xaxis_index=0,type_="inside"),
        opts.DataZoomOpts(range_start=0, range_end=100, pos_bottom="49%", xaxis_index=1,type_="inside"),
        opts.DataZoomOpts(range_start=0, range_end=100, pos_bottom="49%", xaxis_index=2,type_="inside"),    
],
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="log",
            name="Cumularive Cases",
            min_=10000,
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
    # ).render("test1.html")
)
)

Death_situation=(
    Line()
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Deaths",
        y_axis=DEATH_ALL,
        xaxis_index=1,
        yaxis_index=2,
        symbol_size=10,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#AB2524'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Deaths",
        y_axis=new_dea,
        symbol_size=10,
        xaxis_index=1,
        yaxis_index=3,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#6B716F'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="New Deaths",
            name_location="end",
            type_="log",
            min_=100,
            # max_=50000,
            position="right",
            # is_inverse=True,
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Deaths_situation", pos_left="64%",pos_top="top",),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="78%",pos_top="top"),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="log",
            name="Cumularive Deaths",
            min_=1000,
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
    # ).render("test1.html")
)
)

#疫情情况折线图

Recovered_line=(
    Line()
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Recovered",
        y_axis=RECOVERED_ALL,
        xaxis_index=2,
        yaxis_index=4,
        symbol_size=10,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#AB2524'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Recovered",
        y_axis=new_recovered,
        symbol_size=10,
        xaxis_index=2,
        yaxis_index=5,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#6B716F'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="New Recovered",
            name_location="end",
            type_="log",
            min_=100,
            # max_=50000,
            position="right",
            # is_inverse=True,
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Recover_situation",subtitle=time, pos_left="center",pos_top="49%",),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="left",pos_top="49%"),
        datazoom_opts=[
        opts.DataZoomOpts(range_start=0, range_end=100, pos_bottom="49%", xaxis_index=1,type_="inside")],
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="log",
            name="Cumularive Recovered",
            min_=1000,
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
    # ).render("test1.html")
)
)


grid = (
    Grid(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add(POSITIVE_situation, grid_opts=opts.GridOpts(pos_right="55%",pos_bottom="55%"), is_control_axis_index=True)
    .add(Death_situation, grid_opts=opts.GridOpts(pos_left="55%",pos_bottom="55%"), is_control_axis_index=True)
    .add(Recovered_line, grid_opts=opts.GridOpts(pos_top="57%"), is_control_axis_index=True)
    .render("situation_log.html")
)