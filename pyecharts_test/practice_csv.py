# 这是一个对csv形式进行解析的demo
import pandas as pd
from pyecharts.charts import Bar, Page


def csv_data_show(csv_file, x_head_key):
    # 这个函数的目的是去读取csv内部的内容
    df = pd.read_csv(csv_file, encoding='gbk')
    # df = pd.DataFrame(df)
    cols_len = len(df.columns)
    # print(cols_len)   9
    rows_len = len(df)
    # print(rows_len)
    # x_head = [str(c).strip() for c in df[x_head_key]]
    # temp = set(x_head)
    # print(temp)
    res = df.groupby([x_head_key], as_index=False)['rate'].agg({'cnt': 'count'})
    tag_list = res["rate"]
    tag_name = tag_list[2:]
    count_list = res['cnt']
    count = count_list[2:]
    bars_show(tag_name, count)


def csv_local_show():
    df = pd.read_csv()


def bars_show(x, y):
    bar = Bar()
    bar.add_xaxis(list(x))
    bar.add_yaxis("风险等级", list(y))
    bar.render()



csv_data_show("result1.csv", 'rate')