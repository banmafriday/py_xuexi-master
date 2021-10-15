# coding:utf-8
import requests
import re
import json

s = requests.session()


def login():
    '''登录'''
    url = "https://yapi.lessoald.cn/api/user/login"

    d = json.dumps({
        "email": "294350757@qq.com",
        "password": "13975943593",
    })
    headers = {

        'Host': 'yapi.lessoald.cn',
        'Connection': 'keep-alive',
        'Content-Length': '53',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://yapi.lessoald.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://yapi.lessoald.cn/login',

    }
    response = s.post(url, headers=headers, data=d)
    result = response.cookies
    print(result)

login()

def Add_api():
    # https: // yapi.lessoald.cn / group / 238
    url = "https://yapi.lessoald.cn/group/238"

    headers = {

        'Host': 'yapi.lessoald.cn',
        'Connection': 'keep-alive',
        'Content-Length': '53',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://yapi.lessoald.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://yapi.lessoald.cn/login',

    }

    response = s.get(url, headers=headers)
