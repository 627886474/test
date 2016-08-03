import time

def organization(self):
    driver = self.driver
    driver.find_element_by_link_text(u'员工设置').click()
    time.sleep(3)
    driver.find_element_by_link_text(u'组织架构').click()
    time.sleep(3)

def records(self):
    driver = self.driver
    driver.find_element_by_link_text(u'员工资料').click()
    time.sleep(3)

def manage(self):
    driver = self.driver
    driver.find_element_by_link_text(u'管理制度').click()
    time.sleep(3)

def scheduling(self):
    driver = self.driver
    driver.find_element_by_link_text(u'排班设置').click()
    time.sleep(3)

def attendance(self):
    driver = self.driver
    driver.find_element_by_link_text(u'考勤记录').click()
    time.sleep(3)