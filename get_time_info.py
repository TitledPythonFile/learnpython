#encoding:utf-8

import time
import datetime

import json
import urllib
import requests

def fetch_schedule(train_code, station_name, depart):
    url = 'http://dynamic.12306.cn/map_zwdcx/cx.jsp'

    params = {
        'cz' : station_name,
        'cc' : train_code,
        'cxlx' : '1' if depart else '0',
        'rq' : datetime.datetime.now().strftime('%Y-%m-%d'),
        'czEn' : urllib.quote(station_name.encode('utf-8')).replace('%','-'),
        'tp' : int(time.time() * 1000)
    }

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }

    try:
        s = requests.get(url, params = params , headers = headers)
    except Exception,e:
        print 'request fail' + url
        raise e

    print s.content.strip().decode('gbk').encode('utf-8')

if __name__ == '__main__':
    fetch_schedule('C6146', u'成都' ,False)