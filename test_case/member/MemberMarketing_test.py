# coding=utf-8
import time,unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

from test_case import login
from test_case.member import MemberMarketing

class Member(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url="http://www.maywant.com/zefun"
        self.driver.get(self.base_url)
        login.login(self)
        self.verificationErrors=[]
        self.accept_next_alert=True

    def test_MemberMarketing(self):
        u"""会员营销界面测试"""
        MemberMarketing.memberdata(self)
        time.sleep(2)
        MemberMarketing.membermarketing(self)
        time.sleep(2)
        MemberMarketing.memberpacket(self)
        time.sleep(2)

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text=alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__=="__main__":
    suite=unittest.TestSuite()
    suite.addTest(Member("test_MemberMarketing"))

    unittest.TextTestRunner().run(suite)