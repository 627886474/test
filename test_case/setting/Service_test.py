# coding=utf-8
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from test_case import login
from test_case.setting import Service


class Project_Setting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url="http://www.maywant.com/zefun"
        self.driver.get(self.base_url)
        login.login(self)
        self.verificationErrors = []
        # 脚本运行时，错误的信息打印到这个列表中
        self.accept_next_alert = True
        # 是否接受下一个警告

    def test_project(self):
        u"""项目设置界面"""
        Service.project(self)
        time.sleep(3)
        Service.course(self)
        time.sleep(3)
        Service.goods(self)
        time.sleep(3)
        Service.stock(self)
        time.sleep(3)
        Service.ruku(self)
        time.sleep(3)
        Service.chuku(self)
        time.sleep(3)
        Service.brand(self)
        time.sleep(3)
        Service.suppliers(self)
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
    suite.addTest(Project_Setting("test_project"))

    unittest.TextTestRunner().run(suite)