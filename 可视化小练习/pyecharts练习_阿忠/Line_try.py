import csv
import pandas
import pyecharts.options as opts
from pyecharts.charts import Line


def get_csv_data(path):
    data_first = []
    state_first = []
    with open(path, "r") as f:
        L = list(csv.reader(f))
        for i, line in enumerate(L):
            if i == 0:
                continue
            else:
                print("正在处理第{}行数据".format(i))
                state_first.append(line[1])
                data_first.append(line[2])
    data_last = []
    # 筛选出“WA”州的数据
    for i in range(len(state_first)):
        if state_first[i] == "WA":
            data_last.append(data_first[i])
    return data_last


def Draw_data_Line(data, dates_list):
    (
        Line()
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Washington Positive_situation"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", is_show=True),
            xaxis_opts=opts.AxisOpts(name="Dates", type_="category", boundary_gap=False),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name="Cumularive Cases",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
        .add_xaxis(xaxis_data=dates_list)
        .add_yaxis(
            series_name="Cumularive Cases",
            y_axis=data,
            linestyle_opts=opts.LineStyleOpts(width=3),
            symbol="emptyCircle",
            is_symbol_show=False,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .render("Line_try.html")
    )


if __name__ == '__main__':
    path = "daily.csv"
    data = (get_csv_data(path))
    data.reverse()
    data = list(map(int, data))
    list_len = len(data)
    dates = pandas.date_range(end='20200520', periods=list_len)
    dates_list = [date.strftime('%m-%d') for date in dates]
    Draw_data_Line(data, dates_list)
    print("Finished All")

