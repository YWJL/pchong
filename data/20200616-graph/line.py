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
name1 = 'D:/Pchong/data_see/data/20200619-data/2020-06-19-1point3acres-us_state-confirmed-data.json.csv'
name2 = 'D:/Pchong/data_see/data/20200619-data/2020-06-19-1point3acres-us_state-death-data.json.csv'
name3 = 'D:/Pchong/data_see/data_all/20200619-world-confirm-data.json.csv'
daily_country = pd.read_csv(name3)
daily_country_name = ['China', 'US', 'World',
                      'Australia', 'Russia', 'Germany', 'Brazil', 'India']
US_POS = pd.read_csv(name1)  # 如有报错可能是路径的问题
US_DEA = pd.read_csv(name2)
day_pos_begin = 9
day_pos_end = len(US_POS)
day_dea_end = len(US_DEA)
positive_all = []
death_all = []
DATE = []
STATE = []
print(US_POS.iloc[day_pos_end-1, 0])
print(US_POS.iloc[day_pos_begin, 0])
print(US_DEA.iloc[0, 0])
print(US_DEA.columns.values[1])
count = 60
for i in range(1, count):
    if US_POS.columns.values[i] != 'US':
        STATE.append(US_POS.columns.values[i])
    if US_POS.columns.values[i] == 'US':
        for j in range(day_pos_begin, day_pos_end):
            positive_all.append(float(US_POS.iloc[j, i]))
            US_POS.iloc[j, i] = 0
            US_DEA.iloc[j-day_pos_begin, i] = 0
            DATE.append(US_POS.iloc[j, 0])
for i in range(0, day_dea_end):
    a = 0
    for j in range(1, count):
        if type(US_DEA.iloc[i, j]) != str:
            if math.isnan(US_DEA.iloc[i, j]):
                US_DEA.iloc[i, j] = 0
        a = a+float(US_DEA.iloc[i, j])
    death_all.append(int(a))


print(positive_all)


new_case = []
new_dea = []
account_pos = []
account_dea = []
print(death_all)
for i in range(len(positive_all)-1):
    new_case.append(int(float(positive_all[i+1])-float(positive_all[i])))
    new_dea.append(int(float(death_all[i+1])-float(death_all[i])))
US_pos = []
US_Dea = []
past_US_pos = []
past_US_Dea = []
past_day = 56*7  # 7天前
past_3_day = 56*3  # 3天前
past_5_day = 56*5  # 5天前
POSITIVE_NUMBER = []
rate_7days = []

# 计算近七天疫情确诊人数的增长速率
for j in range(1, count):
    if US_POS.iloc[day_dea_end, j] != 0:
        a = (float(US_POS.iloc[day_dea_end-1, j])-float(
            US_POS.iloc[day_dea_end-7, j]))/7/(float(US_POS.iloc[day_dea_end, j]))*100
        rate_7days.append('%.2f' % a)


avg_pos = []
avg_dea = []
for i in range(0, len(new_case)):
    a = 0
    b = 0
    if i <= 6 and i > 0:
        for j in range(0, i):
            a = a+new_case[j]
            b = b+new_dea[j]
        avg_dea.append(int(b/i))
        avg_pos.append(int(a/i))
    if i == 0:
        avg_pos.append(int(new_case[i]))
        avg_dea.append(int(new_dea[i]))
    if i > 6:
        avg_pos.append(int((new_case[i]+new_case[i-1]+new_case[i-2] +
                            new_case[i-3]+new_case[i-4]+new_case[i-5]+new_case[i-6])/7))
        avg_dea.append(int((new_dea[i]+new_dea[i-1]+new_dea[i-2] +
                            new_dea[i-3]+new_dea[i-4]+new_dea[i-5]+new_dea[i-6])/7))


# 国家对比
date = []
China = []
USA = []
World = []
Australia = []
Russia = []
Germany = []
Brazil = []
India = []
# China.append(0)
# USA.append(0)
# World.append(0)
# Australia.append(0)
# Russia.append(0)
# Germany.append(0)
# Brazil.append(0)
# India.append(0)

for i in range(0, int(daily_country.shape[1])):
    if daily_country.iloc[1, i] == 'China':
        print('China', i)
    if daily_country.iloc[1, i] == 'US':
        print('US', i)
    if daily_country.iloc[1, i] == 'World':
        print('World', i)
    if daily_country.iloc[1, i] == 'Australia':
        print('Australia', i)
    if daily_country.iloc[1, i] == 'Russia':
        print('Russia', i)
    if daily_country.iloc[1, i] == 'Germany':
        print('Germany', i)
    if daily_country.iloc[1, i] == 'Brazil':
        print('Brazil', i)
    if daily_country.iloc[1, i] == 'India':
        print('India', i)
for i in range(2, len(daily_country)):
    date.append(daily_country.iloc[i, 0])
for i in range(2, len(daily_country)-1):
    if math.isnan(float(daily_country.iloc[i, 32])):  # China
        daily_country.iloc[i, 32] = 0
        daily_country.iloc[i+1, 32] = 0
    if math.isnan(float(daily_country.iloc[i, 151])):  # US
        daily_country.iloc[i, 151] = 0
        daily_country.iloc[i+1, 151] = 0
    if math.isnan(float(daily_country.iloc[i, 161])):  # World
        daily_country.iloc[i, 161] = 0
        daily_country.iloc[i+1, 161] = 0
    if math.isnan(float(daily_country.iloc[i, 8])):  # Australia
        daily_country.iloc[i, 8] = 0
        daily_country.iloc[i+1, 8] = 0
    if math.isnan(float(daily_country.iloc[i, 123])):  # Russia
        daily_country.iloc[i, 123] = 0
        daily_country.iloc[i+1, 123] = 0
    if math.isnan(float(daily_country.iloc[i, 19])):  # Brazil
        daily_country.iloc[i, 19] = 0
        daily_country.iloc[i+1, 19] = 0
    if math.isnan(float(daily_country.iloc[i, 69])):  # india
        daily_country.iloc[i, 69] = 0
        daily_country.iloc[i+1, 69] = 0
    if math.isnan(float(daily_country.iloc[i, 57])):  # Germany
        daily_country.iloc[i, 57] = 0
        daily_country.iloc[i+1, 57] = 0
    China.append(
        float(daily_country.iloc[i+1, 32])-float(daily_country.iloc[i, 32]))
    USA.append(
        float(daily_country.iloc[i+1, 151])-float(daily_country.iloc[i, 151]))
    World.append(
        float(daily_country.iloc[i+1, 161])-float(daily_country.iloc[i, 161]))
    Australia.append(
        float(daily_country.iloc[i+1, 8])-float(daily_country.iloc[i, 8]))
    Russia.append(
        float(daily_country.iloc[i+1, 123])-float(daily_country.iloc[i, 123]))
    Germany.append(
        float(daily_country.iloc[i+1, 57])-float(daily_country.iloc[i, 57]))
    Brazil.append(
        float(daily_country.iloc[i+1, 19])-float(daily_country.iloc[i, 19]))
    India.append(
        float(daily_country.iloc[i+1, 69])-float(daily_country.iloc[i, 69]))

print(len(positive_all))
Combine_Pos_log = (
    Line()
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Cases",
        y_axis=positive_all,
        yaxis_index=0,
        xaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4, color='#CC6600'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Cases",
        y_axis=new_case,
        yaxis_index=1,
        xaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Cases(7days)",
        y_axis=avg_pos,
        yaxis_index=1,
        xaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4, color='#379B9F'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="New Cases",
            name_location="end",
            type_="value",
            min_=10000,
            # max_=50000,
            position="right",
            # is_inverse=True,
            axistick_opts=opts.AxisTickOpts(is_show=False),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Positive_situation", pos_left="35%", pos_top="top",),
        # , axis_pointer_type="cross"
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        datazoom_opts=[
            opts.DataZoomOpts(range_start=0, range_end=100,
                              pos_bottom="49%", xaxis_index=0, type_="inside"),
            opts.DataZoomOpts(range_start=0, range_end=100,
                              pos_bottom="49%", xaxis_index=1, type_="inside"),
            opts.DataZoomOpts(range_start=0, range_end=100,
                              pos_bottom="49%", xaxis_index=2, type_="inside"),
            opts.DataZoomOpts(range_start=0, range_end=100,
                              pos_bottom="49%", xaxis_index=3, type_="inside"),
            opts.DataZoomOpts(range_start=0, range_end=100,
                              pos_bottom="49%", xaxis_index=4, type_="inside"),
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
Combine_DEA = (
    Line()
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Deaths",
        y_axis=death_all,
        xaxis_index=1,
        yaxis_index=2,
        linestyle_opts=opts.LineStyleOpts(width=4, color='#AB2524'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Deaths",
        y_axis=new_dea,
        # symbol_size=10,
        xaxis_index=1,
        yaxis_index=3,
        linestyle_opts=opts.LineStyleOpts(width=4, color='#6B716F'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Deaths(7 days)",
        y_axis=avg_dea,
        # symbol_size=10,
        xaxis_index=1,
        yaxis_index=3,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="New Deaths",
            name_location="end",
            type_="value",
            min_=0,
            max_=8000,
            # max_=50000,
            position="right",
            # is_inverse=True,
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Deaths_situation", pos_left="54%", pos_top="top",),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="70%", pos_top="top"),
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name="Cumularive Deaths",
            min_=0,
            max_=151000,
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
        # ).render("test1.html")
    )
)

Combine_Pos_value = (
    Line()
    .add_xaxis(xaxis_data=DATE)
    .add_yaxis(
        series_name="Cumularive Cases",
        y_axis=positive_all,
        xaxis_index=2,
        yaxis_index=4,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New cases",
        y_axis=new_case,
        # symbol_size=10,
        xaxis_index=2,
        yaxis_index=5,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="New Cases(7 days)",
        y_axis=avg_pos,
        # symbol_size=10,
        xaxis_index=2,
        yaxis_index=5,
        linestyle_opts=opts.LineStyleOpts(width=4),
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
        title_opts=opts.TitleOpts(
            title="POS_value", pos_left="20%", pos_top="37%",),
        tooltip_opts=opts.TooltipOpts(
            trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_left="17%", pos_top="35%"),
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
Country_US = (
    Line(init_opts=opts.InitOpts())
    .add_xaxis(xaxis_data=STATE)
    .add_yaxis(
        series_name="近7天",
        xaxis_index=3,
        yaxis_index=6,
        y_axis=rate_7days,  # [item[1] for item in ACC_3DAYS]
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
        title_opts=opts.TitleOpts(
            title="美国近一周疫情情况", pos_top="35%", pos_left="62%", subtitle="各州疫情确诊人数的增长速率(%)"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", formatter="{c}%"),
        legend_opts=opts.LegendOpts(pos_left="80%", pos_top="40%"),
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

POSITIVE_situation = (
    Line()
    .add_xaxis(xaxis_data=date)
    .add_yaxis(
        series_name="China",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=China,
        linestyle_opts=opts.LineStyleOpts(width=4, color='#CC6600'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="US",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=USA,
        linestyle_opts=opts.LineStyleOpts(width=4, color='#379B9F'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="Russia",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=Russia,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False, color='#FF7F00'),
    )
    .add_yaxis(
        series_name="World",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=World,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False, color='#FF0000'),
    )
    .add_yaxis(
        series_name="Australia",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=Australia,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False, color='#FFFF00'),
    )
    .add_yaxis(
        series_name="Brazil",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=Brazil,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False, color='#00FF00'),
    )
    .add_yaxis(
        series_name="Germany",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=Germany,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False, color='#00FFFF'),
    )
    .add_yaxis(
        series_name="India",
        xaxis_index=4,
        yaxis_index=7,
        y_axis=India,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False, color=' #0000FF'),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="各国新增确诊人数", pos_top="63%", pos_left="40%"),
        # , axis_pointer_type="cross"
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        legend_opts=opts.LegendOpts(pos_top="66%", pos_left="20%"),
        datazoom_opts=[
            opts.DataZoomOpts(range_start=0, range_end=100, xaxis_index=0),
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
    )  # .render("D:/Pchong/data_see/html_all/Country_daily.html")
)

grid = (
    Grid(init_opts=opts.InitOpts(width="1200px", height="1200px"))
    .add(Combine_Pos_log, grid_opts=opts.GridOpts(pos_right="55%", pos_top="5%", pos_bottom="70%"), is_control_axis_index=True)
    .add(Combine_DEA, grid_opts=opts.GridOpts(pos_left="55%", pos_top="5%", pos_bottom="70%"), is_control_axis_index=True)
    .add(Combine_Pos_value, grid_opts=opts.GridOpts(pos_right="55%", pos_top="40%", pos_bottom="40%"), is_control_axis_index=True)
    .add(Country_US, grid_opts=opts.GridOpts(pos_left="55%", pos_top="40%", pos_bottom="40%"), is_control_axis_index=True)
    .add(POSITIVE_situation, grid_opts=opts.GridOpts(pos_top="67%"), is_control_axis_index=True)
    .render("D:\Pchong\data_see\html_all\situation_log_test.html")
)
accoun_world = []
a = 0
for i in range(2, len(daily_country)-1):
    a = float(daily_country.iloc[i+1, 161]) / \
        float(daily_country.iloc[i, 161])
    accoun_world.append('%.2f' % a)

(
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=date)
    .add_yaxis(
        series_name="感染率",
        y_axis=accoun_world,
        linestyle_opts=opts.LineStyleOpts(width=2),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全球疫情增长速率", pos_left="center"),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{c}"),
        datazoom_opts=[
            opts.DataZoomOpts(range_start=0, range_end=100,
                              pos_bottom="49%", xaxis_index=0, type_="inside"),
        ],
        legend_opts=opts.LegendOpts(pos_left="left"),
        xaxis_opts=opts.AxisOpts(type_="category", name="x"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            name="y",
            min_=1.0,
            splitline_opts=opts.SplitLineOpts(is_show=False),
            is_scale=True,
        ),
    )
    .render("D:\Pchong\data_see\html_all\world_line.html")
)
