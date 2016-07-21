#encoding:utf-8

import requests
import json
import time

def fetch_provinces():
    url = 'https://kyfw.12306.cn/otn/userCommon/allProvince'

    try:
        s = requests.get(url,verify = False)
    except Exception, e:
        print 'fetch provinces.' + url
        raise e

    j = json.loads(s.content)
    return j['data']

def fetch_data(url, province, fd):
    try:
        s = requests.get(url, params = {"province":province, "city":"", "county":""}, verify = False)
    except Exception, e:
        print 'requests url fail.', url, province.encode('utf-8')
        return

    datas = json.loads(s.content)

    for data in datas["data"]["datas"]:
        out = u''
        out += data['province']
        out += u'' + data['city']
        out += u'' + data['county']
        out += u'' + data['agency_name']
        out += u'' + data['address']
        out += u'' + data['windows_quantity']
        start = data['start_time_am']
        end = data['stop_time_pm']

        out += u' ' + start[:2] + u':' + start[2:] + u' - ' + end[:2] + u':' + end[2:]
        s = out.encode("utf-8")
        fd.write(s)
        fd.write('\n')
        print s

if __name__ == '__main__':
    provs = fetch_provinces()

    url = 'https://kyfw.12306.cn/otn/queryAgencySellTicket/query'

    with open('11.final.txt','w') as fd:
        for prov in provs:
            fetch_data(url, prov['chineseName'], fd)
            time.sleep(5)