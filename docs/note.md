#### 关于pyecharts的一些学习心得

##### 条形图

```python
# 下面是对条形图进行的测试
bar = Bar()
bar.add_xaxis(["数统","计科","物院","文院"])
bar.add_yaxis("学院",[5,8,2,7])

# bar.render_notebook() 这是在notebook上面进行直接展示使用的
# 下面一种是可以直接生产html文件的方法，值得注意的是其中也是可以添加路径参数的
bar.render()
```

##### 散点图

```python
scatter = Scatter()
scatter.add_xaxis(Faker.choose())
scatter.add_yaxis("商家", Faker.values())

# 这里是一些全局变量的设置，主要是标题和时候画出分隔线，也许其中会有很多不一样的尝试机会
scatter.set_global_opts(
    title_opts=opts.TitleOpts(title="显示分隔线"),
    xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
    yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
)

scatter.render()
```

##### 层叠多图

```python
def overlap_line_scatter():
    x = Faker.choose()
    bar = Bar().add_xaxis(x).add_yaxis("商家A", Faker.values()).add_yaxis("商家B", Faker.values())
    line = Line().add_xaxis(x).add_yaxis("商家A", Faker.values()).add_yaxis("商家B", Faker.values())
    bar.overlap(line)
    return bar

overlap_line_scatter().render()
```

##### 折线图

```python
def line_xaxis_type():
    c = Line()
    c.add_xaxis(Faker.values())
    c.add_yaxis("商家A", Faker.values())
    c.add_yaxis("商家B", Faker.values())
    c.set_global_opts(title_opts=opts.TitleOpts(title="折线图"), xaxis_opts=opts.AxisOpts(type_="value"))
    return c


line_xaxis_type().render()
```

##### 热力图

```python
def heatmap_base():
    value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    c = HeatMap()
    c.add_xaxis(Faker.clock)
    c.add_yaxis("serise0", Faker.week, value)
    c.set_global_opts(visualmap_opts=opts.VisualMapOpts())
    return c


heatmap_base().render()
```

##### 饼图

```python
# 下面开始折线图
def line_xaxis_type():
    c = Line()
    c.add_xaxis(Faker.values())
    c.add_yaxis("商家A", Faker.values())
    c.add_yaxis("商家B", Faker.values())
    c.set_global_opts(title_opts=opts.TitleOpts(title="折线图"), xaxis_opts=opts.AxisOpts(type_="value"))
    return c
```

