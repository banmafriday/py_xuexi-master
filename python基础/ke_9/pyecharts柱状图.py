import pyecharts
from pyecharts.charts import Bar  # pyecharts柱状图
from pyecharts.charts import Pie  # 饼图
from pyecharts.charts import Line  # 折现图
from pyecharts import options as opts  # 设置参数

bar = Bar()   #创建一个柱状图对象
bar.add_xaxis(["衬衫","毛衣","裙子","风衣"])  #添加x轴数据
bar.add_yaxis("A商家销量",[120,167,353,929])   #添加y轴数据
bar.add_yaxis("B商家销量",[170,637,343,949])   #添加y轴数据
bar.add_yaxis("C商家销量",[190,647,333,199])   #添加y轴数据
bar.set_global_opts(title_opts=opts.TitleOpts(title="商品销售情况"))   #设置标题
bar.render("柱状图.html")
