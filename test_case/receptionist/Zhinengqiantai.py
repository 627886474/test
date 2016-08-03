# coding=utf-8
import time
from selenium import webdriver
# 会员充值测试
def yuyuezhongxin(self):
    # u"""预约中心"""
    driver = self.driver
    driver.find_element_by_link_text(u"预约中心").click()
    if driver.find_element_by_id("alertToast"):
        driver.get_screenshot_as_file("D:\\py\\test\\error_page\\预约网络繁忙.png")

def account(self):
    # u"""开支记账"""
    driver = self.driver
    driver.find_element_by_link_text(u"开支记账").click()
    time.sleep(3)
    driver.find_element_by_name("flowAmount").click()
    time.sleep(1)
    driver.find_element_by_name("flowAmount").send_keys("100")
    time.sleep(1)

    driver.find_element_by_link_text(u"选择记账类别").click()
    time.sleep(2)
    lis = driver.find_elements_by_xpath('//div/ul')
    for li in lis:
        if '固定支出' in li.text:
            li.click()
            break
    time.sleep(2)

    driver.find_element_by_link_text(u"选择记账项目").click()
    time.sleep(2)
    lis = driver.find_elements_by_xpath('//div/ul')
    for li in lis:
        if '宿舍租金' in li.text:
            li.click()
            break
    time.sleep(2)

    driver.find_element_by_link_text(u"选择收支来源").click()
    time.sleep(2)
    lis = driver.find_elements_by_xpath('//div/ul')
    for li in lis:
        if u"备用金" in li.text:
            li.click()
            break
    time.sleep(2)

    driver.find_element_by_link_text(u"选择经手人").click()
    time.sleep(2)
    lis = driver.find_elements_by_xpath('//div/ul')
    for li in lis:
        if u"1101 杨洋" in li.text:
            li.click()
            break
    time.sleep(2)
    driver.find_element_by_name("businessDesc").click()
    time.sleep(1)
    driver.find_element_by_name("businessDesc").send_keys(u"自动化测试")
    time.sleep(2)
    driver.find_element_by_id("save").click()
    time.sleep(2)

def journalise(self):
    driver = self.driver
    driver.find_element_by_link_text(u"流水查询").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="yesterday"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="totday"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//tr/td[1]/button[5]').click()
    time.sleep(3)

def yuangonglunpai(self):
    # 员工轮牌界面
    driver = self.driver
    driver.find_element_by_link_text(u"员工轮牌").click()
    time.sleep(3)

def recharge(self):
    # u"""会员充值测试"""
    driver = self.driver
    driver.find_element_by_link_text(u"开卡充值").click()
    time.sleep(5)
    driver.find_element_by_xpath("(//input[@id='searchBox'])[2]").click()
    driver.find_element_by_xpath("(//input[@id='searchBox'])[2]").clear()
    driver.find_element_by_xpath("(//input[@id='searchBox'])[2]").send_keys("13875780000")
    time.sleep(3)
    driver.find_element_by_xpath("(//button[@onclick='newSeachMember(this)'])").click()
    time.sleep(3)
    driver.find_element_by_name("czCashAmount").clear()
    driver.find_element_by_name("czCashAmount").send_keys("500")
    time.sleep(3)
    driver.find_element_by_link_text(u"选择部门").click()
    time.sleep(3)
    lis = driver.find_elements_by_xpath('//div/ul')
    for li in lis:
        if u"美容部" in li.text:
            li.click()
            break
    time.sleep(2)
    driver.find_element_by_xpath('//button[@onclick="czConfirm(1,this,2)"]').click()
    time.sleep(3)

def openorder(self):
    # u"""散客开项目测试"""
    driver = self.driver
    driver.find_element_by_name("kaidan").click()
    time.sleep(3)
    driver.find_element_by_xpath("//div[1]/div[3]/div[2]/div[1]/div[2]/ul/li[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[1]/div[3]/div[2]/div[3]/ul/li[2]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//div[@onclick='save(2)']").click()
    time.sleep(5)
    driver.find_element_by_link_text(u"立即买单").click()
    time.sleep(5)
    driver.find_element_by_xpath("//td[7]/div[3]").click()
    time.sleep(5)
    driver.find_element_by_link_text(u"收银").click()
    time.sleep(5)
    # try:
    #     driver.find_element_by_link_text("fuck").click()
    # except:
    #     driver.get_screenshot_as_file("D:\\py\\test\\error_page\\fuck.png")
    # driver.find_element_by_link_text("结账").click()

def openorder(self):
    # u"""散客开商品测试"""
    driver = self.driver
    driver.find_element_by_link_text(u"手工开单").click()
    time.sleep(3)
    driver.find_element_by_xpath("//div/div[1]/div[3]/div[2]/div[1]/div[1]/ul/li[3]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//div[8]/ul/li[2]").click()
    time.sleep(3)
    driver.find_element_by_xpath("//div[@onclick='save(2)']").click()
    time.sleep(5)
    driver.find_element_by_link_text(u"立即买单").click()
    time.sleep(5)
    driver.find_element_by_xpath("//td[7]/div[3]").click()
    time.sleep(5)
    driver.find_element_by_link_text(u"收银").click()
    time.sleep(5)

def gavecardmoney(self):
    # u"""会员赠送卡金测试"""
    driver = self.driver
    driver.find_element_by_link_text(u"开卡充值").click()
    time.sleep(5)
    driver.find_element_by_xpath("//li[5]/span").click()
    time.sleep(5)
    driver.find_element_by_xpath('(//input[@id="searchBox"])[6]').click()
    time.sleep(3)
    driver.find_element_by_xpath('(//input[@id="searchBox"])[6]').clear()
    driver.find_element_by_xpath('(//input[@id="searchBox"])[6]').send_keys("13875780000")
    time.sleep(3)
    driver.find_element_by_xpath("(//button[@onclick='newSeachMember(this)'])[5]").click()
    time.sleep(3)
    driver.find_element_by_name("zsIntegralAmount").send_keys("100")
    driver.find_element_by_name("zsGiftmoneyAmount").send_keys("100")
    time.sleep(2)
    driver.find_element_by_name("zsReason").send_keys("测试")
    time.sleep(2)
    driver.find_element_by_name("zsReason").click()
    driver.find_element_by_xpath('//button[@onclick="presentGift()"]').click()
    time.sleep(5)