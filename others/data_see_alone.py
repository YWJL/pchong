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
Date=pd.read_csv('daily.csv',usecols=[13])
state=pd.read_csv('daily.csv',usecols=[1])
positive=pd.read_csv('daily.csv',usecols=[2])
recovered=pd.read_csv('daily.csv',usecols=[11])
death=pd.read_csv('daily.csv',usecols=[14])
x=['positive','death','recovered']
tl = Timeline()
date=[]
day=int(len(state)/56)-26  #前26天数据代表性不强，不考虑
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
    for j in range(55):
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
for i in range(len(POSITIVE_ALL)-1):
    new_case.append(POSITIVE_ALL[i+1]-POSITIVE_ALL[i])
    account_pos.append((POSITIVE_ALL[i+1]-POSITIVE_ALL[i])/POSITIVE_ALL[i])

account_dea=[]
new_dea=[]
for i in range(len(POSITIVE_ALL)-1):
    new_dea.append(DEATH_ALL[i+1]-DEATH_ALL[i])
    account_dea.append((DEATH_ALL[i+1]-DEATH_ALL[i])/DEATH_ALL[i])
new_dea.append(0)
new_case.append(0)

account_pos=0
account_dea=0
account_pos=sum(new_case)/sum(POSITIVE_ALL)
account_dea=sum(new_dea)/sum((DEATH_ALL))
account_pos='%.2f%%' % (account_pos * 100)
account_dea='%.2f%%' % (account_dea * 100)
print(account_pos)
print('account_dea:',account_dea)
print('new_dea:',new_dea)
print('account_pos:',account_pos)
print('new_case:',new_case)
print('DATE:',DATE)

#时间轴（柱状图）
for i in range(day):
    situation= []
    situation.append(positive_all[day-i-1])
    situation.append(recovered_all[day - i - 1])
    situation.append(death_all[day - i - 1])
    bar = (
        Bar()
        .add_xaxis(x)
        .add_yaxis("新型冠状病毒当日情况", situation)
        .set_global_opts(
            title_opts=opts.TitleOpts("4月{}日病毒感染情况 - With Graphic 组件".format(i+1)),
            graphic_opts=[
                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(
                        rotation=JsCode("Math.PI / 4"),
                        bounding="raw",
                        right=100,
                        bottom=110,
                        z=100,
                    ),
                    children=[
                        opts.GraphicRect(
                            graphic_item=opts.GraphicItem(
                                left="center", top="center", z=100
                            ),
                            graphic_shape_opts=opts.GraphicShapeOpts(            #有关水印？
                                width=400, height=50
                            ),
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                fill="rgba(0,0,0,0.3)"
                            ),
                        ),
                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(
                                left="center", top="center", z=100
                            ),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                text="4月{}日病毒感染情况".format(i+1),
                                font="bold 26px Microsoft YaHei",
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                    fill="#fff"
                                ),
                            ),
                        ),
                    ],
                )
            ],
        )
    )
    tl.add(bar, "4月{}日".format(i+1))
tl.render("病毒情况（时间轴）.html")
print(situation)

#疫情情况折线图

Situation_line=(
    Line()#init_opts=opts.InitOpts(width="1680px", height="800px")
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="positive",
        y_axis=POSITIVE_ALL,
        linestyle_opts=opts.LineStyleOpts(type_='dashed'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="recovered",
        y_axis=RECOVERED_ALL,
        yaxis_index=1,
        linestyle_opts=opts.LineStyleOpts(width=3), #粗线，颜色可在这设置
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="recovered",
            name_location="start",
            type_="value",
            max_=100000,
            is_inverse=True,
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="美国疫情情况",
            subtitle="数据均为截至到当日时感染（治愈）人数",
            pos_left="center",
            pos_top="top",
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        datazoom_opts=[
            opts.DataZoomOpts(range_start=0, range_end=100),
            opts.DataZoomOpts(type_="inside", range_start=0, range_end=100),
        ],
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        yaxis_opts=opts.AxisOpts(name="positive", type_="value", max_=1100000),
    )
    .set_series_opts(
        markarea_opts=opts.MarkAreaOpts(
            is_silent=False,
            data=[
                opts.MarkAreaItem(
                    name="recovered",
                    x=("2009/9/12-7:00", "2009/9/22-7:00"),
                    label_opts=opts.LabelOpts(is_show=False),
                    itemstyle_opts=opts.ItemStyleOpts(color="#DCA3A2", opacity=0.5),
                ),
                opts.MarkAreaItem(
                    name="positive",
                    x=("2009/9/10-7:00", "2009/9/20-7:00"),
                    label_opts=opts.LabelOpts(is_show=False),
                    itemstyle_opts=opts.ItemStyleOpts(color="#A1A9AF", opacity=0.5),
                ),
            ],
        ),
        axisline_opts=opts.AxisLineOpts(),
    )
    # .render("疫情情况（折线图）.html")
)
#POSITIVE_situation

POSITIVE_situation=(
    Line()#init_opts=opts.InitOpts(width="1680px", height="800px")
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Cases",
        y_axis=POSITIVE_ALL,
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
            name_location="start",
            type_="value",
            max_=50000,
            is_inverse=True,
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Positive_situation",
            subtitle="Growth rate:{}".format(account_pos),
            pos_left="center",
            pos_top="top",
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        datazoom_opts=[
            opts.DataZoomOpts(range_start=0, range_end=100),
            opts.DataZoomOpts(type_="inside", range_start=0, range_end=100),
        ],
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        yaxis_opts=opts.AxisOpts(name="Cumulative Cases", type_="value", max_=1100000),
    )
    .set_series_opts(
        markarea_opts=opts.MarkAreaOpts(
            is_silent=False,
            data=[
                opts.MarkAreaItem(
                    name="New Cases",
                    x=("2009/9/12-7:00", "2009/9/22-7:00"),
                    label_opts=opts.LabelOpts(is_show=False),
                    itemstyle_opts=opts.ItemStyleOpts(color="#DCA3A2", opacity=0.5),
                ),
                opts.MarkAreaItem(
                    name="Cumulative Cases",
                    x=("2009/9/10-7:00", "2009/9/20-7:00"),
                    label_opts=opts.LabelOpts(is_show=False),
                    itemstyle_opts=opts.ItemStyleOpts(color="#A1A9AF", opacity=0.5),
                ),
                # opts.GraphicText(
                #     graphic_item=opts.GraphicItem(
                #         left="center",top="center",z=100
                #     ),
                #     graphic_textstyle_opts=opts.GraphicBasicStyleOpts(
                #         text="1",
                #         font="2",
                #         graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                #             fill='#fff'
                #         ),
                #     ),
                # ),
            ],
        ),
        axisline_opts=opts.AxisLineOpts(),
    )
    # .render("Positive_situation.html")
)
#death
Death_situation=(
    Line()#init_opts=opts.InitOpts(width="1680px", height="800px")
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Deaths",
        y_axis=DEATH_ALL,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#AB2524'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Deaths",
        y_axis=new_dea,
        yaxis_index=1,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#6B716F'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="New Deaths",
            name_location="start",
            type_="value",
            max_=5000,
            is_inverse=True,
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Deaths_situation",
            subtitle="Growthing rate:{}".format(account_dea),

            pos_left="center",
            pos_top="top",
        ),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        datazoom_opts=[
            # opts.DataZoomOpts(range_start=0, range_end=100),
            # opts.DataZoomOpts(type_="inside", range_start=0, range_end=100),
        ],
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
        yaxis_opts=opts.AxisOpts(name="Cumulative Deaths", type_="value", max_=110000),
    )
    .set_series_opts(
        markarea_opts=opts.MarkAreaOpts(
            is_silent=False,
            data=[
                opts.MarkAreaItem(
                    name="New Deaths",
                    x=("2009/9/12-7:00", "2009/9/22-7:00"),
                    label_opts=opts.LabelOpts(is_show=False),
                    itemstyle_opts=opts.ItemStyleOpts(color="#DCA3A2", opacity=0.5),
                ),
                # opts.MarkAreaItem(
                #     name="Cumulative Deaths",
                #     x=("2009/9/10-7:00", "2009/9/20-7:00"),
                #     label_opts=opts.LabelOpts(is_show=False),
                #     itemstyle_opts=opts.ItemStyleOpts(color="#A1A9AF", opacity=0.5),
                # ),
            ],
        ),
        axisline_opts=opts.AxisLineOpts(),
    )
    # .render("Fatality_situation.html")
)
grid = (
    Grid(init_opts=opts.InitOpts(width="1200px", height="800px"))
    # .add(POSITIVE_situation, grid_opts=opts.GridOpts(pos_left="10%",pos_bottom="70%",pos_right="60%"))
    .add(Death_situation, grid_opts=opts.GridOpts(pos_left="60%",pos_bottom="70%"))
    .render("grid_horizontal.html")
)






#        tooltip_opts=opts.TooltipOpts(is_show=True)   x轴标注