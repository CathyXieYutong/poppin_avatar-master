# -*- coding: utf-8 -*-
import json

import pytest

from api.auth.authApi import HttpClientAuthApi
# from api.auth.authApi import HttpClientAuthApi
from apiAutomation.baseTestCase import BaseTestCase
from cases.authCases.testData import testAuthData
from apiAutomation.mysqlClient import executeSql
from apiAutomation import redisClient
# from cases.dbService import dbContactApi,dbProfileApi
# from cases.contactCases.testData import testContactApiData
from cases.dbService import dbCommon

class TestAuthtApi(BaseTestCase):
    @classmethod
    def setup_class(cls):
        cls.authApiService = HttpClientAuthApi()


    # @pytest.mark.parametrize('smsData',smsData,ids=[i.get('name') for i in smsData])
    def testSendSms(self):
        # 获取参数
        smsDatas = testAuthData.sendSmsData
        # 循环获取每一条用例的参数
        for smsData in smsDatas:
            itcPhone = dbCommon.itcPhone(**smsData)
            if itcPhone is not None:
                val = {"value": "1001", "name": 'auth:sms_risk_count:hour:'+itcPhone}
                if "phoneNumber" in smsData:
                    redisClient.set(**val)
            res = self.authApiService.sendSms(**smsData)
            self.assert_equal(res.error_code, smsData['errcode'], 'failed')

    def testLoginOrRegister(self):
        # auth:sms_key:8613061819332
        loginDatas = testAuthData.loginOrRegisterData
        for loginData in loginDatas:
            if "authType" in loginData and "phoneNumber" in loginData:
                if loginData['authType'] == 3 and loginData['phoneNumber'] != "":
                    self.authApiService.sendSms(**loginData)
                    itcPhone = dbCommon.itcPhone(**loginData)
                    redRes = dbCommon.redisSearch("auth:sms_key:" + itcPhone)
                    rsprds = json.loads(redRes)
                    print('---p---p---: ', rsprds['SmsCode'])
                    loginData['verificationCode'] = rsprds['SmsCode']
                    res = self.authApiService.login(**loginData)

                elif loginData['phoneNumber'] == '':
                    res = self.authApiService.login(**loginData)

                elif loginData['authType'] == '':
                    res = self.authApiService.login(**loginData)

            else:
                res = self.authApiService.login(**loginData)


    def testSearch(self):
        res  = self.authApiService.search(phone=8613300000001,
                                          key="testsearch")
    #
    #     self.assert_equal(res.error_code,"200","结果错误")

    # def testLogout(self):
    #     res = self.authApiService.logout(phone = 8613300000025)

    def testQueryItcs(self):
        res = self.authApiService.queryItcs()
        flag = 0
        try:
            itclist = res['data']['itcs']
            itc = testAuthData.queryItcs
            for itcs in itclist:
                if itc['itc'] == itcs['itc']:
                    flag = 1
        except Exception as e:
            print(e)
        finally:
            self.assert_equal(1,flag,"获取区号列表成功")

    #
    # def testLogout_2(self):
    #     res = self.authApiService.logout(phone = 8613300000027)
    #
    # def testLogout_3(self):
    #     res = self.authApiService.logout(phone = 8613300000028)
    #
    # def testLogout_4(self):
    #     res = self.authApiService.logout(phone = 8613300000029)
    #
    # def testLogout_5(self):
    #     res = self.authApiService.logout(phone = 8613300000030)
    #
    # def testLogout_6(self):
    #     res = self.authApiService.logout(phone = 8613300000031)
    #
    # def testLogout_7(self):
    #     res = self.authApiService.logout(phone = 8613300000032)
    #
    # def testLogout_8(self):
    #     res = self.authApiService.logout(phone = 8613300000033)
    #
    # def testLogout_9(self):
    #     res = self.authApiService.logout(phone = 8613300000034)
