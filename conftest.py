import time
import pytest
from feishuTools.feishuRobot import FeishuRobot


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    msgTitle = str(time.strftime('%Y-%m-%d', time.localtime())) + "\tApiTest Result"
    msgInfo = []
    msgHead = {"tag":"div","fields":[]}
    msgPassed = {"tag":"div","fields":[]}
    msgFailed = {"tag":"div","fields":[]}
    msgAction = {}
    msgLine = {"tag":"hr"}

    total = terminalreporter._numcollected
    passed= len([i for i in terminalreporter.stats.get('passed', []) if i.when == 'call'])
    failed=len([i for i in terminalreporter.stats.get('failed', []) if i.when == 'call'])
    # error=len([i for i in terminalreporter.stats.get('error', []) if i.when == 'call'])
    # skipped=len([i for i in terminalreporter.stats.get('skipped', []) if i.when == 'call'])
    successful = round(len(terminalreporter.stats.get('passed', []))/terminalreporter._numcollected*100,2)

    #处理卡片信息上展示的统计部分
    msgHead["fields"].append(
        {"is_short":True,
         "text":{
             "tag":"lark_md",
             "content":
                 "**TOTAL：**{}".format(str(total))
         }})
    msgHead["fields"].append(
        {"is_short": True,
         "text": {
             "tag": "lark_md",
             "content":
                 "<font color='green'>**PASSED：**<font> {}".format(str(passed))
         }})
    msgHead["fields"].append(
        {"is_short": True,
         "text": {
             "tag": "lark_md",
             "content":
                 "**SUCCESSFUL：**<font color='{}'>{}<font>".format(
                 "red" if int(successful) < 100 else "green",
                 str(successful) + "%")}})
    msgInfo.append(msgHead)
    msgInfo.append(msgLine)

    # 处理卡片信息上通过的测试用例
    if passed >= 1:
        for case in terminalreporter.stats["passed"]:
            msgPassed["fields"].append(
                {"is_short": False,
                 "text": {
                     "tag": "lark_md",
                     "content":
                         "<font color='green'>**【PASSED】**<font>\t{}".format(
                             case.nodeid.split(".py")[1].lstrip("::"))}})
        msgInfo.append(msgPassed)
        msgInfo.append(msgLine)
    else:pass

    #处理卡片信息上失败的测试用例
    if failed >= 1:
        for case in terminalreporter.stats["failed"]:
            msgFailed["fields"].append(
                {"is_short": False,
                 "text": {
                     "tag": "lark_md",
                     "content":
                         "<font color='red'>**【PASSED】**<font>\t{}".format(
                             case.nodeid.split(".py")[1].lstrip("::"))}})
        msgInfo.append(msgFailed)
    FeishuRobot().interactiveMsg(title=msgTitle, elements=msgInfo)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    out = yield  # 钩子函数的调用结果
    res = out.get_result()  # 获取用例执行结果
    if res.when == "call":
        if res.outcome == "passed":
            pass
        else:
            print("用例失败时的详细日志：{}".format(res.longrepr))

