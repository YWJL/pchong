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
US_name='daily.csv'
death_name='20200517-world-death-data.json.csv'
positive_name='20200517-world-confirm-data.json.csv'
recovered_name='20200517-world-cover-data.json.csv'
RECOVERED=pd.read_csv(recovered_name)
DEATH=pd.read_csv(death_name)
POSITIVE=pd.read_csv(positive_name)
US=pd.read_csv(US_name)
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
print('US_pos:',US_pos)
print('US_Dea:',US_Dea)
print('US_Rec:',US_Rec)
country_number_pos=int((POSITIVE.shape[1])/2-1)
country_number_dea=int((DEATH.shape[1])/2-1)
country_number_rec=int((RECOVERED.shape[1])/2-2)
print(country_number_dea)
print(RECOVERED.iloc[1,country_number_rec])
day=len(POSITIVE)-1
print(day)
country_pos=[]
country_dea=[]
country_rec=[]
positive=[]
death=[]
recovered=[]
print('sum(US_dea):',sum(US_Dea))
print('sum(US_pos):',sum(US_pos))
print('sum(US_rec):',sum(US_Rec))
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
        series_name="Positive_number",
        data_pair=MAP_data_pos,
        maptype="world",
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False)
        .add(
        series_name="Death_number",
        data_pair=MAP_data_dea,
        maptype="world",
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False)
        .add(
        series_name="Recovered_number",
        data_pair=MAP_data_rec,
        maptype="world",
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title="Map-世界地图",
            subtitle=time),
        # subtitle=time,
        visualmap_opts=opts.VisualMapOpts(max_=sum(US_pos)),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b0}<br/>(number:{c}) "
        ),
    )
    .render("map_world.html")
)
# print([list(z) for z in zip(Faker.country, Faker.values())])
print(max(US_pos))