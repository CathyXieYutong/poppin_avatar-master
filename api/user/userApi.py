from apiAutomation.httpHelper import get,post
from apiAutomation.httpClient import BaseClient


class HttpClientUserApi(BaseClient):

    @post('/v2/user/init-profile',is_json_req=True)
    def initProfile(self,**kwargs):
        """完善个人形象"""

    @get('/v2/user/profile',is_json_req = True)
    def userProfile(self,**kwargs):
        """个人信息"""

    @post('/v2/user/update-profile',is_json_req=True)
    def updateProfile(self,**kwargs):
        """用户信息更新"""

    @post('/v2/user/delete', is_json_req=True)
    def delAccount(self, **kwargs):
        """用户删除自己的账号"""

    @get('/v2/user/search', is_json_req=True)
    def userSearch(self, **kwargs):
        """搜索用户信息"""

    @get(' /v2/user/invite/info', is_json_req=True)
    def inviterInfo(self, **kwargs):
        """获取邀请人信息接口"""

    @get('/v2/user/invite/link', is_json_req=True)
    def inviteLink(self, **kwargs):
        """获取邀请链接接口"""

    @post('/v2/user/invite/link-check', is_json_req=True)
    def linkStatus(self, **kwargs):
        """检查邀请链接是否过期"""

    @post('/v2/user/invite/link-reset', is_json_req=True)
    def linkReset(self, **kwargs):
        """重置邀请链接"""

    @get('/v2/user/status/categories', is_json_req=True)
    def statusCtgry(self, **kwargs):
        """查询所有状态类"""

    @get('/v2/user/status', is_json_req=True)
    def userStatus(self, **kwargs):
        """查询用户的最新Status"""

    @post('/v2/user/status/pub', is_json_req=True)
    def pubStatus(self, **kwargs):
        """更新用户Status"""

    @post('/v2/user/block', is_json_req=True)
    def blockUser(self, **kwargs):
        """拉黑用户"""

    @post('/v2/user/unblock', is_json_req=True)
    def unblokUser(self, **kwargs):
        """解除拉黑用户"""

    @get('/v2/user/blocklist', is_json_req=True)
    def blockList(self, **kwargs):
        """我的黑名单列表"""

    @post('/v2/user/follow', is_json_req=True)
    def followUser(self, **kwargs):
        """关注用户"""

    @post('/v2/user/unfollow', is_json_req=True)
    def userUnfollow(self, **kwargs):
        """用户取关"""
