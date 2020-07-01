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
path='D:\Pchong\可视化\learning'
os.chdir(path)

name='daily.csv'
US=pd.read_csv('D:\Pchong\可视化\learning\daily.csv',usecols=[0,1,2,11,16,15])    #如有报错可能是路径的问题
print(US)
day=int(len(US)/56)-18
print('疫情起始日期：',US.iloc[day*56,0],US.iloc[day*56,1])
positive_all=[]
recovered_all=[]
death_all=[]
DATE=[]
for i in range(day,0,-1):
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



POSITIVE_situation_log=(
    Line()
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Cases",
        y_axis=positive_all,
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
            type_="value",
            min_=10000,
            max_=40000,
            # max_=50000,
            position="right",
            # is_inverse=True,
            axistick_opts=opts.AxisTickOpts(is_show=False),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Positive_situation", pos_left="36%",pos_top="top",),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),  #, axis_pointer_type="cross"
        legend_opts=opts.LegendOpts(pos_left="left"),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="log",
            name="Cumularive Cases",
            min_=10000,
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
    # ).render("test1.html")
    ).render("log.html")
)
POSITIVE_situation_value=(
    Line()
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Cases",
        y_axis=positive_all,
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
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Positive_situation", pos_left="36%",pos_top="top",),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),  #, axis_pointer_type="cross"
        legend_opts=opts.LegendOpts(pos_left="left"),
        datazoom_opts=[
        opts.DataZoomOpts(range_start=0, range_end=100,pos_bottom="49%",xaxis_index=0,type_="inside"),
        opts.DataZoomOpts(range_start=0, range_end=100, pos_bottom="49%", xaxis_index=1,type_="inside"),
        opts.DataZoomOpts(range_start=0, range_end=100, pos_bottom="49%", xaxis_index=2,type_="inside"),    
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

Death_situation=(
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
grid = (
    Grid(init_opts=opts.InitOpts(width="1200px", height="800px"))
    .add(POSITIVE_situation_value, grid_opts=opts.GridOpts(pos_right="55%",pos_bottom="55%"), is_control_axis_index=True)
    .add(Death_situation, grid_opts=opts.GridOpts(pos_left="55%",pos_bottom="55%"), is_control_axis_index=True)
    # .add(Recovered_line, grid_opts=opts.GridOpts(pos_top="57%"), is_control_axis_index=True)
    .render("situation_log_test.html")
)

Death=(
    Line()
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Deaths",
        y_axis=death_all,
        xaxis_index=0,
        yaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#AB2524'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Deaths",
        y_axis=new_dea,
        # symbol_size=10,
        xaxis_index=0,
        yaxis_index=1,
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
        title_opts=opts.TitleOpts(title="Deaths_situation", pos_left="45%",pos_top="top",),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="68%",pos_top="top"),
        datazoom_opts=[
        opts.DataZoomOpts(range_start=0, range_end=100,pos_bottom="49%",xaxis_index=0,type_="inside"),],
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
).render("D:\Pchong\可视化\daily\death.html")
)

Recovered=(
    Line()
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Recovered",
        y_axis=recovered_all,
        xaxis_index=0,
        yaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#AB2524'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Recovered",
        y_axis=new_rec,
        # symbol_size=10,
        xaxis_index=0,
        yaxis_index=1,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#6B716F'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="New Deaths",
            name_location="end",
            type_="value",
            min_=0,
            max_=30000,
            # max_=50000,
            position="right",
            # is_inverse=True,
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Deaths_situation", pos_left="45%",pos_top="top",),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="68%",pos_top="top"),
        datazoom_opts=[
        opts.DataZoomOpts(range_start=0, range_end=100,pos_bottom="49%",xaxis_index=0,type_="inside"),],
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name="Cumularive Deaths",
            min_=0,
            max_=400000,
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
    # ).render("test1.html")
).render("D:\Pchong\可视化\daily\Recovered.html")

)