import csv
from pyecharts.charts import Map
from pyecharts import options as opts


def get_data(confirm_data):
    data = []
    with open(confirm_data, 'r', encoding='utf8') as f:
        text = csv.reader(f)
        for line in text:
            data.append(line)
        data.remove(data[0])
        data.remove(data[0])
        Countries_name = data[0]
        confirm_data_list = data[-1]
        confirm_data_list.remove(confirm_data_list[0])
    return Countries_name, confirm_data_list
    # with open(confirm_data, 'r', encoding='utf-8') as f:
    #     text = json.load(f)
    #     dict_key = [str(key) for key in text[0].keys()]
    #     for i in range(len(text)):
    #         dict_value = [value for value in text[i].values()]
    #
    #     data = [dict(zip(dict_key, dict_value))]
    #     print(data)
    #     # pandas.DataFrame(data).T.to_csv("data.csv")

    pass


def draw_map(data):
    c = {
        Map()
        .add("confirm_data", [list(z) for z in zip(data[0], data[1])], 'world', is_map_symbol_show=False)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="World_Epidemic_Data"),
            visualmap_opts=opts.VisualMapOpts(max_=70000),
        )
        .render("world_map_oneday.html")
    }
    pass


if __name__ == '__main__':
    confirm_data = '20200526-world-confirm-data.json.csv'
    # death_data = '20200526-world-death-data.json'
    data = get_data(confirm_data)
    draw_map(data)