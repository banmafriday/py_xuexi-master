# coding:utf-8
import requests
import re


def login():
    '''登录'''
    url = "https://yapi.lessoald.cn/api/user/login"
    qu = {"email": "294350757@qq.com", "password": "13975943593"}

    headersw = {
        'Host': 'yapi.lessoald.cn',
        'content-type': "mapplication/json;charset=UTF-8",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        'Accept': "application/json, text/plain, */*",
        'host': 'yapi.lessoald.cn',
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "320",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
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
    response = requests.post(url, headers=headers, params=qu)
    print(response.text)


login()
