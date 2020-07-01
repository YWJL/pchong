import csv
from typing import List
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie

Countries_name = []
Data_Text = []
Data = []
Date = []
Day = []
ratio = []
World = []
Day_data = []
A = []
N = []
M_data = []
with open('20200605-world-confirm-data.json.csv', 'r') as f:
    Text = csv.reader(f)
    for Line in Text:
        Data_Text.append(Line)

print('正在提取CSV数据...')
for i in range(1, len(Data_Text[2])):
    if Data_Text[2][i] == 'World':
        continue
    if Data_Text[2][i] == 'US':
        Countries_name.append('United States')
        continue
    if Data_Text[2][i] == 'Zimbabwe':
        Countries_name.append(Data_Text[2][i])
        break
    else:
        Countries_name.append(Data_Text[2][i])

for i in range(3):
    Data_Text.remove(Data_Text[0])

print('正在处理已提取的数据...')
for i in range(len(Data_Text)):
    World.append(Data_Text[i][157])
    Data_Text[i].remove(Data_Text[i][157])
    Date.append(Data_Text[i][0])
World = list(map(float, World))

for i in range(len(Data_Text)):
    Data_Text[i].remove(Data_Text[i][0])

for i in range(len(Data_Text)):
    for j in range(len(Data_Text[i])):
        if Data_Text[i][j] == '':
            Data_Text[i][j] = '0'
    Data_Text[i] = list(map(float, Data_Text[i]))

for i in range(len(Data_Text)):
    a = []
    n = []
    for j in range(len(Countries_name)):
        if Data_Text[i][j] != 0:
            a.append(Data_Text[i][j])
            n.append(Countries_name[j])
        else:
            continue
    A.append(a)
    N.append(n)

for i in range(len(A)):
    for j in range(len(A[i])):
        for h in range(j, len(A[i])):
            if A[i][j] < A[i][h]:
                A[i][j], A[i][h] = A[i][h], A[i][j]
                N[i][j], N[i][h] = N[i][h], N[i][j]


for i in range(len(A)):
    d = []
    for j in range(len(N[i])):
        t = A[i][j] / World[i] * 100
        d.append(round(t, 4))
    ratio.append(d)

print('正在封装数据...')
for i in range(len(ratio)):
    n = []
    for j in range(len(A[i])):
        n.append(A[i][j])
        n.append(ratio[i][j])
        n.append(N[i][j])
    Day.append(n)

for i in range(len(Day)):
    h = []
    for j in range(0, len(Day[i])-2, 3):
        m = []
        m.append(Day[i][j])
        m.append(Day[i][j+1])
        m.append(Day[i][j+2])
        h.append(m)
    Day_data.append(h)

for i in range(len(Day_data)):
    d = []
    n = ['name', 'value']
    for j in range(len(Day_data[i])):
        v = []
        v.append(N[i][j])
        v.append(Day_data[i][j])
        d.append(dict(zip(n, v)))
    Data.append(d)

print('正在列举已封装的数据...')
for i in range(len(Data)):
    d = []
    n = ['time', 'data']
    d.append(Date[i])
    d.append(Data[i])
    M_data.append(dict(zip(n, d)))


time_list = Date
total_num = World


def get_days_chart(year: str):
    map_data = [
        [[x['name'], x['value']] for x in d['data']] for d in M_data if d['time'] == year
    ][0]
    data_mark: List = []
    i = 0
    for x in time_list:
        if x == year:
            data_mark.append(total_num)
        else:
            data_mark.append('')
        i = i + 1

    map_chart = (
        Map()
        .add(
            series_name="",
            data_pair=map_data,
            zoom=1,
            center=[10, 20],
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
            maptype='world',
            label_opts=opts.LabelOpts(is_show=False)
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title='' + str(year) + '世界各地疫情感染分布概况',
                subtitle='当前数据截止至' + Date[-1],
                pos_left='center',
                pos_top='top',
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(255,255,255, 0.9)"
                )
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                formatter=JsCode(
                    '''function(params){
                    if ('value' in params.data){
                        return params.data.value[2] + ': ' + params.data.value[0];
                    }
                }'''
                )
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left='30',
                pos_top='center',
                range_text=['High', 'Low'],
                range_color=['lightskyblue', 'yellow', 'orangered'],
                textstyle_opts=opts.TextStyleOpts(color='#ddd'),
                min_=0,
                max_=maxNum,
            )
        )
    )

    grid_chart = (
        Grid()
        .add(map_chart, grid_opts=opts.GridOpts())
    )
    return grid_chart


if __name__ == '__main__':
    print('正在绘制地图...')
    timeline = Timeline(
        init_opts=opts.InitOpts(width='1900px', height='900px', theme=ThemeType.DARK)
    )
    i = 0
    for y in time_list:
        minNum = 0
        maxNum = A[i][0]
        g = get_days_chart(year=y)
        timeline.add(g, time_point=str(y))
        i = i + 1

    timeline.add_schema(
        orient='vertical',
        is_auto_play=True,
        is_inverse=True,
        play_interval=500,
        pos_left='null',
        pos_right='5',
        pos_top='20',
        pos_bottom='20',
        width='60',
        label_opts=opts.LabelOpts(is_show=True, color='#fff')
    )

    timeline.render('Map_World_Distribution_of_the_epidemic.html')
    print('地图绘制结束，打开“Map_World_Distribution_of_the_epidemic.html”文件进行查看！')