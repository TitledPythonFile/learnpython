# encoding:utf-8

import pymysql.cursors

if __name__ == '__main__':
    #连接数据库connect
    conn = pymysql.connect(host='localhost', port=3306,
                           user='12306',
                           password='12306',
                           db='12306-train',
                           charset='utf8')
    try:
        with conn.cursor() as cursor:
            sql = "INSERT IGNORE INTO `example` VALUES (%s, %s, %s)"
            cursor.execute(sql, (u"G1001", u"武汉", u"深圳")) 

        conn.commit()

        with conn.cursor() as cursor:
            sql = "SELECT `code`, `start`, `end` FROM `example`"
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                print result[0], result[1], result[2]

    finally:
        conn.close()
