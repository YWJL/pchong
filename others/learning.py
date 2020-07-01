import pyecharts.options as opts
from pyecharts.charts import Line

"""
以下，关于预测虚线部分处理的核心，及各个点的标志和大小
Gallery 使用 pyecharts 1.1.0
参考地址: https://www.echartsjs.com/examples/editor.html?c=line-marker

目前无法实现的功能:

1、最低气温的最高值暂时无法和 Echarts 的示例完全复刻


week_name_list = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
high_temperature = [11, 11, 15, 13, 12, 13, 10]
low_temperature = [1, -2, 2, 5, 3, 2, 0]


(
    Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add_xaxis(xaxis_data=week_name_list)
    .add_yaxis(
        series_name="最高气温",
        y_axis=high_temperature,
        symbol="triangle",
        symbol_size=20,
        linestyle_opts=opts.LineStyleOpts(color="green", width=4, type_="dashed"),
        markpoint_opts=opts.MarkPointOpts(
            data=[
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
            ]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[opts.MarkLineItem(type_="average", name="平均值")]
        ),
    )
    .add_yaxis(
        series_name="最低气温",
        y_axis=low_temperature,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem(value=-2, name="周最低", x=1, y=-1.5)]
        ),
        markline_opts=opts.MarkLineOpts(
            data=[
                opts.MarkLineItem(type_="average", name="平均值"),
                opts.MarkLineItem(symbol="none", x="90%", y="max"),
                opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
            ]
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="未来一周气温变化", subtitle="纯属虚构"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        toolbox_opts=opts.ToolboxOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("temperature_change_line_chart.html")
)
"""