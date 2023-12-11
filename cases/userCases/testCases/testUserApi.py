# -*- coding: utf-8 -*-
import base64
import json
import re

import pytest
from api.user.userApi import HttpClientUserApi
from apiAutomation.baseTestCase import BaseTestCase
from cases.userCases.testData import testUserData
from cases.dbService import dbCommon
from apiAutomation.utils import Encrypt


class TestUserApi(BaseTestCase):

    @classmethod
    def setup_class(cls):
        cls.userApiService = HttpClientUserApi()

    def testInitProfile(self):
        pass

    def testUserProfile(self):
        dts = testUserData.userProfileData
        for uid in dts:
            resp = self.userApiService.userProfile(**uid)
            respPid = resp['data']['poppinID']
            sqlVar = dbCommon.sqlparm('t_user', 'username', respPid)
            dbrs = dbCommon.sqlSelId(**sqlVar)
            folco, fanco = dbCommon.folowCount(dbrs['id'])
            dbrsDcode = Encrypt().aes_decrypt(dbrs['phone_number']).encode('utf-8')
            dbrsNumber = base64.b64encode(dbrsDcode).decode('utf-8')
            if uid.get('uid'):
                phon = Encrypt().aes_encrypt(str(dbCommon.desPhone(uid['phone'])))
                logUidvar = dbCommon.sqlparm('t_user', 'phone_number', phon)
                logUid = dbCommon.sqlSelId(**logUidvar)
                isfolow = dbCommon.isFolw(logUid['id'], resp['data']['uid'])
                isFan = dbCommon.isFolw(resp['data']['uid'],logUid['id'])
                self.assert_equal(resp['data']['isFollow'], isfolow, 'failed')
                self.assert_equal(resp['data']['isFan'], isFan, 'failed')
            self.assert_equal(respPid, respPid, 'failed')
            self.assert_equal(resp['data']['uid'], dbrs['id'], 'failed')
            self.assert_equal(resp['data']['state'], dbrs['state'], 'failed')
            self.assert_equal(resp['data']['avatar'], dbrs['avatar'], 'failed')
            self.assert_equal(resp['data']['phoneNumber'], dbrsNumber, 'failed')
            self.assert_equal(resp['data']['followCount'],folco.get('con'),'failed')
            self.assert_equal(resp['data']['fanCount'], fanco.get('con'), 'failed')




    def testUpdateProfile(self):
        pass

    def testDelAccount(self):
        pass

    def testUserSearch(self):
        # @TODO phone check
        serchDatas = testUserData.userSerchData
        flag = True
        for serchData in serchDatas:
            res = self.userApiService.userSearch(**serchData)
            for resd in res['data']['users']:

                if not re.search(serchData['key'], resd['poppinID'], re.IGNORECASE) \
                        and not re.search(serchData['key'], resd['name'], re.IGNORECASE):
                    flag = False
                    break
            self.assert_equal(True, flag, 'failed')
            # self.assert_response(res)


    def testInviterInfo(self):
        pass

    def testInviteLink(self):
        linkDatas = testUserData.inviteLnkData
        usr = {}
        for linkData in linkDatas:
            res = self.userApiService.inviteLink(**linkData)
            usrname = res['data']['username']
            sqlvar = dbCommon.sqlparm('t_user', 'username',usrname)
            dbrs = dbCommon.sqlSelId(**sqlvar)
            uid = dbrs['id']
            rsd = json.loads(dbCommon.redisSearch('u:invite:'+str(uid)))
            seek = dbCommon.regexSeekid(**res['data'])
            seekrds = rsd['seek_id']
            self.assert_equal(seek[0],seekrds,'failed')


    def testLinkStatus(self):
        linkChkDatas = testUserData.linkChkData
        for linkChkData in linkChkDatas:
            linkres = self.userApiService.inviteLink(**linkChkData)
            usrname = linkres['data']['username']
            sqlvar = dbCommon.sqlparm('t_user', 'username', usrname)
            dbrs = dbCommon.sqlSelId(**sqlvar)
            uid = dbrs['id']
            rsd = json.loads(dbCommon.redisSearch('u:invite:' + str(uid)))
            seek = dbCommon.regexSeekid(**linkres['data'])
            seekrds = rsd['seek_id']
            self.assert_equal(seek[0], seekrds, 'failed')
            val = {'seekId': seek[0]}
            resStatus = self.userApiService.linkStatus(**val)
            '''chk link is valid'''
            self.assert_equal(False, resStatus['data']['expired'], 'failed')
            linkRestSts = self.userApiService.linkReset()
            rstSeekId = dbCommon.regexSeekid(**linkRestSts['data'])
            '''chk link is reseted'''
            self.assert_not_equal(seek[0],rstSeekId[0], 'failed')
            rsSts = self.userApiService.linkStatus(**val)
            '''chk link is invalid'''
            self.assert_equal(True, rsSts['data']['expired'], 'failed')


    def testLinkReset(self):
        pass

    def testStatusCtgry(self):
        pass

    def testUserStatus(self):
        usrStatusDatas = testUserData.userStatusData
        for usrStatusData in usrStatusDatas:
            res = self.userApiService.userStatus(**usrStatusData)


    def testPubStatus(self):
        pass

    def testBlockUser(self):
        userBlkData = testUserData.blockUserData
        for usrBlkData in userBlkData:
            self.userApiService.blockUser(**usrBlkData)



    def testUnblokUser(self):
        pass

    def testBlockList(self):
        pass

    def testFollowUser(self):
        usrFolowDatas = testUserData.userFollowData
        for usrFolowData in usrFolowDatas:
            self.userApiService.followUser(**usrFolowData)
        pass

    def testUserUnfollow(self):
        pass

