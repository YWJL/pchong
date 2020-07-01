import asyncio
from aiohttp import TCPConnector, ClientSession
import json
import pyecharts.options as opts
from pyecharts.charts import Map
import pandas as pd
import math
with open('USA.json', 'r') as f:
    data=json.loads(f.read())
name='daily.csv'
US=pd.read_csv(name)
#MAP_data=[['Alaska', 300], ['Alabama', 4404], ['Arkansas', 1620], ['Arizona', 4234], ['California', 26182], ['Colorado', 8675], ['Connecticut', 15884], ['Washington.D.C', 2350], ['Delaware', 2075], ['Florida', 23340], ['Georgia', 16368], ['Hawaii', 541], ['Iowa', 2141], ['Idaho', 1609], ['Illinois', 25733], ['Indiana', 9542], ['Kansas', 1588], ['Kentucky', 2429], ['Louisiana', 22532], ['Massachusetts', 32181], ['Maryland', 10784], ['Maine', 796], ['Michigan', 29263], ['Minnesota', 1912], ['Missouri', 5111], ['Mississippi', 3624], ['Montana', 415], ['North Carolina', 5465], ['North Dakota', 393], ['Nebraska', 1066], ['New Hampshire', 1211], ['New Jersey', 75317], ['New Mexico', 1597], ['Nevada', 3321], ['New York', 222284], ['Ohio', 8414], ['Oklahoma', 2357], ['Oregon', 1736], ['Pennsylvania', 27735], ['Rhode Island', 3838], ['South Carolina', 3931], ['South Dakota', 1311], ['Tennessee', 6262], ['Texas', 16455], ['Utah', 2683], ['Virginia', 6889], ['Vermont', 768], ['Washington', 11152], ['Wisconsin', 3875], ['West Virginia', 739], ['Wyoming', 296], ['Puerto Rico', 1043], ['AS', 0], ['Guam', 135], ['Northern Mariana Islands', 13], ['US Virgin Islands', 51]]
count=56
time="截止至{}美国疫情数据".format(US.iloc[0,0])
STATE=[]
US_pos=[]
US_Dea=[]
US_Rec=[]
past_STATE=[]
past_US_pos=[]
past_US_Dea=[]
past_US_Rec=[]
past_day=56*6 #7天前
POSITIVE_NUMBER=[]
#计算今天的数据
for i in range(0,56):
    if math.isnan(US.iloc[i,2]):
        US.iloc[i, 2]=0
    if math.isnan(US.iloc[i, 16]):
        US.iloc[i, 16]=0
    if math.isnan(US.iloc[i, 11]):
        US.iloc[i,11]=0
    STATE.append(US.iloc[i,1])
    US_pos.append(US.iloc[i, 2])
    US_Dea.append(US.iloc[i, 16])
    US_Rec.append(US.iloc[i, 11])
MAP_Pos=[list(z) for z in zip(STATE,US_pos)]
MAP_Dea=[list(z) for z in zip(STATE,US_Dea)]
MAP_Rec=[list(z) for z in zip(STATE,US_Rec)]
#计算一周前的数据
for i in range(past_day,past_day+56):
    if math.isnan(US.iloc[i,2]):
        US.iloc[i, 2]=0
    if math.isnan(US.iloc[i, 16]):
        US.iloc[i, 16]=0
    if math.isnan(US.iloc[i, 11]):
        US.iloc[i,11]=0
    past_STATE.append(US.iloc[i,1])
    past_US_pos.append(US.iloc[i, 2])
    past_US_Dea.append(US.iloc[i, 16])
    past_US_Rec.append(US.iloc[i, 11])
print('US_pos:',MAP_Pos)
print('US_Dea:',MAP_Dea)
print('US_Rec:',MAP_Rec)
account_pos=[]
account_dea=[]
account_rec=[]
print(past_US_pos[1])
#获得小数
for i in range(0,56):
    if US_pos[i]!=0:
        account_pos.append((US_pos[i] - past_US_pos[i]) / 7 / US_pos[i])
    else:
        account_pos.append(0)
    if US_Dea[i]!=0:
        account_dea.append((US_Dea[i]-past_US_Dea[i])/7/US_Dea[i])
    else:
        account_dea.append(0)
    if US_Rec!=[0]:
        account_rec.append((US_Rec[i]-past_US_Rec[i])/7/US_Rec[i])
    else:
        account_rec.append(0)
#转百分数
ACC_POS=[]
ACC_DEA=[]
ACC_REC=[]
num=[]
# account7='%.2f%%' % (account7 * 100)
for i in  range(0,56):
    a=account_pos[i]*100
    ACC_POS.append('%.4f' % a)
    b=account_dea[i]*100
    ACC_DEA.append('%.4f' % b)
    c=account_rec[i]*100
    ACC_REC.append('%.4f' % c)
    num.append(a)
    num.append(b)
# A=0.0019865
# b=A*100
# print('%.4f' % b)
# print('%.4f%%' % (A * 100))
ACCOUNT_POS=[list(z) for z in zip(STATE,ACC_POS)]
ACCOUNT_DEA=[list(z) for z in zip(STATE,ACC_DEA)]
ACCOUNT_REC=[list(z) for z in zip(STATE,ACC_REC)]
a=float((int(sum(US_pos))-int(sum(past_US_pos)))/7/int(sum(US_pos)))
a=a*100
week_Pos=('%.4f%%' % a)
b=float((int(sum(US_Dea))-int(sum(past_US_Dea)))/7/int(sum(US_Dea)))
b=b*100
week_Dea=('%.4f%%' % b)
c=float((int(sum(US_Rec))-int(sum(past_US_Rec)))/7/int(sum(US_Rec)))
c=c*100
week_Rec=('%.4f%%' % c)
print('1',max(num))
print(account_pos)
print(US_pos[2],past_US_pos[2])
print(US_pos)
print(ACCOUNT_POS)
print(ACCOUNT_DEA)
print(ACCOUNT_REC)
# time='{}'.format(POSI)
#地图重命名
NAME_MAP_DATA = {
    # "key": "value"
    # "name on the hong kong map": "name in the MAP DATA",
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
    .add_js_funcs("echarts.registerMap('HK', {});".format(data))
        .add(
        series_name="Positive_number",
        data_pair=MAP_Pos,
        maptype="HK",
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False)
        .add(
        series_name="Death_number",
        data_pair=MAP_Dea,
        maptype="HK",
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False)
        .add(
        series_name="Recovered_number",
        data_pair=MAP_Rec,
        maptype="HK",
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="美国疫情情况",
            subtitle=time,
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b}<br/>{c} "
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=min(US_Rec),
            max_=max(US_pos),
            range_text=["high", "low"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
        ),
    )
    .render("USA-5-14.html")
)

#下图进行USA疫情增长率的可视化分析（一周）
(
    Map(init_opts=opts.InitOpts(width="1400px", height="800px"))
    .add_js_funcs("echarts.registerMap('HK', {});".format(data))
        .add(
        series_name="Positive-Growth rate(7 days):{}".format(week_Pos),
        data_pair=ACCOUNT_POS,
        maptype="HK",
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False)
        .add(
        series_name="Death-Growth rate(7 days):{}".format(week_Dea),
        data_pair=ACCOUNT_DEA,
        maptype="HK",
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False)
        .add(
        series_name="Recovered-Growth rate(7 days):{}".format(week_Rec),
        data_pair=ACCOUNT_REC,
        maptype="HK",
        name_map=NAME_MAP_DATA,
        is_map_symbol_show=False)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="美国疫情情况",
            subtitle=time,
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b}:{c}% "
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=min(num),
            max_=max(num),
            range_text=["Dangerous", "Safe"],
            is_calculable=True,
            range_color=["lightskyblue", "yellow", "orangered"],
        ),
    )
    .render("USA-week.html")
)