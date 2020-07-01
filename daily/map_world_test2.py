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
import pandas as pd
import json
import os
path='D:\Pchong\data_see\daily'
os.chdir(path)
US_name='D:/Pchong/data_see/data_all/daily.csv'
death_name='D:/Pchong/data_see/data_all/20200608-world-death-data.json.csv'
positive_name='D:/Pchong/data_see/data_all/20200608-world-confirm-data.json.csv'
recovered_name='D:/Pchong/data_see/data_all/20200608-world-cover-data.json.csv'
line_world_name='D:/Pchong/data_see/data_all/2020-05-31-World_comfirmed.csv'
line_world=pd.read_csv(positive_name)
day=0
tl = Timeline()
tll=Timeline()
Time_POS={}          #Z重要
data2={}   #每日确诊人数最大值
data3={}   #每日新增确诊人数最大值
count=0
line_country=[]
line_date=[]
pos_world=[]
pos_add_world=[]
pos_add_POS={}
a=0
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
for i in range(1,180):
    line_country.append(line_world.iloc[1,i])
    if i>150 and line_world.iloc[1,i]=='Albania':
        del line_country[-1]
        break
    if line_world.iloc[1,i]=='World':
        a=i
    if line_world.iloc[1,i]=='US':
        del line_country[-1]
        line_country.append('United States')
pos=[]
for i in range(2,len(line_world)-1):
    pos_world.append(line_world.iloc[i,a])
    pos_add_world.append(int(float(line_world.iloc[i+1,a])-float(line_world.iloc[i,a])))
    line_world.iloc[i,a]=0
pos_world.append(line_world.iloc[i+1,a])
line_world.iloc[i+1,a]=0
for i in range(2,len(line_world)):
    Time_POS[i-2]=[]
    pos=[]
    a=0
    data2[i-2]=[]
    line_date.append(line_world.iloc[i,0])
    for j in range(1,len(line_country)):
        # if math.isnan(line_world.iloc[i,j]):
        #     line_world.iloc[i,j]=0
        pos.append(float(line_world.iloc[i,j]))                      #float格式一定可以
        if a<float(line_world.iloc[i,j]):
            a=float(line_world.iloc[i,j])
    data2[i-2]=a
    Time_POS[i-2]=[list(z) for z in zip(line_country, pos)]
for i in range(0, len(line_world)-2):
    map0 = (
        Map()
        .add("确诊人数", Time_POS[i], "world",is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="{}-世界疫情趋势".format(line_date[i]),subtitle="世界确诊人数总和{}人".format(pos_world[i])),
            visualmap_opts=opts.VisualMapOpts(max_=data2[i]),
        )
    )
    tl.add(map0, "{}".format(line_date[i]))
#     bar = (
#     Bar()
#     .add_xaxis(xaxis_data=bar_x_data)
#     .add_yaxis(
#         series_name='',
#         yaxis_data=bar_y_data,
#         label_opts=opts.LabelOpts(
#             is_show=True, position='right', formatter='{b} : {c}'
#         )
#     )
#     .reversal_axis()
#     .set_global_opts(
#         xaxis_opts=opts.AxisOpts(
#             max_=maxNum, axislabel_opts=opts.LabelOpts(is_show=False)
#         ),
#         yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
#         tooltip_opts=opts.TooltipOpts(is_show=False),
#         visualmap_opts=opts.VisualMapOpts(
#             is_calculable=True,
#             dimension=0,
#             pos_left='10',
#             pos_top='top',
#             range_text=['High', 'Low'],
#             range_color=['lightskyblue', 'yellow', 'orangered'],
#             textstyle_opts=opts.TextStyleOpts(color='#ddd'),
#             min_=min_data,
#             max_=max_data,
#         )
#     )
# )
tl.render("D:/Pchong/data_see/html_all/map_world_test_1.html")
print([x[1] for x in Time_POS[0]] )
today_country=[]
today_number=[]
x=Time_POS[0][0]
a=[]
b=[]
for x in Time_POS[0]:
    if math.isnan(x[1]):
        x[1]=0
for i in range(0,10):
    b.append(max(x[1] for x in Time_POS[0]))
    a.append(x[0])
    Time_POS[0].remove(x[1])
    Time_POS[0].remove(x[0])
print(a)
print(b)



























































































# for i in range(2,len(line_world)-1):
#     pos_add_POS[i-2]=[]
#     pos=[]
#     a=0
#     data2[i-2]=[]
#     for j in range(1,len(line_country)):
#         # if math.isnan(line_world.iloc[i,j]):
#         #     line_world.iloc[i,j]=0
#         pos.append(float(line_world.iloc[i+1,j])-float(line_world.iloc[i,j]))                      #float格式一定可以
#         if a<float(line_world.iloc[i+1,j])-float(line_world.iloc[i,j]):
#             a=float(line_world.iloc[i+1,j])-float(line_world.iloc[i,j])
#     data3[i-2]=a
#     pos_add_POS[i-2]=[list(z) for z in zip(line_country, pos)]
# for i in range(0, len(line_world)-3):
#     map1 = (
#         Map()
#         .add("新增确诊人数", pos_add_POS[i], "world",is_map_symbol_show=False)
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="{}-世界疫情趋势".format(line_date[i]),subtitle="全球新增确诊人数总和{}人".format(pos_add_world[i])),
#             visualmap_opts=opts.VisualMapOpts(max_=data3[i]),
#         )
#     )
#     tll.add(map1, "{}".format(line_date[i]))
# tll.render("D:/Pchong/data_see/html_all/map_world_test_2.html")