# -*- coding: utf-8 -*-
from apiAutomation.httpHelper import get,post
from apiAutomation.httpClient import BaseClient


class HttpClientAuthApi(BaseClient):

    @get("/v2/app/query-itcs",is_json_req=True)
    def queryItcs(self,**kwargs):
        """获取国际区号"""

    @post("/v2/auth/send-sms",is_json_req=True)
    def sendSms(self,**kwargs):
        """发送验证码"""

    @post("/v2/auth/login",is_json_req=True)
    def login(self,**kwargs):
        """登陆"""

    @post("/v2/user/init-profile", is_json_req=True)
    def initProfile(self, **kwargs):
        """个人信息初始化"""

    @post("/v2/auth/logout", is_json_req=True)
    def logout(self, **kwargs):
        """退出登陆"""

    @get("/v2/user/search")
    def search(self,**kwargs):
        """搜索"""
