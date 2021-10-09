# josn

import json

# 保存一个学员信息
stu1 = '{"name":"张三","age":18,"hobby":"play"}'

# 保存多个学员信息
stu2 = '[{"name":"张三","age":18,"hobby":"play"},' \
       '{"name":"李四","age":18,"hobby":"play"},{"name":"王五","age":18,"hobby":"play"}]'

# 1.json转python(转成字典或者列表)
jsonData = '{"name":"张三","age":18,"hobby":"play"}'
pythonData = json.loads(jsonData)
# print(pythonData)
# print(pythonData['name'])

# 2.python转json(转成字典或者列表)

pythonData2 = {"cname": "1001", "cpwd": "123", "cbalance": 1000,"name":"张三"}
pythonData3 = json.dumps(pythonData2,ensure_ascii=False) # ensure_ascii=False 禁止ascii转换

print(pythonData3)
