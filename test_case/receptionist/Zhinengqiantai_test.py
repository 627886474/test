# coding=utf-8
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

from test_case import login
from test_case.receptionist import Zhinengqiantai


class Reception(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url="http://www.maywant.com/zefun"
        self.driver.get(self.base_url)
        login.login(self)
        self.verificationErrors=[]
        self.accept_next_alert=True

    def test_card(self):
        u"""会员充值界面访问、员工轮牌界面访问、流水查询、开支记账"""
        Zhinengqiantai.yuyuezhongxin(self)
        time.sleep(3)
        Zhinengqiantai.yuangonglunpai(self)
        time.sleep(3)
        Zhinengqiantai.account(self)
        time.sleep(3)
        Zhinengqiantai.journalise(self)
        time.sleep(3)

    def test_openorder(self):
        u"""散客开项目测试、散客开商品测试"""
        Zhinengqiantai.openorder(self)
        time.sleep(3)
        Zhinengqiantai.openorder(self)
        time.sleep(3)

    def test_card2(self):
        u"""会员充值测试、会员赠送卡金"""
        Zhinengqiantai.recharge(self)
        time.sleep(3)
        Zhinengqiantai.gavecardmoney(self)
        time.sleep(3)

    # 对弹窗的异常处理
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    # 关闭警告以及对得到的文本框进行处理
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        # 对前面的verificationErrors方法获得的列表进行比较，输出报错信息

if __name__ == "__main__":
    suite=unittest.TestSuite()
    suite.addTest(Reception("test_card"))
    suite.addTest(Reception("test_openorder"))
    suite.addTest(Reception("test_card2"))

    unittest.TextTestRunner().run(suite)