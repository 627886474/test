# coding=utf-8
import time
from selenium import webdriver

def summary(self):
    # 门店汇总
    driver=self.driver
    driver.find_element_by_link_text(u"营业报表").click()
    time.sleep(3)
    driver.find_element_by_link_text(u"门店汇总").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[3]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[4]').click()
    time.sleep(3)

def membership(self):
    driver = self.driver
    driver.find_element_by_link_text(u"卡项销售").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[3]').click()
    time.sleep(3)

def laborperformance(self):
    driver = self.driver
    driver.find_element_by_link_text(u"劳动业绩").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[3]').click()
    time.sleep(3)

def course_sales(self):
    driver = self.driver
    driver.find_element_by_link_text(u"疗程销售").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[3]').click()
    time.sleep(3)

def goods_sales(self):
    driver = self.driver
    driver.find_element_by_link_text(u"商品销售").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[3]').click()
    time.sleep(3)

def member_performance(self):
    driver = self.driver
    driver.find_element_by_link_text(u"员工业绩").click()
    time.sleep(5)
    driver.find_element_by_id('month').click()
    time.sleep(3)
    driver.find_element_by_id('2016-06').click()
    time.sleep(3)
    driver.find_element_by_class_name('chzn-single').click()
    time.sleep(3)
    driver.find_element_by_id('position_chzn_o_1').click()
    time.sleep(3)

def payroll(self):
    driver = self.driver
    driver.find_element_by_link_text(u"工资单").click()
    time.sleep(3)
    # driver.find_element_by_id('month').click()
    # time.sleep(3)
    # driver.find_element_by_id('2016-06').click()
    # time.sleep(3)

def reconciliation(self):
    driver = self.driver
    driver.find_element_by_link_text(u"跨店对账").click()
    time.sleep(3)
    # driver.find_element_by_id('month').click()
    # time.sleep(3)
    # driver.find_element_by_id('2016-06').click()
    # time.sleep(3)



