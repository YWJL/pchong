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
async def get_json_data(url: str) -> dict:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url=url) as response:
            return await response.json()
path='D:\Pchong\data_see\learning'
os.chdir(path)
name1='daily.csv'
name2='20200527-data.json.csv'
name3='20200527-world-confirm-data.json.csv'
name4='20200527-world-death-data.json.csv'
daily_country=pd.read_csv(name3)
daily_country_name=['China','US','World','Australia','Russia','Germany','Brazil','India']
US=pd.read_csv(name1,usecols=[0,1,2,11,16,15])    #如有报错可能是路径的问题
print(US)
day=int(len(US)/56)-18
print('疫情起始日期：',US.iloc[day*56,0],US.iloc[day*56,1])
positive_all=[]
recovered_all=[]
death_all=[]
DATE=[]
for i in range(day,-1,-1):
    num1=0
    num2=0
    num3=0
    a = US.iloc[i*56, 4].split('T')
    a = a[0]
    a = a.split('-', 1)[1]
    for j in range(56):
        if math.isnan(US.iloc[i*56+j,2]):
            US.iloc[i*56+j,2]=0
        if math.isnan(US.iloc[i*56+j,3]):
            US.iloc[i*56+j,3]=0
        if math.isnan(US.iloc[i*56+j,5]):
            US.iloc[i*56+j,5]=0
        num1 =num1 + US.iloc[i*56+j,2]
        num2 =num2 + US.iloc[i*56+j,3]
        num3 =num3 + US.iloc[i*56+j,5]
    positive_all.append(num1)
    recovered_all.append(num2)
    death_all.append(num3)
    DATE.append(a)
print('DATE:',DATE)       #获取规范日期
print('POS:',positive_all)  #获取截至当天感染总数
print('REC:',recovered_all)   #获取截至当天治愈总数
print('DEA:',death_all)   #获取截至当天死亡总数
new_case=[]
new_dea=[]
new_rec=[]
account_pos=[]
account_dea=[]
account_rec=[]
for i in range(len(positive_all)-2):
    new_case.append(positive_all[i+1]-positive_all[i])
    new_rec.append(recovered_all[i+1]-recovered_all[i])
    new_dea.append(death_all[i+1]-death_all[i])
    account_dea.append((death_all[i+1]-death_all[i])/death_all[i+1])
STATE=[]
US_pos=[]
US_Dea=[]
US_Rec=[]
past_US_pos=[]
past_US_Dea=[]
past_US_Rec=[]
past_day=56*7 #7天前
past_3_day=56*3 #3天前
past_5_day=56*5 #5天前
POSITIVE_NUMBER=[]
rate_3days=[]
rate_5days=[]
rate_7days=[]
#计算今天的数据
for i in range(0,56):
    if math.isnan(US.iloc[i,2]):
        US.iloc[i, 2]=0
    if math.isnan(US.iloc[i, 5]):
        US.iloc[i, 5]=0
    if math.isnan(US.iloc[i, 3]):
        US.iloc[i,3]=0
    STATE.append(US.iloc[i,1])
    US_pos.append(US.iloc[i, 2])
    US_Dea.append(US.iloc[i, 5])
    US_Rec.append(US.iloc[i, 3])
MAP_Pos=[list(z) for z in zip(STATE,US_pos)]
MAP_Dea=[list(z) for z in zip(STATE,US_Dea)]
MAP_Rec=[list(z) for z in zip(STATE,US_Rec)]
#计算一周前的数据
for i in range(past_day,past_day+56):
    if math.isnan(US.iloc[i,2]):
        US.iloc[i, 2]=0
    if math.isnan(US.iloc[i, 5]):
        US.iloc[i, 5]=0
    if math.isnan(US.iloc[i, 3]):
        US.iloc[i,3]=0
    past_US_pos.append(US.iloc[i, 2])
    past_US_Dea.append(US.iloc[i, 5])
    past_US_Rec.append(US.iloc[i, 3])
test1=[list(z) for z in zip(STATE,past_US_Rec)]
#计算近七天疫情确诊人数的增长速率
for i in range(0,56):
    if math.isnan(US.iloc[i,2]):
        a=0
        rate_3days.append('%.4f' % a)
        rate_5days.append('%.4f' % a)
        rate_7days.append('%.4f' % a)
    a=(US.iloc[i,2]-US.iloc[i+past_3_day,2])/3/US.iloc[i,2]*100
    rate_3days.append('%.4f' % a)
    b=(US.iloc[i,2]-US.iloc[i+past_5_day,2])/5/US.iloc[i,2]*100
    rate_5days.append('%.4f' % b)
    c=(US.iloc[i,2]-US.iloc[i+past_day,2])/7/US.iloc[i,2]*100
    rate_7days.append('%.4f' % c)


#国家对比
date=[]
China=[]
USA=[]
World=[]
Australia=[]
Russia=[]
Germany=[]
Brazil=[]
India=[]
for i in range(3,len(daily_country)-1):
    date.append(daily_country.iloc[i,0])
    if math.isnan(float(daily_country.iloc[i,30])):
        daily_country.iloc[i,30]=0
        daily_country.iloc[i+1,30]=0
    if math.isnan(float(daily_country.iloc[i,145])):
        daily_country.iloc[i,145]=0
        daily_country.iloc[i+1,145]=0
    if math.isnan(float(daily_country.iloc[i,155])):
        daily_country.iloc[i,155]=0
        daily_country.iloc[i+1,155]=0
    if math.isnan(float(daily_country.iloc[i,7])):
        daily_country.iloc[i,7]=0
        daily_country.iloc[i+1,7]=0
    if math.isnan(float(daily_country.iloc[i,118])):
        daily_country.iloc[i,118]=0
        daily_country.iloc[i+1,118]=0
    if math.isnan(float(daily_country.iloc[i,18])):
        daily_country.iloc[i,18]=0
        daily_country.iloc[i+1,18]=0
    if math.isnan(float(daily_country.iloc[i,65])):
        daily_country.iloc[i,65]=0
        daily_country.iloc[i+1,65]=0
    if math.isnan(float(daily_country.iloc[i,53])):
        daily_country.iloc[i,53]=0
        daily_country.iloc[i+1,53]=0
    China.append(float(daily_country.iloc[i+1,30])-float(daily_country.iloc[i,30]))
    USA.append(float(daily_country.iloc[i+1,145])-float(daily_country.iloc[i,145]))
    World.append(float(daily_country.iloc[i+1,155])-float(daily_country.iloc[i,155]))
    Australia.append(float(daily_country.iloc[i+1,7])-float(daily_country.iloc[i,7]))
    Russia.append(float(daily_country.iloc[i+1,118])-float(daily_country.iloc[i,118]))
    Germany.append(float(daily_country.iloc[i+1,53])-float(daily_country.iloc[i,53]))
    Brazil.append(float(daily_country.iloc[i+1,18])-float(daily_country.iloc[i,18]))
    India.append(float(daily_country.iloc[i+1,65])-float(daily_country.iloc[i,65]))


Combine_Pos_log=(
    Line()
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Cases",
        y_axis=positive_all,
        yaxis_index=0,
        xaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#CC6600'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Cases",
        y_axis=new_case,
        yaxis_index=1,
        xaxis_index=0,
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
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Positive_situation", pos_left="25%",pos_top="top",),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),  #, axis_pointer_type="cross"
        legend_opts=opts.LegendOpts(pos_left="left"),
        datazoom_opts=[
        opts.DataZoomOpts(range_start=0, range_end=100,pos_bottom="49%",xaxis_index=0,type_="inside"),
        opts.DataZoomOpts(range_start=0, range_end=100, pos_bottom="49%", xaxis_index=1,type_="inside"),
        opts.DataZoomOpts(range_start=0, range_end=100, pos_bottom="49%", xaxis_index=2,type_="inside"),  
        opts.DataZoomOpts(range_start=0, range_end=100, pos_bottom="49%", xaxis_index=3,type_="inside"),   
        opts.DataZoomOpts(range_start=0, range_end=100, pos_bottom="49%", xaxis_index=4,type_="inside"),     
],
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name="Cumularive Cases",
            min_=10000,
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
    # ).render("test1.html")
    )
)
Combine_DEA=(
    Line()
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Deaths",
        y_axis=death_all,
        xaxis_index=1,
        yaxis_index=2,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#AB2524'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Deaths",
        y_axis=new_dea,
        # symbol_size=10,
        xaxis_index=1,
        yaxis_index=3,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#6B716F'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="New Deaths",
            name_location="end",
            type_="value",
            min_=0,
            max_=7000,
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
            type_="value",
            name="Cumularive Deaths",
            min_=0,
            max_=100000,
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
    # ).render("test1.html")
)
)

Combine_Pos_value=(
    Line()
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Cases",
        y_axis=positive_all,
        xaxis_index=2,
        yaxis_index=4,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#AB2524'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Cases",
        y_axis=new_case,
        # symbol_size=10,
        xaxis_index=2,
        yaxis_index=5,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#6B716F'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="New Cases",
            name_location="end",
            type_="value",
            # min_=0,
            # max_=70000,
            # max_=50000,
            position="right",
            # is_inverse=True,
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="POS_value", pos_left="20%",pos_top="33%",),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="20%",pos_top="37%"),
        # datazoom_opts=[
        # opts.DataZoomOpts(range_start=0, range_end=100,pos_bottom="49%",xaxis_index=0,type_="inside"),],
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
Country_US=(
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=STATE)
    .add_yaxis(
        series_name="近7天",
        xaxis_index=3,
        yaxis_index=6,
        y_axis=rate_7days,  #[item[1] for item in ACC_3DAYS]
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
            ]
        ),
        label_opts=opts.LabelOpts(is_show=False),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="美国近一周疫情情况",pos_top="33%",pos_left="52%",subtitle="各州疫情确诊人数的增长速率"),
        tooltip_opts=opts.TooltipOpts(trigger="axis",formatter="{c}%"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        legend_opts=opts.LegendOpts(pos_left="80%",pos_top="40%"),
        datazoom_opts=[
        opts.DataZoomOpts(yaxis_index=0),
        opts.DataZoomOpts(type_="inside", yaxis_index=0),
        ],
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            # type_="value",
            # name="Cumularive Cases",
            # min_=10000,
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
        # xaxis_opts=opts.AxisOpts(type_="category", boundary
        # _gap=False),
    )
    # .render("D:/Pchong/data_see/html_all/美国各州近一周来疫情增长速度.html")
)

POSITIVE_situation=(
    Line()
    .add_xaxis(xaxis_data=date)
    .add_yaxis(
        series_name="China",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=China,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#CC6600'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="US",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=USA,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#379B9F'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="Russia",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=Russia,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False,color='#FF7F00'),
    )
    .add_yaxis(
        series_name="World",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=World,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False,color='#FF0000'),
    )
    .add_yaxis(
        series_name="Australia",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=Australia,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False,color='#FFFF00'),
    )
    .add_yaxis(
        series_name="Brazil",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=Brazil,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False,color='#00FF00'),
    )
    .add_yaxis(
        series_name="Germany",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=Germany,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False,color='#00FFFF'),
    )
    .add_yaxis(
        series_name="India",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=India,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False,color=' #0000FF'),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各国新增确诊人数",pos_top="63%",pos_left="40%"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),  #, axis_pointer_type="cross"
        legend_opts=opts.LegendOpts(pos_top="66%",pos_left="20%"),
        datazoom_opts=[
        opts.DataZoomOpts(range_start=0, range_end=100,xaxis_index=0),
],
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="log",
            # name="Cumularive Cases",
            min_=1,
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
    # ).render("test1.html")
)#.render("D:/Pchong/data_see/html_all/Country_daily.html")
)

grid = (
    Grid(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add(Combine_Pos_log, grid_opts=opts.GridOpts(pos_right="55%",pos_top="5%",pos_bottom="70%"), is_control_axis_index=True)
    .add(Combine_DEA, grid_opts=opts.GridOpts(pos_left="55%",pos_top="5%",pos_bottom="70%"), is_control_axis_index=True)
    .add(Combine_Pos_value, grid_opts=opts.GridOpts(pos_right="55%",pos_top="40%",pos_bottom="40%"), is_control_axis_index=True)
    .add(Country_US, grid_opts=opts.GridOpts(pos_left="55%",pos_top="40%",pos_bottom="40%"), is_control_axis_index=True)
    .add(POSITIVE_situation, grid_opts=opts.GridOpts(pos_top="67%"), is_control_axis_index=True)
    .render("combine_line.html")
)

