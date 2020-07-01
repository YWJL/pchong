import csv
from typing import List
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Line

Countries_name = []
Data_Text = []
Data = []
Date = []
Day = []
ratio = []
World = []
Day_data = []
Top_ten = []
with open('20200605-world-confirm-data.json.csv', 'r') as f:
    Text = csv.reader(f)
    for Line in Text:
        Data_Text.append(Line)

print('正在提取CSV数据...')
for i in range(1, len(Data_Text[2])):
    # if Data_Text[2][i] == 'World':
    #     print(i)
    if Data_Text[2][i] == 'US':
        Countries_name.append('United States')
        continue
    if Data_Text[2][i] == 'Zimbabwe':
        # print(i)
        Countries_name.append(Data_Text[2][i])
        break
    else:
        Countries_name.append(Data_Text[2][i])
Countries_name.remove(Countries_name[156])

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

A = []
N = []
for i in range(len(Data_Text)):
    a = []
    n = []
    for j in range(len(Countries_name)):
        a.append(Data_Text[i][j])
        n.append(Countries_name[j])
    A.append(a)
    N.append(n)

for i in range(len(A)):
    for j in range(len(Countries_name)):
        for h in range(j, len(Countries_name)):
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
    for j in range(len(Countries_name)):
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

BAP = []
for i in range(len(Data)):
    d = []
    for j in range(0, 20):
        d.append(Data[i][j])
    BAP.append(d)

print('正在列举已封装的数据...')
M_data = [
    {'time': Date[0], 'data': Data[0]}, {'time': Date[1], 'data': Data[1]},
    {'time': Date[2], 'data': Data[2]}, {'time': Date[3], 'data': Data[3]},
    {'time': Date[4], 'data': Data[4]}, {'time': Date[5], 'data': Data[5]},
    {'time': Date[6], 'data': Data[6]}, {'time': Date[7], 'data': Data[7]},
    {'time': Date[8], 'data': Data[8]}, {'time': Date[9], 'data': Data[9]},
    {'time': Date[10], 'data': Data[10]}, {'time': Date[11], 'data': Data[11]},
    {'time': Date[12], 'data': Data[12]}, {'time': Date[13], 'data': Data[13]},
    {'time': Date[14], 'data': Data[14]}, {'time': Date[15], 'data': Data[15]},
    {'time': Date[16], 'data': Data[16]}, {'time': Date[17], 'data': Data[17]},
    {'time': Date[18], 'data': Data[18]}, {'time': Date[19], 'data': Data[19]},
    {'time': Date[20], 'data': Data[20]}, {'time': Date[21], 'data': Data[21]},
    {'time': Date[22], 'data': Data[22]}, {'time': Date[23], 'data': Data[23]},
    {'time': Date[24], 'data': Data[24]}, {'time': Date[25], 'data': Data[25]},
    {'time': Date[26], 'data': Data[26]}, {'time': Date[27], 'data': Data[27]},
    {'time': Date[28], 'data': Data[28]}, {'time': Date[29], 'data': Data[29]},
    {'time': Date[30], 'data': Data[30]}, {'time': Date[31], 'data': Data[31]},
    {'time': Date[32], 'data': Data[32]}, {'time': Date[33], 'data': Data[33]},
    {'time': Date[34], 'data': Data[34]}, {'time': Date[35], 'data': Data[35]},
    {'time': Date[36], 'data': Data[36]}, {'time': Date[37], 'data': Data[37]},
    {'time': Date[38], 'data': Data[38]}, {'time': Date[39], 'data': Data[39]},
    {'time': Date[40], 'data': Data[40]}, {'time': Date[41], 'data': Data[41]},
    {'time': Date[42], 'data': Data[42]}, {'time': Date[43], 'data': Data[43]},
    {'time': Date[44], 'data': Data[44]}, {'time': Date[45], 'data': Data[45]},
    {'time': Date[46], 'data': Data[46]}, {'time': Date[47], 'data': Data[47]},
    {'time': Date[48], 'data': Data[48]}, {'time': Date[49], 'data': Data[49]},
    {'time': Date[50], 'data': Data[50]}, {'time': Date[51], 'data': Data[51]},
    {'time': Date[52], 'data': Data[52]}, {'time': Date[53], 'data': Data[53]},
    {'time': Date[54], 'data': Data[54]}, {'time': Date[55], 'data': Data[55]},
    {'time': Date[56], 'data': Data[56]}, {'time': Date[57], 'data': Data[57]},
    {'time': Date[58], 'data': Data[58]}, {'time': Date[59], 'data': Data[59]},
    {'time': Date[60], 'data': Data[60]}, {'time': Date[61], 'data': Data[61]},
    {'time': Date[62], 'data': Data[62]}, {'time': Date[63], 'data': Data[63]},
    {'time': Date[64], 'data': Data[64]}, {'time': Date[65], 'data': Data[65]},
    {'time': Date[66], 'data': Data[66]}, {'time': Date[67], 'data': Data[67]},
    {'time': Date[68], 'data': Data[68]}, {'time': Date[69], 'data': Data[69]},
    {'time': Date[70], 'data': Data[70]}, {'time': Date[71], 'data': Data[71]},
    {'time': Date[72], 'data': Data[72]}, {'time': Date[73], 'data': Data[73]},
    {'time': Date[74], 'data': Data[74]}, {'time': Date[75], 'data': Data[75]},
    {'time': Date[76], 'data': Data[76]}, {'time': Date[77], 'data': Data[77]},
    {'time': Date[78], 'data': Data[78]}, {'time': Date[79], 'data': Data[79]},
    {'time': Date[80], 'data': Data[80]}, {'time': Date[81], 'data': Data[81]},
    {'time': Date[82], 'data': Data[82]}, {'time': Date[83], 'data': Data[83]},
    {'time': Date[84], 'data': Data[84]}, {'time': Date[85], 'data': Data[85]},
    {'time': Date[86], 'data': Data[86]}, {'time': Date[87], 'data': Data[87]},
    {'time': Date[88], 'data': Data[88]}, {'time': Date[89], 'data': Data[89]},
    {'time': Date[90], 'data': Data[90]}, {'time': Date[91], 'data': Data[91]},
    {'time': Date[92], 'data': Data[92]}, {'time': Date[93], 'data': Data[93]},
    {'time': Date[94], 'data': Data[94]}, {'time': Date[95], 'data': Data[95]},
    {'time': Date[96], 'data': Data[96]}, {'time': Date[97], 'data': Data[97]},
    {'time': Date[98], 'data': Data[98]}, {'time': Date[99], 'data': Data[99]},
    {'time': Date[100], 'data': Data[100]}, {'time': Date[101], 'data': Data[101]},
    {'time': Date[102], 'data': Data[102]}, {'time': Date[103], 'data': Data[103]},
    {'time': Date[104], 'data': Data[104]}, {'time': Date[105], 'data': Data[105]},
    {'time': Date[106], 'data': Data[106]}, {'time': Date[107], 'data': Data[107]},
    {'time': Date[108], 'data': Data[108]}, {'time': Date[109], 'data': Data[109]},
    {'time': Date[110], 'data': Data[110]}, {'time': Date[111], 'data': Data[111]},
    {'time': Date[112], 'data': Data[112]}, {'time': Date[113], 'data': Data[113]},
    {'time': Date[114], 'data': Data[114]}, {'time': Date[115], 'data': Data[115]},
    {'time': Date[116], 'data': Data[116]}, {'time': Date[117], 'data': Data[117]},
    {'time': Date[118], 'data': Data[118]}, {'time': Date[119], 'data': Data[119]},
    {'time': Date[120], 'data': Data[120]}, {'time': Date[121], 'data': Data[121]},
    {'time': Date[122], 'data': Data[122]}, {'time': Date[123], 'data': Data[123]},
    {'time': Date[124], 'data': Data[124]}, {'time': Date[125], 'data': Data[125]},
    {'time': Date[126], 'data': Data[126]}, {'time': Date[127], 'data': Data[127]},
    {'time': Date[128], 'data': Data[128]}, {'time': Date[129], 'data': Data[129]},
    {'time': Date[130], 'data': Data[130]}, {'time': Date[131], 'data': Data[131]},
    {'time': Date[132], 'data': Data[132]}, {'time': Date[133], 'data': Data[133]},
    {'time': Date[134], 'data': Data[134]}
]

BAP_data = [
    {'time': Date[0], 'data': BAP[0]}, {'time': Date[1], 'data': BAP[1]},
    {'time': Date[2], 'data': BAP[2]}, {'time': Date[3], 'data': BAP[3]},
    {'time': Date[4], 'data': BAP[4]}, {'time': Date[5], 'data': BAP[5]},
    {'time': Date[6], 'data': BAP[6]}, {'time': Date[7], 'data': BAP[7]},
    {'time': Date[8], 'data': BAP[8]}, {'time': Date[9], 'data': BAP[9]},
    {'time': Date[10], 'data': BAP[10]}, {'time': Date[11], 'data': BAP[11]},
    {'time': Date[12], 'data': BAP[12]}, {'time': Date[13], 'data': BAP[13]},
    {'time': Date[14], 'data': BAP[14]}, {'time': Date[15], 'data': BAP[15]},
    {'time': Date[16], 'data': BAP[16]}, {'time': Date[17], 'data': BAP[17]},
    {'time': Date[18], 'data': BAP[18]}, {'time': Date[19], 'data': BAP[19]},
    {'time': Date[20], 'data': BAP[20]}, {'time': Date[21], 'data': BAP[21]},
    {'time': Date[22], 'data': BAP[22]}, {'time': Date[23], 'data': BAP[23]},
    {'time': Date[24], 'data': BAP[24]}, {'time': Date[25], 'data': BAP[25]},
    {'time': Date[26], 'data': BAP[26]}, {'time': Date[27], 'data': BAP[27]},
    {'time': Date[28], 'data': BAP[28]}, {'time': Date[29], 'data': BAP[29]},
    {'time': Date[30], 'data': BAP[30]}, {'time': Date[31], 'data': BAP[31]},
    {'time': Date[32], 'data': BAP[32]}, {'time': Date[33], 'data': BAP[33]},
    {'time': Date[34], 'data': BAP[34]}, {'time': Date[35], 'data': BAP[35]},
    {'time': Date[36], 'data': BAP[36]}, {'time': Date[37], 'data': BAP[37]},
    {'time': Date[38], 'data': BAP[38]}, {'time': Date[39], 'data': BAP[39]},
    {'time': Date[40], 'data': BAP[40]}, {'time': Date[41], 'data': BAP[41]},
    {'time': Date[42], 'data': BAP[42]}, {'time': Date[43], 'data': BAP[43]},
    {'time': Date[44], 'data': BAP[44]}, {'time': Date[45], 'data': BAP[45]},
    {'time': Date[46], 'data': BAP[46]}, {'time': Date[47], 'data': BAP[47]},
    {'time': Date[48], 'data': BAP[48]}, {'time': Date[49], 'data': BAP[49]},
    {'time': Date[50], 'data': BAP[50]}, {'time': Date[51], 'data': BAP[51]},
    {'time': Date[52], 'data': BAP[52]}, {'time': Date[53], 'data': BAP[53]},
    {'time': Date[54], 'data': BAP[54]}, {'time': Date[55], 'data': BAP[55]},
    {'time': Date[56], 'data': BAP[56]}, {'time': Date[57], 'data': BAP[57]},
    {'time': Date[58], 'data': BAP[58]}, {'time': Date[59], 'data': BAP[59]},
    {'time': Date[60], 'data': BAP[60]}, {'time': Date[61], 'data': BAP[61]},
    {'time': Date[62], 'data': BAP[62]}, {'time': Date[63], 'data': BAP[63]},
    {'time': Date[64], 'data': BAP[64]}, {'time': Date[65], 'data': BAP[65]},
    {'time': Date[66], 'data': BAP[66]}, {'time': Date[67], 'data': BAP[67]},
    {'time': Date[68], 'data': BAP[68]}, {'time': Date[69], 'data': BAP[69]},
    {'time': Date[70], 'data': BAP[70]}, {'time': Date[71], 'data': BAP[71]},
    {'time': Date[72], 'data': BAP[72]}, {'time': Date[73], 'data': BAP[73]},
    {'time': Date[74], 'data': BAP[74]}, {'time': Date[75], 'data': BAP[75]},
    {'time': Date[76], 'data': BAP[76]}, {'time': Date[77], 'data': BAP[77]},
    {'time': Date[78], 'data': BAP[78]}, {'time': Date[79], 'data': BAP[79]},
    {'time': Date[80], 'data': BAP[80]}, {'time': Date[81], 'data': BAP[81]},
    {'time': Date[82], 'data': BAP[82]}, {'time': Date[83], 'data': BAP[83]},
    {'time': Date[84], 'data': BAP[84]}, {'time': Date[85], 'data': BAP[85]},
    {'time': Date[86], 'data': BAP[86]}, {'time': Date[87], 'data': BAP[87]},
    {'time': Date[88], 'data': BAP[88]}, {'time': Date[89], 'data': BAP[89]},
    {'time': Date[90], 'data': BAP[90]}, {'time': Date[91], 'data': BAP[91]},
    {'time': Date[92], 'data': BAP[92]}, {'time': Date[93], 'data': BAP[93]},
    {'time': Date[94], 'data': BAP[94]}, {'time': Date[95], 'data': BAP[95]},
    {'time': Date[96], 'data': BAP[96]}, {'time': Date[97], 'data': BAP[97]},
    {'time': Date[98], 'data': BAP[98]}, {'time': Date[99], 'data': BAP[99]},
    {'time': Date[100], 'data': BAP[100]}, {'time': Date[101], 'data': BAP[101]},
    {'time': Date[102], 'data': BAP[102]}, {'time': Date[103], 'data': BAP[103]},
    {'time': Date[104], 'data': BAP[104]}, {'time': Date[105], 'data': BAP[105]},
    {'time': Date[106], 'data': BAP[106]}, {'time': Date[107], 'data': BAP[107]},
    {'time': Date[108], 'data': BAP[108]}, {'time': Date[109], 'data': BAP[109]},
    {'time': Date[110], 'data': BAP[110]}, {'time': Date[111], 'data': BAP[111]},
    {'time': Date[112], 'data': BAP[112]}, {'time': Date[113], 'data': BAP[113]},
    {'time': Date[114], 'data': BAP[114]}, {'time': Date[115], 'data': BAP[115]},
    {'time': Date[116], 'data': BAP[116]}, {'time': Date[117], 'data': BAP[117]},
    {'time': Date[118], 'data': BAP[118]}, {'time': Date[119], 'data': BAP[119]},
    {'time': Date[120], 'data': BAP[120]}, {'time': Date[121], 'data': BAP[121]},
    {'time': Date[122], 'data': BAP[122]}, {'time': Date[123], 'data': BAP[123]},
    {'time': Date[124], 'data': BAP[124]}, {'time': Date[125], 'data': BAP[125]},
    {'time': Date[126], 'data': BAP[126]}, {'time': Date[127], 'data': BAP[127]},
    {'time': Date[128], 'data': BAP[128]}, {'time': Date[129], 'data': BAP[129]},
    {'time': Date[130], 'data': BAP[130]}, {'time': Date[131], 'data': BAP[131]},
    {'time': Date[132], 'data': BAP[132]}, {'time': Date[133], 'data': BAP[133]},
    {'time': Date[134], 'data': BAP[134]}
]

minNum = 0
maxNum = 1872660
time_list = Date
# time_list = [str(d) + '年' for d in range(len(Date))]
total_num = World


def get_days_chart(year: str):
    map_data = [
        [[x['name'], x['value']] for x in d['data']] for d in M_data if d['time'] == year
    ][0]
    Bar_and_Pie_data = [
        [[x['name'], x['value']] for x in d['data']] for d in BAP_data if d['time'] == year
    ][0]
    min_data, max_data = (minNum, maxNum)
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
            center=[100, 20],
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
                title='' + str(year) + '世界疫情概况（单位：人）',
                subtitle='',
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

    # line_chart = (
    #     Line()
    #     .add_xaxis(time_list)
    #     .add_yaxis('', total_num)
    #     .add_yaxis(
    #         '',
    #         data_mark,
    #         markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max')])
    #     )
    #     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    #     .set_global_opts(
    #         title_opts=opts.TitleOpts(
    #             title='世界疫情总况2020-01-23到2020-06-05（单位：人）', pos_left='72%', pos_top='5%'
    #         )
    #     )
    # )

    bar_x_data = [x[0] for x in Bar_and_Pie_data]
    bar_y_data = [{'name': x[0], 'value': x[1][0]} for x in Bar_and_Pie_data]
    print(bar_x_data)
    print(bar_y_data)
    bar = (
        Bar()
        .add_xaxis(xaxis_data=bar_x_data)
        .add_yaxis(
            series_name='',
            yaxis_data=bar_y_data,
            label_opts=opts.LabelOpts(
                is_show=True, position='right', formatter='{b} : {c}'
            )
        )
        .reversal_axis()
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                max_=maxNum, axislabel_opts=opts.LabelOpts(is_show=False)
            ),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left='10',
                pos_top='top',
                range_text=['High', 'Low'],
                range_color=['lightskyblue', 'yellow', 'orangered'],
                textstyle_opts=opts.TextStyleOpts(color='#ddd'),
                min_=min_data,
                max_=max_data
            )
        )
    )

    pie_data = [[x[0], x[1][0]] for x in Bar_and_Pie_data]
    print(pie_data)
    pie = (
        Pie()
        .add(
            series_name="",
            data_pair=pie_data,
            radius=["10%", "20%"],
            center=["85%", "85%"],
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=1, border_color="rgba(0,0,0,0.3)"
            ),
        )
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b}：{d}%"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    grid_chart = (
        Grid()
        .add(
            bar,
            grid_opts=opts.GridOpts(
                pos_left="10", pos_right="45%", pos_top="50%", pos_bottom="5"
            ),
        )
        #     .add(
        #     line_chart,
        #     grid_opts=opts.GridOpts(
        #         pos_left="65%", pos_right="80", pos_top="10%", pos_bottom="50%"
        #     ),
        # )
        .add(pie, grid_opts=opts.GridOpts(pos_left="45%", pos_top="60%"))
        .add(map_chart, grid_opts=opts.GridOpts())
    )

    return grid_chart


if __name__ == '__main__':
    print('正在绘制地图...')
    timeline = Timeline(
        init_opts=opts.InitOpts(width='1000px', height='500px', theme=ThemeType.DARK)
    )
    for y in time_list:
        g = get_days_chart(year=y)
        timeline.add(g, time_point=str(y))

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

    timeline.render('Map_World_from_0123_to_0605.html')
    print('地图绘制结束，打开(html)文件进行查看！')
