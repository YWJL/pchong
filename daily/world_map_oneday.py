import csv
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode


def get_data(confirm_data, death_data):
    data_confirm = []
    with open(confirm_data, 'r', encoding='gbk') as f1:
        text_confirm = csv.reader(f1)
        for line in text_confirm:
            data_confirm.append(line)
        data_confirm.remove(data_confirm[0])
        data_confirm.remove(data_confirm[0])

        count1 = 0
        Countries_confirm_name = []
        confirm_data_list_all = []
        Countries_confirm = data_confirm[0]
        for i in Countries_confirm:
            if i == 'Zambia':
                Countries_confirm_name.append(i)
                confirm_data_list_all.append(data_confirm[-1][count1])
                break
            else:
                Countries_confirm_name.append(i)
                confirm_data_list_all.append(data_confirm[-1][count1])
                count1 = count1 + 1
        Countries_confirm_name.remove(Countries_confirm_name[0])
        confirm_data_list_all.remove(confirm_data_list_all[0])

    count2 = 0
    data_death = []
    death_data_list = []
    Countries_death_name = []
    with open(death_data, 'r', encoding='gbk') as f2:
        text_death = csv.reader(f2)
        for line in text_death:
            data_death.append(line)
        data_death.remove(data_death[0])
        data_death.remove(data_death[0])

        Countries_death = data_death[0]
        for i in Countries_death:
            if i == 'Yemen':
                Countries_death_name.append(i)
                death_data_list.append(data_death[-1][count2])
                break
            else:
                Countries_death_name.append(i)
                death_data_list.append(data_death[-1][count2])
                count2 = count2 + 1
        Countries_death_name.remove(Countries_death_name[0])
        death_data_list.remove(death_data_list[0])

        death_data_list = data_death[-1]
        death_data_list.remove(death_data_list[0])

    return Countries_confirm_name, confirm_data_list_all, Countries_death_name, death_data_list


def draw_map(data):
    c = {
        Map()
        .add(
            series_name="confirm_data",
            data_pair=[list(z) for z in zip(data[0], data[1])],
            maptype='world',
            is_map_symbol_show=False)
        .add(
            series_name="death_data",
            data_pair=[list(z) for z in zip(data[2], data[3])],
            maptype='world',
            is_map_symbol_show=False,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False,))
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="World_Epidemic_Data",
                subtitle='World_Epidemic_data_0526',
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                trigger='item',
                trigger_on='mousemove|click',
                # formatter="{b}<br/>{a}:{c}"
                formatter=JsCode("""
                function(a){
            var result = [ ], counter = 0;
            var num_array = a.data.toString().split('.');
            var num = num_array[0];
            var newstr = '';
            for (var i = num.length - 1; i >= 0; i--) {
                result.unshift(num[i]);
            }
                return result.join('');
            }
                """)
            ),
            visualmap_opts=opts.VisualMapOpts(max_=400000),
        )
        .render("world_map_oneday.html")
    }
    pass


if __name__ == '__main__':
    confirm_data = '20200526-world-confirm-data.json.csv'
    death_data = '20200527-world-death-data.json.csv'
    data = get_data(confirm_data, death_data)
    draw_map(data)
