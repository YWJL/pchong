import pandas
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Collector, Faker
from pyecharts.datasets import register_url
import pandas as pd
import asyncio
from pyecharts.commons.utils import JsCode
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
path='D:\Pchong\data_see\daily'
os.chdir(path)
US_name='D:/Pchong/data_see/data_all/daily.csv'
death_name='D:/Pchong/data_see/data_all/20200527-world-death-data.json.csv'
positive_name='D:/Pchong/data_see/data_all/20200527-world-confirm-data.json.csv'
recovered_name='D:/Pchong/data_see/data_all/20200527-world-cover-data.json.csv'
daily_country=pd.read_csv(positive_name)
# a=0
# a=float(daily_country.iloc[2,29])
# print(type(a),a)
test1=pd.read_csv(positive_name)
# print(test1.iloc[1,30])
daily_country_name=['China','US','World','Australia','Russia','Germany','Brazil','India']
# print(daily_country.columns.values[-1])#列名
#China 30    US 145    World 155  Australia 7    Russia 118    Germany 53    Brazil 18    India 65
# for i in range(0,int(daily_country.shape[1])):
#     if daily_country.columns.values[i]=='China':
#         print('China',i)
#     if daily_country.columns.values[i]=='US':
#         print('US',i)
#     if daily_country.columns.values[i]=='World':
#         print('World',i)
#     if daily_country.columns.values[i]=='Australia':
#         print('Australia',i)
#     if daily_country.columns.values[i]=='Russia':
#         print('Russia',i)
#     if daily_country.columns.values[i]=='Germany':
#         print('Germany',i)
#     if daily_country.columns.values[i]=='Brazil':
#         print('Brazil',i)
#     if daily_country.columns.values[i]=='India':
#         print('India',i)
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





RECOVERED=pd.read_csv(recovered_name)
DEATH=pd.read_csv(death_name)
POSITIVE=pd.read_csv(positive_name)
US=pd.read_csv(US_name)
print(DEATH.iloc[1,0])
US_pos=[]
US_Dea=[]
US_Rec=[]
for i in range(1,56):
    if math.isnan(US.iloc[i,2]):
        US.iloc[i, 2]=0
    if math.isnan(US.iloc[i, 16]):
        US.iloc[i, 16]=0
    if math.isnan(US.iloc[i, 11]):
        US.iloc[i,11]=0
    US_pos.append(US.iloc[i, 2])
    US_Dea.append(US.iloc[i, 16])
    US_Rec.append(US.iloc[i, 11])
# print('US_pos:',US_pos)
# print('US_Dea:',US_Dea)
# print('US_Rec:',US_Rec)
country_number_pos=int((POSITIVE.shape[1])/2-1)
country_number_dea=int((DEATH.shape[1])/2-1)
country_number_rec=int((RECOVERED.shape[1])/2-2)
# print(country_number_dea)
# print(RECOVERED.iloc[1,country_number_rec])
day=len(POSITIVE)-1
print('day',DEATH.iloc[day-1,1],day)
country_pos=[]
country_dea=[]
country_rec=[]
positive=[]
death=[]
recovered=[]
# print('sum(US_dea):',sum(US_Dea))
# print('sum(US_pos):',sum(US_pos))
# print('sum(US_rec):',sum(US_Rec))
time="截止至{}全球疫情数据".format(POSITIVE.iloc[-1,0])
for i in range(1,country_number_dea):
    country_dea.append(DEATH.iloc[1,i])
    death.append(DEATH.iloc[day-1,i])
country_dea.append('United States')
death.append(sum(US_Dea))
MAP_data_dea=[list(z) for z in zip(country_dea, death)]
print('MAP_data_dea:',MAP_data_dea)
for i in range(1,country_number_pos):
    country_pos.append(POSITIVE.iloc[1,i])
    positive.append(POSITIVE.iloc[day,i])
country_pos.append('United States')
positive.append(sum(US_pos))
MAP_data_pos=[list(z) for z in zip(country_pos, positive)]
print(len(positive))
MAP_data_rec=[]
# print(type(RECOVERED.iloc[2,0]))
for i in range(1,day-6):
    for j in range(1,day-6):
        if type(RECOVERED.iloc[i,j])!=str and math.isnan(RECOVERED.iloc[i,j]):
            RECOVERED.iloc[i,j]=0
for i in range(1,day-6):
    country_rec.append(RECOVERED.iloc[1,i])
    recovered.append(RECOVERED.iloc[day-6,i])
    MAP_data_rec=[list(z) for z in zip(country_rec, recovered)]
country_rec.append('United States')
recovered.append(sum(US_Rec))
print('MAP_data_pos:',MAP_data_pos)
# for i in range(1,country_number_dea-1):
#     for j in range(1,country_number_dea-1):
#         if country_pos[i]==country_dea[j]:
#             map1=[list(z) for z in zip(country_dea, country_pos)]
# print(map1)

# print(country)
# print(data.iloc[day,1])
# print(day)
NAME_MAP_DATA = {
    # "key": "value"
    # "name on the hong kong map": "name in the MAP DATA",

}

c = (
    Map(init_opts=opts.InitOpts(width="1400px", height="800px"))

        .add(
        series_name="D",
        data_pair=MAP_data_dea,
        maptype="world",
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False)
                .add(
        series_name="P",
        data_pair=MAP_data_pos,
        maptype="world",
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False)
        # .add(
        # series_name="Recovered_number",
        # data_pair=MAP_data_rec,
        # maptype="world",
        # name_map=NAME_MAP_DATA,
        # is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Map-世界地图",
            subtitle=time),
        # subtitle=time,
        tooltip_opts=opts.TooltipOpts(formatter=JsCode(
                        """function (params) {
                               return params.value;
                           }"""
                   )),
        visualmap_opts=opts.VisualMapOpts(
            max_=sum(US_pos),
            range_text=["Dangerous", "Safe"],
            is_calculable=True,
            # range_color=["lightskyblue", "yellow", "orangered"],
        )
    )
    .render("D:\Pchong\data_see\html_all\map_world.html")
)
# print([list(z) for z in zip(Faker.country, Faker.values())])
print(max(US_pos))

POSITIVE_situation=(
    Line()
    .add_xaxis(xaxis_data=date)
    .add_yaxis(
        series_name="China",
        y_axis=China,
        yaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#CC6600'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="US",
        y_axis=USA,
        yaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4,color='#379B9F'),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="Russia",
        y_axis=Russia,
        yaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False,color='#FF7F00'),
    )
    .add_yaxis(
        series_name="World",
        y_axis=World,
        yaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False,color='#FF0000'),
    )
    .add_yaxis(
        series_name="Australia",
        y_axis=Australia,
        yaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False,color='#FFFF00'),
    )
    .add_yaxis(
        series_name="Brazil",
        y_axis=Brazil,
        yaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False,color='#00FF00'),
    )
    .add_yaxis(
        series_name="Germany",
        y_axis=Germany,
        yaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False,color='#00FFFF'),
    )
    .add_yaxis(
        series_name="India",
        y_axis=India,
        yaxis_index=0,
        linestyle_opts=opts.LineStyleOpts(width=4),
        label_opts=opts.LabelOpts(is_show=False,color=' #0000FF'),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),  #, axis_pointer_type="cross"
        legend_opts=opts.LegendOpts(pos_left="left"),
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
).render("D:/Pchong/data_see/html_all/Country_daily.html")
)
print('US',USA)
print('India',India)
tl = Timeline()
# for i in range(2015, 2020):
#     map0 = (
#         Map()
#         .add("商家A", MAP_data_pos, "world",is_map_symbol_show=False)
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="Map-{}年某些数据".format(i)),
#             visualmap_opts=opts.VisualMapOpts(max_=sum(US_pos)),
#         )
#     )
#     tl.add(map0, "{}年".format(i))
# tl.render("D:/Pchong/data_see/html_all/map_world_test.html")
Time_POS={}          #Z重要
data2={}
for i in range(2,day):
    Time_POS[i-2]=[]
    pos=[]
    data2[i-2]=[]
    for j in range(1,country_number_pos):
        pos.append(POSITIVE.iloc[i,j])
        data2[i-2].append(POSITIVE.iloc[i,30])
    Time_POS[i-2]=[list(z) for z in zip(country_pos, pos)]
print('Time_POS[1]:',Time_POS[1])

# for i in range(0, day-2):
#     map0 = (
#         Map()
#         .add("商家A", Time_POS[i], "world",is_map_symbol_show=False)
#         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#         .set_global_opts(
#             title_opts=opts.TitleOpts(title="世界疫情趋势".format(i)),
#             visualmap_opts=opts.VisualMapOpts(max_=max(data2[i])),
#         )
#     )
#     tl.add(map0, "疫情开始第{}天".format(i+1))
# tl.render("D:/Pchong/data_see/html_all/map_world_test.html")






#     positive.append(POSITIVE.iloc[day,i])
# country_pos.append('United States')
# positive.append(sum(US_pos))
# MAP_data_pos=[list(z) for z in zip(country_pos, positive)]
print(JsCode(
                        """function (params) {
                               return params.value;
                           }"""
                   ))

                        # """function (params) {
                        #        return params.seriesName['']+':'+params.value;
                        #    }"""
                            #     # tooltip_opts=opts.TooltipOpts(formatter=JsCode(
    #                     """function (params){
    #    componentType: 'series',
    #    seriesType: string,
    #    seriesIndex: number,
    #    seriesName: string,
    #    name: string,
    #    dataIndex: number,
    #    data: Object,
    #    value: number
    #    color: string,
    #  }"""
                #    )),