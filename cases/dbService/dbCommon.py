# -*- coding: utf-8 -*-

from apiAutomation import redisClient
from apiAutomation.utils import Encrypt
from apiAutomation.phoneNumbers import phoneNumbersInfo
import re
from apiAutomation.mysqlClient import executeSql

redis = redisClient
encrypt = Encrypt()

def redisSearch(key):
    res = redis.get(key)
    return res

def itcPhone(**kwargs):
    if 'itc' and 'phoneNumber' in kwargs:
        itcphone = kwargs['itc']+kwargs['phoneNumber']
        return itcphone


def regexSeekid(**val):
    try:
        link = val['link']
        reg = r'sid=(.*)&'
        resReg = re.findall(reg,link)
        return resReg
    except Exception as e:
        print(e)

def sqlSelId(**val):
    table = val['table']
    val.pop('table')
    mysqlRes = None
    for k in val:
        sql = "select * from im_db_dev.{} where {} = '{}' and state = 1 ".format(table, k, str(val.get(k)))
        if 't_user' == table:
            sql += "and appid = 2"
        try:
            mysqlRes = executeSql(sql)
            return mysqlRes[0]
        except:
            break
    return mysqlRes

def sqlparm(tab,col,vlu):
    sqlvar = {'table': tab, col: vlu}
    return sqlvar

def isFolw(uid,fuid):
    folwflg = False
    sql = 'select * from im_db_dev.follow where uid = {} and follow_uid = {} and state = 1'.format(uid, fuid)
    mysRes = executeSql(sql)
    if mysRes:
        folwflg = True
    return folwflg

def desPhone(phone):
    pho = phoneNumbersInfo(phone)
    return pho.get('number')

def folowCount(uid):
    fosql = "select count(1) as con from im_db_dev.follow where uid = '{}' and state = 1".format(uid)
    fasql = "select count(1) as con from im_db_dev.follow where follow_uid = '{}' and state = 1".format(uid)

    try:
        folco = executeSql(fosql)
        fanco = executeSql(fasql)

        return folco[0], fanco[0]
    except:
        print('error occured,let us try later')

if __name__ == '__main__':
    # val = {
    #     "table": "t_user",
    #     "link": "https://www-test.poppin.im/invitation?sid=ahvj6enswq46s7tvqq\u0026source=qrcode"
    # }
    # res = regexSeekid(**val)
    # print(res)


    (fol,fan) = folowCount('65077292')
    print(fol.get('con'),fan.get('con'))