import time
from selenium import webdriver
# 会员充值测试
def project(self):
    driver = self.driver
    driver.find_element_by_link_text(u"服务设置").click()
    time.sleep(3)
    driver.find_element_by_link_text(u"项目设置").click()
    time.sleep(3)

def course(self):
    driver = self.driver
    driver.find_element_by_link_text(u"疗程设置").click()
    time.sleep(3)

def goods(self):
    driver = self.driver
    driver.find_element_by_link_text(u"商品设置").click()
    time.sleep(3)

def stock(self):
    driver = self.driver
    driver.find_element_by_link_text(u"商品库存").click()
    time.sleep(3)

def ruku(self):
    driver = self.driver
    driver.find_element_by_link_text(u"入库管理").click()
    time.sleep(3)

def chuku(self):
    driver = self.driver
    driver.find_element_by_link_text(u"出库管理").click()
    time.sleep(3)

def brand(self):
    driver = self.driver
    driver.find_element_by_link_text(u"商品品牌").click()
    time.sleep(3)

def suppliers(self):
    driver = self.driver
    driver.find_element_by_link_text(u"供应商管理").click()
    time.sleep(3)