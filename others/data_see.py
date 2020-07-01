import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd
import re
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Pie
pd.set_option('display.width', 1000, 'display.max_rows', 1000)
"""""
csv_file = "clean_data.csv"
csv_data = pd.read_csv(csv_file, low_memory = False)#防止弹出警告
csv_df = pd.DataFrame(csv_data)
"""""
data = pd.DataFrame(pd.read_csv('clean_data.csv'),columns=['X','sex','age','area','time','E','F','G'])

data.sex = pd.read_csv('clean_data.csv',usecols=[1])
data.age = pd.read_csv('clean_data.csv',usecols=[2])
data.area = pd.read_csv('clean_data.csv',usecols=[3])
data.time = pd.read_csv('clean_data.csv',usecols=[4])






sex_1 = 0
sex_2 = 0
count = 1
for i in np.arange(len(data)):
    i=i+1
print(i)
sex1=[]
sex2=[]
all=[]
data_num=[]

for i in np.arange(len(data)):
    data.iloc[i,4]=data.iloc[i,4].replace('月','.')
for i in np.arange(len(data)-1):
    if data.iloc[i,4] !=data.iloc[i+1,4]:
        data_num.append(data.iloc[i,4])

a=0
b=0
time=float(data.iloc[0,4])
for i in np.arange(len(data)-1):
    sex_1=0
    sex_2=0
    if float(data.iloc[i,4]) - time >=0.009 or float(data.iloc[i,4]) - time <0 or i==0 :
        for j in range(i, len(data) - 1):
            if float(data.iloc[j, 4]) - float(data.iloc[i, 4]) >= 0.009 and float(data.iloc[j, 4]) - float(
                    data.iloc[i, 4]) <= 0.011:
                if data.iloc[j, 1] == '男':
                    sex_1 = sex_1 + 1
                if data.iloc[j, 1] == '女':
                    sex_2 = sex_2 + 1
                a=a+sex_1
                b=b+sex_2
                sex1.append(a)
                sex2.append(b)
                time = float(data.iloc[i, 4])
                print(time)
                break
            if float(data.iloc[j, 4]) - float(data.iloc[i, 4]) >= 0.79 and float(data.iloc[j, 4]) - float(
                    data.iloc[i, 4]) <= 0.80:
                if data.iloc[j, 1] == '男':
                    sex_1 = sex_1 + 1
                if data.iloc[j, 1] == '女':
                    sex_2 = sex_2 + 1
                a=a+sex_1
                b=b+sex_2
                sex1.append(a)
                sex2.append(b)
                time = float(data.iloc[i, 4])
                print(time)
                break
            if float(data.iloc[j, 4]) - float(data.iloc[i, 4]) > 0.09 and float(data.iloc[j, 4]) - float(
                    data.iloc[i, 4]) < 0.11:
                if data.iloc[j, 1] == '男':
                    sex_1 = sex_1 + 1
                if data.iloc[j, 1] == '女':
                    sex_2 = sex_2 + 1
                a=a+sex_1
                b=b+sex_2
                sex1.append(a)
                sex2.append(b)
                time = float(data.iloc[i, 4])
                print(time)
                break
            if float(data.iloc[j, 4]) - float(data.iloc[i, 4]) > -0.80 and float(data.iloc[j, 4]) - float(
                    data.iloc[i, 4]) < -0.79:
                if data.iloc[j, 1] == '男':
                    sex_1 = sex_1 + 1
                if data.iloc[j, 1] == '女':
                    sex_2 = sex_2 + 1
                a=a+sex_1
                b=b+sex_2
                sex1.append(a)
                sex2.append(b)
                time = float(data.iloc[i, 4])
                print(time)
                break



print(len(sex1))
print(sex1)
print(len(sex2))
print(sex2)


count=0

for i in np.arange(len(data)-1):
    count = 0
    for j in range(i,len(data)-1):
        if data.iloc[i,4] == data.iloc[j,4]:
            count=count+1
    data.iloc[i,6]=count
a=0
time=float(data.iloc[0,4])
for i in np.arange(len(data)-1):
    if float(data.iloc[i,4]) - time >=0.009 or float(data.iloc[i,4]) - time <0 or i==0:
        for j in range(i, len(data) - 1):
            if float(data.iloc[j, 4]) - float(data.iloc[i, 4]) >= 0.009 and float(data.iloc[j, 4]) - float(
                    data.iloc[i, 4]) <= 0.011:
                all.append(data.iloc[i, 6])
                time = float(data.iloc[i, 4])
                #print(time)
                break
            if float(data.iloc[j, 4]) - float(data.iloc[i, 4]) >= 0.79 and float(data.iloc[j, 4]) - float(
                    data.iloc[i, 4]) <= 0.80:
                all.append(data.iloc[i, 6])
                time = float(data.iloc[i, 4])
                #print(time)
                break
            if float(data.iloc[j, 4]) - float(data.iloc[i, 4]) > 0.09 and float(data.iloc[j, 4]) - float(
                    data.iloc[i, 4]) < 0.11:
                all.append(data.iloc[i, 6])
                time = float(data.iloc[i, 4])
                #print(time,i,j)
                break
            if float(data.iloc[j, 4]) - float(data.iloc[i, 4]) > -0.80 and float(data.iloc[j, 4]) - float(
                    data.iloc[i, 4]) < -0.79:
                all.append(data.iloc[i, 6])
                time = float(data.iloc[i, 4])
                #print(time,i,j)
                break
#观察数据，发现最后3个数据，2.12-2.17并未处理好
people=[]
a=0
for i in np.arange(len(all)):
    a=a+all[i]
    people.append(a)
print(people)



# print(all)
print(data)
#print(data_num)
#print(sex2)
#print(sex1)

import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
""""
(
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=data_num)
    .add_yaxis(
        series_name="男",
        y_axis=sex1,
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
    .add_yaxis(
        series_name="女", y_axis=sex2, linestyle_opts=opts.LineStyleOpts(width=2)
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="新型冠状病毒感染情况（1）", pos_left="center"),
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/> {c}"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        xaxis_opts=opts.AxisOpts(type_="category", name="日期"),
        yaxis_opts=opts.AxisOpts(
            type_="log",
            name="感染人数",
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
    )
    .render("answer_1.html")
)
"""
GYYQ=0
TC=0
CS=0
XCQ=0
WJQ=0
GSQ=0
WZQ=0
KSS=0
GXQ=0
gyyq=['工业园区']
tc=['太仓市']
cs=['常熟市']
xcq=['相城区']
wjq=['吴江区']
gsq=['姑苏区']
wzq=['吴中区']
kss=['昆山市']
gxq=['高新区']
print(re.findall('工业园区',data.iloc[0,3]))
for i in range(len(data)):
    if re.findall('工业园区',data.iloc[i,3])==gyyq:
        GYYQ=GYYQ+1
    if re.findall('太仓市',data.iloc[i,3])==tc:
        TC=TC+1
    if re.findall('常熟市', data.iloc[i, 3]) == cs:
        CS=CS+1
    if re.findall('相城区', data.iloc[i, 3]) == xcq:
        XCQ=XCQ+1
    if re.findall('吴江区', data.iloc[i, 3]) == wjq:
        WJQ=WJQ+1
    if re.findall('姑苏区', data.iloc[i, 3]) == gsq:
        GSQ=GSQ+1
    if re.findall('吴中区', data.iloc[i, 3]) == wzq:
        WZQ=WZQ+1
    if re.findall('昆山市', data.iloc[i, 3]) == kss:
        KSS=KSS+1
    if re.findall('高新区', data.iloc[i, 3]) == gxq:
        GXQ=GXQ+1
data_are=[]
data_are.append(GYYQ)
data_are.append(TC)
data_are.append(CS)
data_are.append(XCQ)
data_are.append(WJQ)
data_are.append(GXQ)
data_are.append(WZQ)
data_are.append(KSS)
data_are.append(GXQ)
# print(data_are)
# print(sum(data_are))
#
# print(GYYQ)
# print(gyyq)

x_data = ["工业园区", "太仓市", "常熟市", "相城区", "吴江区","姑苏区","吴中区","昆山市","高新区"]
y_data = data_are
data_pair = [list(z) for z in zip(x_data, y_data)]
print(data_pair)
data_pair.sort(key=lambda x: x[1])
print(data_pair.sort())

c = (
    Pie()
    .add(
        "",
        data_pair,
        center=["35%", "50%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="苏州各地区新型冠状病毒感染情况（1.22-2.17）"),
        legend_opts=opts.LegendOpts(pos_left="55%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("answer_3(1).html")
)

(
    Pie(init_opts=opts.InitOpts(width="1600px", height="800px", bg_color="#2c343c"))
    .add(
        series_name="地区",
        data_pair=data_pair,
        rosetype="radius",
        # radius="55%",
        # center=["50%", "50%"],
        label_opts=opts.LabelOpts(is_show=False, position="center"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="苏州各地区新型冠状病毒感染情况（1.22-2.17）",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(color="#fff"),
        ),
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(color="rgba(255, 255, 255, 0.3)"),
    )
    .render("answer_3.html")
)



(
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=data_num)
    .add_yaxis(
        series_name="疫情感染人数",
        y_axis=people,
        linestyle_opts=opts.LineStyleOpts(width=2),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="新型冠状病毒感染情况（1）", pos_left="center"),
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/> {c}"),
        legend_opts=opts.LegendOpts(pos_left="left"),
        xaxis_opts=opts.AxisOpts(type_="category", name="日期"),
        yaxis_opts=opts.AxisOpts(
            type_="log",
            name="感染人数",
            splitline_opts=opts.SplitLineOpts(is_show=True),
            is_scale=True,
        ),
    )
    .render("answer_2.html")
)
print(people)


""""

"""














