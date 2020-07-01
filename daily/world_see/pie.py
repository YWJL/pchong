import math
from aiohttp import TCPConnector, ClientSession
import pyecharts.options as opts
from pyecharts.charts import Map
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline, Pie
from pyecharts import options as opts
from pyecharts.charts import Grid, Line, Scatter
from pyecharts.faker import Faker
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker
from pyecharts.charts import Geo
import pandas as pd
import json
import os
# F1 命令
path = 'D:\Pchong\data_see\daily'
os.chdir(path)

death_name = '20200619-world-death-data.json.csv'
positive_name = '20200619-world-confirm-data.json.csv'
recovered_name = '20200619-world-cover-data.json.csv'
line_world_name = '2020-05-31-World_comfirmed.csv'
line_world = pd.read_csv(positive_name)
day = 0
tl = Timeline()
tll = Timeline()
t3 = Timeline()
Time_POS = {}  # Z重要
data2 = {}  # 每日确诊人数最大值
data3 = {}  # 每日新增确诊人数最大值
data4 = {}
Account_pos = {}  # 每日新增确诊人数的比例
count = 0
line_country = []
line_date = []
pos_world = []
pos_add_world = []
pos_add_POS = {}
a = 0
# for i in range(0,180):
#     if line_world.iloc[1,i]=='China':
#         print('China',i)
#     if line_world.iloc[1,i]=='US':
#         print('US',i)
#     if line_world.iloc[1,i]=='World':
#         print('World',i)
#     if line_world.iloc[1,i]=='Australia':
#         print('Australia',i)
#     if line_world.iloc[1,i]=='Russia':
#         print('Russia',i)
#     if line_world.iloc[1,i]=='Germany':
#         print('Germany',i)
#     if line_world.iloc[1,i]=='Brazil':
#         print('Brazil',i)
#     if line_world.iloc[1,i]=='India':
#         print('India',i)
for i in range(1, 180):  # 国家名称
    line_country.append(line_world.iloc[1, i])
    if i > 150 and line_world.iloc[1, i] == 'Albania':
        del line_country[-1]
        break
    if line_world.iloc[1, i] == 'World':
        a = i
    if line_world.iloc[1, i] == 'US':
        del line_country[-1]
        line_country.append('United States')
pos = []

for i in range(2, len(line_world)-1):  # 全球确诊人数
    pos_world.append(line_world.iloc[i, a])
    pos_add_world.append(
        int(float(line_world.iloc[i+1, a])-float(line_world.iloc[i, a])))
    line_world.iloc[i, a] = 0
pos_world.append(line_world.iloc[i+1, a])
line_world.iloc[i+1, a] = 0
for i in range(2, len(line_world)):
    Time_POS[i-2] = []
    pos = []
    a = 0
    data2[i-2] = []
    line_date.append(line_world.iloc[i, 0])
    for j in range(1, len(line_country)):
        # if math.isnan(line_world.iloc[i,j]):
        #     line_world.iloc[i,j]=0
        pos.append(float(line_world.iloc[i, j]))  # float格式一定可以
        if a < float(line_world.iloc[i, j]):
            a = float(line_world.iloc[i, j])
    data2[i-2] = a
    Time_POS[i-2] = [list(z) for z in zip(line_country, pos)]

for i in range(0, len(line_world)-2):
    map0 = (
        Map()
        .add("确诊人数", Time_POS[i], "world", is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="{}-世界疫情趋势".format(line_date[i]), subtitle="世界确诊人数总和{}人".format(pos_world[i])),
            visualmap_opts=opts.VisualMapOpts(max_=data2[i]),
        )
    )
    tl.add(map0, "{}".format(line_date[i]))
tl.render("map_world_test_1.html")
for i in range(2, len(line_world)-1):  # 全球确诊人数（日增长
    pos_add_POS[i-2] = []
    pos = []
    a = 0
    data2[i-2] = []
    for j in range(1, len(line_country)):
        # if math.isnan(line_world.iloc[i,j]):
        #     line_world.iloc[i,j]=0
        pos.append(float(line_world.iloc[i+1, j]) -
                   float(line_world.iloc[i, j]))  # float格式一定可以
        if a < float(line_world.iloc[i+1, j])-float(line_world.iloc[i, j]):
            a = float(line_world.iloc[i+1, j])-float(line_world.iloc[i, j])
    data3[i-2] = a
    pos_add_POS[i-2] = [list(z) for z in zip(line_country, pos)]
for i in range(0, len(line_world)-3):
    map1 = (
        Map()
        .add("新增确诊人数", pos_add_POS[i], "world", is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="{}-世界疫情趋势".format(line_date[i]), subtitle="全球新增确诊人数总和{}人".format(pos_add_world[i])),
            visualmap_opts=opts.VisualMapOpts(max_=data3[i]),
        )
    )
    tll.add(map1, "{}".format(line_date[i]))
tll.render("map_world_test_2.html")

print(line_world.iloc[2, 0])
pie_country = []
pie_2_23 = []

for j in range(2, len(line_country)):
    if type(line_world.iloc[33, j]) == str:
        pie_country.append(line_world.iloc[1, j])
        pie_2_23.append(float(line_world.iloc[33, j]))
    # else:
    #     pie_country.append(line_world.iloc[1,j])
    #     pie_2_23.append(float(line_world.iloc[33,j]))
pie_pair = [list(z) for z in zip(pie_country, pie_2_23)]
print(pie_country, pie_2_23)
c = (
    Pie()
    .add(
        "",
        pie_pair,
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2-23全球疫情确诊情况"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))
    .render("pie_position.html")
)
