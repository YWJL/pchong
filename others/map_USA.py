import asyncio
from aiohttp import TCPConnector, ClientSession
import json
import pyecharts.options as opts
from pyecharts.charts import Map
import pandas as pd
with open('USA.json', 'r') as f:
    data=json.loads(f.read())
name='daily.csv'
state=pd.read_csv(name,usecols=[1])
positive=pd.read_csv(name,usecols=[2])
print(type(positive.iloc[1,0]))
#MAP_data=[['Alaska', 300], ['Alabama', 4404], ['Arkansas', 1620], ['Arizona', 4234], ['California', 26182], ['Colorado', 8675], ['Connecticut', 15884], ['Washington.D.C', 2350], ['Delaware', 2075], ['Florida', 23340], ['Georgia', 16368], ['Hawaii', 541], ['Iowa', 2141], ['Idaho', 1609], ['Illinois', 25733], ['Indiana', 9542], ['Kansas', 1588], ['Kentucky', 2429], ['Louisiana', 22532], ['Massachusetts', 32181], ['Maryland', 10784], ['Maine', 796], ['Michigan', 29263], ['Minnesota', 1912], ['Missouri', 5111], ['Mississippi', 3624], ['Montana', 415], ['North Carolina', 5465], ['North Dakota', 393], ['Nebraska', 1066], ['New Hampshire', 1211], ['New Jersey', 75317], ['New Mexico', 1597], ['Nevada', 3321], ['New York', 222284], ['Ohio', 8414], ['Oklahoma', 2357], ['Oregon', 1736], ['Pennsylvania', 27735], ['Rhode Island', 3838], ['South Carolina', 3931], ['South Dakota', 1311], ['Tennessee', 6262], ['Texas', 16455], ['Utah', 2683], ['Virginia', 6889], ['Vermont', 768], ['Washington', 11152], ['Wisconsin', 3875], ['West Virginia', 739], ['Wyoming', 296], ['Puerto Rico', 1043], ['AS', 0], ['Guam', 135], ['Northern Mariana Islands', 13], ['US Virgin Islands', 51]]
print(state.iloc[1,0])
count=56
STATE=[]
POSITIVE_NUMBER=[]
for i in range(56):
    STATE.append(state.iloc[i,0])
    POSITIVE_NUMBER.append(positive.iloc[i,0])
print(STATE)
print(POSITIVE_NUMBER)
MAP_data=[list(z) for z in zip(STATE, POSITIVE_NUMBER)]
print(MAP_data)
NAME_MAP_DATA = {
    # "key": "value"
    # "name on the hong kong map": "name in the MAP DATA",
    "Alaska": "AK",
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

(
    Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
    .add_js_funcs("echarts.registerMap('HK', {});".format(data))
    .add(
        series_name="美国地图",
        maptype="HK",
        data_pair=MAP_data,
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False,#红点标记
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="美国疫情情况",
            subtitle="数据源：https://echarts.baidu.com/examples/data/asset/geo/USA.json",
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b}<br/>(positive:{c}) "
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=800,
            max_=50000,
            range_text=["High", "Low"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
        ),
    )
    .render("map_test_2.html")
)