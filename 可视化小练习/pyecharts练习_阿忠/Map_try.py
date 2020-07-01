import csv
import json
from pyecharts.charts import Map
from pyecharts import options as opts

with open("USA.json", 'r') as f:
    text = json.loads(f.read())

csv_file = csv.reader(open("USA_epidemic_faker_data.csv"))
MAP_DATA = []
for line in csv_file:
    MAP_DATA.append(line)

NAME_MAP_DATA = {
    "Alaska": "AS",
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
    .add_js_funcs("echarts.registerMap('USA', {})".format(text))
    .add(
        series_name="Positive_number",
        data_pair=MAP_DATA,
        maptype='USA',
        is_selected=True,
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="美国疫情情况",
            subtitle="截止至2020年5月20日美国疫情数据"
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=0,
            max_=354370,
            range_text=["High", "Low"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"]
        )
    )
    .render('Map_try.html')
)
