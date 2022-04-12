# 这是我对各种图进行训练的文件
import random

from pyecharts.charts import Bar, Scatter, Line, HeatMap, Pie
from pyecharts import options as opts
from pyecharts.faker import Faker

# 下面是对条形图进行的测试
bar = Bar()
bar.add_xaxis(["数统","计科","物院","文院"])
bar.add_yaxis("学院",[5,8,2,7])

# bar.render_notebook() 这是在notebook上面进行直接展示使用的
# 下面一种是可以直接生产html文件的方法，值得注意的是其中也是可以添加路径参数的
# bar.render()

# 下面是生成散点图一种方式
scatter = Scatter()
scatter.add_xaxis(Faker.choose())
scatter.add_yaxis("商家", Faker.values())

# 这里是一些全局变量的设置，主要是标题和时候画出分隔线，也许其中会有很多不一样的尝试机会
scatter.set_global_opts(
    title_opts=opts.TitleOpts(title="显示分隔线"),
    xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
    yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
)

# scatter.render()

# 下面开始尝试层叠多图
def overlap_line_scatter():
    x = Faker.choose()
    bar = Bar().add_xaxis(x).add_yaxis("商家A", Faker.values()).add_yaxis("商家B", Faker.values())
    line = Line().add_xaxis(x).add_yaxis("商家A", Faker.values()).add_yaxis("商家B", Faker.values())
    bar.overlap(line)
    return bar

# overlap_line_scatter().render()


# 下面开始折线图
def line_xaxis_type():
    c = Line()
    c.add_xaxis(Faker.values())
    c.add_yaxis("商家A", Faker.values())
    c.add_yaxis("商家B", Faker.values())
    c.set_global_opts(title_opts=opts.TitleOpts(title="折线图"), xaxis_opts=opts.AxisOpts(type_="value"))
    return c


# line_xaxis_type().render()

# 下面是对热力图的尝试
def heatmap_base():
    value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    c = HeatMap()
    c.add_xaxis(Faker.clock)
    c.add_yaxis("serise0", Faker.week, value)
    c.set_global_opts(visualmap_opts=opts.VisualMapOpts())
    return c


# 下面是对饼图的尝试
def pie_base():
    c = Pie()
    c.add("", [list(z) for z in zip(['宝马', '奔驰', '奥迪', '别克', '大众'], [random.randint(1, 20) for _ in range(5)])])
    return c


pie_base().render()


