# coding:utf-8
day = 9  # 取第二个值


def get_sunday():
    return 'Sun'


def get_Moday():
    return 'Moday'


def get_Tue():
    return 'Tue'

def get_dafault():
    return "Unkow"
switcher = {
    0: get_sunday,
    1: get_Moday,
    2: get_Tue

}

day_name = switcher.get(day, get_dafault)()  # get_dafault 如果day不存在时返回Unkow
print(day_name)
