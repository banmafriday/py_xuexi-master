import pyecharts
from pyecharts.charts import Bar  # pyecharts柱状图
from pyecharts.charts import Pie  # 饼图
from pyecharts.charts import Line  # 折现图
from pyecharts import options as opts  # 设置参数

pie = Pie()  # 创建饼状图对象
cate = ["苹果", "华为", "小米", "oppo", "vivo", "魅族"]
data = [12, 4234, 53, 5435, 435, 56]
dataList=[] #数据处理
for i in range(0,len(data)):
    d = [cate[i],data[i]]
    dataList.append(d)
pie.add("单位:万台",dataList)
pie.set_global_opts(title_opts=opts.TitleOpts(title="手机销量情况"))   #设置标题
pie.render("手机销量饼图.html")
