import pandas as pd
import asyncio
from aiohttp import TCPConnector, ClientSession
import pyecharts.options as opts
from pyecharts.charts import Map
async def get_json_data(url: str) -> dict:
    async with ClientSession(connector=TCPConnector(ssl=False)) as session:
        async with session.get(url=url) as response:
            return await response.json()
data = asyncio.run(
    get_json_data(url="https://coronavirus.1point3acres.com/resources/maps/us_map/GA.json")
)    #或者这样获取网页json

# with open('GA.json', 'r') as f:         #这是获取本地json
#     data=json.loads(f.read())
name='countycases-GA.csv'
POSITIVE=pd.read_csv(name,usecols=[2])
GA_name=pd.read_csv(name,usecols=[0])
# print(POSITIVE)
pos=[]
name=[]
print(type(POSITIVE.iloc[1,0]))
#MAP_data=[['Appling', 73], ['Atkinson', 9], ['Bacon', 25], ['Baker', 23], ['Baldwin', 226], ['Banks', 25], ['Barrow', 141], ['Bartow', 320], ['Ben Hill', 26], ['Berrien', 17], ['Bibb', 312], ['Bleckley', 19], ['Brantley', 23], ['Brooks', 59], ['Bryan', 54], ['Bulloch', 40], ['Burke', 86], ['Butts', 153], ['Calhoun', 103], ['Camden', 33], ['Candler', 7], ['Carroll', 375], ['Catoosa', 47], ['Charlton', 11], ['Chatham', 230], ['Chattahoochee', 12], ['Chattooga', 16], ['Cherokee', 476], ['Clarke', 155], ['Clay', 23], ['Clayton', 724], ['Clinch', 8], ['Cobb', 1672], ['Coffee', 141], ['Colquitt', 187], ['Columbia', 162], ['Cook', 25], ['Coweta', 209], ['Crawford', 17], ['Crisp', 167], ['Dade', 16], ['Dawson', 61], ['DeKalb', 2065], ['Decatur', 86], ['Dodge', 28], ['Dooly', 129], ['Dougherty', 1531], ['Douglas', 325], ['Early', 213], ['Echols', 5], ['Effingham', 36], ['Elbert', 23], ['Emanuel', 21], ['Evans', 5], ['Fannin', 30], ['Fayette', 177], ['Floyd', 145], ['Forsyth', 308], ['Franklin', 19], ['Fulton', 2880], ['Gilmer', 69], ['Glynn', 58], ['Gordon', 112], ['Grady', 64], ['Greene', 54], ['Gwinnett', 1843], ['Habersham', 325], ['Hall', 1466], ['Hancock', 51], ['Haralson', 29], ['Harris', 61], ['Hart', 11], ['Heard', 11], ['Henry', 492], ['Houston', 234], ['Irwin', 15], ['Jackson', 97], ['Jasper', 22], ['Jeff Davis', 20], ['Jefferson', 14], ['Jenkins', 16], ['Johnson', 51], ['Jones', 29], ['Lamar', 38], ['Lanier', 9], ['Laurens', 62], ['Lee', 321], ['Liberty', 37], ['Lincoln', 12], ['Long', 5], ['Lowndes', 156], ['Lumpkin', 46], ['Macon', 81], ['Madison', 24], ['Marion', 42], ['McDuffie', 45], ['McIntosh', 6], ['Meriwether', 53], ['Miller', 33], ['Mitchell', 318], ['Monroe', 24], ['Montgomery', 2], ['Morgan', 27], ['Murray', 32], ['Muscogee', 313], ['Newton', 200], ['Non-Georgia Resident', 1080], ['Oconee', 66], ['Oglethorpe', 49], ['Paulding', 190], ['Peach', 52], ['Pickens', 25], ['Pierce', 55], ['Pike', 40], ['Polk', 59], ['Pulaski', 31], ['Putnam', 42], ['Quitman', 4], ['Rabun', 14], ['Randolph', 161], ['Richmond', 411], ['Rockdale', 191], ['Schley', 16], ['Screven', 15], ['Seminole', 29], ['Spalding', 211], ['Stephens', 81], ['Stewart', 24], ['Sumter', 382], ['Talbot', 26], ['Taliaferro', 0], ['Tattnall', 9], ['Taylor', 17], ['Telfair', 28], ['Terrell', 184], ['Thomas', 190], ['Tift', 122], ['Toombs', 31], ['Towns', 22], ['Treutlen', 3], ['Troup', 150], ['Turner', 68], ['Twiggs', 8], ['Union', 33], ['Unknown', 652], ['Upson', 222], ['Walker', 60], ['Walton', 129], ['Ware', 127], ['Warren', 12], ['Washington', 43], ['Wayne', 13], ['Webster', 10], ['Wheeler', 5], ['White', 63], ['Whitfield', 111], ['Wilcox', 90], ['Wilkes', 25], ['Wilkinson', 35], ['Worth', 158], ['Glascock', 30]]
for i in range(len(GA_name)):
    pos.append(float(POSITIVE.iloc[i,0]))
    name.append(GA_name.iloc[i,0])
pos.append(30)
name.append('Glascock')
MAP_data=[list(z) for z in zip(name,pos)]
print(MAP_data)

NAME_MAP_DATA={
    "Appling": "Appling",
    "Atkinson": "Atkinson",
    "Bacon": "Bacon",
    "Baker": "Baker",
    "Baldwin": "Baldwin"
}
#MAP_data=[['Appling', 72], ['Atkinson', 9], ['Bacon', 25], ['Baker', 23], ['Baldwin', 226], ['Banks', 25], ['Barrow', 141], ['Bartow', 320], ['Ben Hill', 26], ['Berrien', 17], ['Bibb', 312], ['Bleckley', 19], ['Brantley', 23], ['Brooks', 59], ['Bryan', 54], ['Bulloch', 40], ['Burke', 86], ['Butts', 153], ['Calhoun', 103], ['Camden', 33], ['Candler', 7], ['Carroll', 375], ['Catoosa', 47], ['Charlton', 11], ['Chatham', 230], ['Chattahoochee', 12], ['Chattooga', 16], ['Cherokee', 476], ['Clarke', 155], ['Clay', 23], ['Clayton', 724], ['Clinch', 8], ['Cobb', 1672], ['Coffee', 141], ['Colquitt', 187], ['Columbia', 162], ['Cook', 25], ['Coweta', 209], ['Crawford', 17], ['Crisp', 167], ['Dade', 16], ['Dawson', 61], ['DeKalb', 2065], ['Decatur', 86], ['Dodge', 28], ['Dooly', 129], ['Dougherty', 1531], ['Douglas', 325], ['Early', 213], ['Echols', 5], ['Effingham', 36], ['Elbert', 23], ['Emanuel', 21], ['Evans', 5], ['Fannin', 30], ['Fayette', 177], ['Floyd', 145], ['Forsyth', 308], ['Franklin', 19], ['Fulton', 2880], ['Gilmer', 69], ['Glynn', 58], ['Gordon', 112], ['Grady', 64], ['Greene', 54], ['Gwinnett', 1843], ['Habersham', 325], ['Hall', 1466], ['Hancock', 51], ['Haralson', 29], ['Harris', 61], ['Hart', 11], ['Heard', 11], ['Henry', 492], ['Houston', 234], ['Irwin', 15], ['Jackson', 97], ['Jasper', 22], ['Jeff Davis', 20], ['Jefferson', 14], ['Jenkins', 16], ['Johnson', 51], ['Jones', 29], ['Lamar', 38], ['Lanier', 9], ['Laurens', 62], ['Lee', 321], ['Liberty', 37], ['Lincoln', 12], ['Long', 5], ['Lowndes', 156], ['Lumpkin', 46], ['Macon', 81], ['Madison', 24], ['Marion', 42], ['McDuffie', 45], ['McIntosh', 6], ['Meriwether', 53], ['Miller', 33], ['Mitchell', 318], ['Monroe', 24], ['Montgomery', 2], ['Morgan', 27], ['Murray', 32], ['Muscogee', 313], ['Newton', 200], ['Non-Georgia Resident', 1080], ['Oconee', 66], ['Oglethorpe', 49], ['Paulding', 190], ['Peach', 52], ['Pickens', 25], ['Pierce', 55], ['Pike', 40], ['Polk', 59], ['Pulaski', 31], ['Putnam', 42], ['Quitman', 4], ['Rabun', 14], ['Randolph', 161], ['Richmond', 411], ['Rockdale', 191], ['Schley', 16], ['Screven', 15], ['Seminole', 29], ['Spalding', 211], ['Stephens', 81], ['Stewart', 24], ['Sumter', 382], ['Talbot', 26], ['Taliaferro', 0], ['Tattnall', 9], ['Taylor', 17], ['Telfair', 28], ['Terrell', 184], ['Thomas', 190], ['Tift', 122], ['Toombs', 31], ['Towns', 22], ['Treutlen', 3], ['Troup', 150], ['Turner', 68], ['Twiggs', 8], ['Union', 33], ['Unknown', 652], ['Upson', 222], ['Walker', 60], ['Walton', 129], ['Ware', 127], ['Warren', 12], ['Washington', 43], ['Wayne', 13], ['Webster', 10], ['Wheeler', 5], ['White', 63], ['Whitfield', 111], ['Wilcox', 90], ['Wilkes', 25], ['Wilkinson', 35], ['Worth', 158], ['Glascock', 30]]

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
            title="GA疫情情况",
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
    .render("GA_test.html")
)