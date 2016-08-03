import time

def memberdata(self):
    driver = self.driver
    driver.find_element_by_link_text(u"会员营销").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[1]").click()
    time.sleep(2)
    driver.find_element_by_id("changeInfoBtn").click()
    time.sleep(2)

def memberpacket(self):
    driver = self.driver
    # 会员分组
    driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[2]").click()
    time.sleep(2)
    # 会员卡设置
    driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[3]").click()
    time.sleep(2)
    # 微门店设置
    driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[4]").click()
    time.sleep(2)
    # 优惠券管理
    driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[6]").click()
    time.sleep(2)
    # 自动回复
    driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[7]").click()
    time.sleep(2)
    # 连锁店会员
    driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[8]").click()
    time.sleep(2)

def membermarketing(self):
    driver=self.driver
    # 营销方案库设置
    driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[5]").click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tabs"]/ul/li[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tabs"]/ul/li[3]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tabs"]/ul/li[4]/a').click()
    time.sleep(2)
