from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("http://www.maywant.com/zefun/")
driver.maximize_window()
time.sleep(1)
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys("123456")
time.sleep(1)
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_class_name("loginButton").click()
time.sleep(5)
driver.execute_script('dialog("网络繁忙，请稍后再试")')
if driver.execute_script('dialog("网络繁忙，请稍后再试")'):
    driver.get_screenshot_as_file("D:\\预约网络繁忙.png")

time.sleep(5)


# driver.find_element_by_link_text(u"服务设置").click()
# time.sleep(3)
# driver.find_element_by_link_text(u"项目设置").click()
# time.sleep(3)
# driver.find_element_by_link_text(u"疗程设置").click()
# time.sleep(3)
# driver.find_element_by_link_text(u"商品设置").click()
# time.sleep(3)
# driver.find_element_by_link_text(u"商品库存").click()
# time.sleep(3)
# driver.find_element_by_link_text(u"入库管理").click()
# time.sleep(3)
# driver.find_element_by_link_text(u"出库管理").click()
# time.sleep(3)
# driver.find_element_by_link_text(u"商品品牌").click()
# time.sleep(3)
# driver.find_element_by_link_text(u"供应商管理").click()
# time.sleep(3)


#
# driver.find_element_by_link_text(u"跨店对账").click()
# time.sleep(3)
# driver.find_element_by_xpath('//div[1]/div/div/button').click()
# time.sleep(5)
# lis  = driver.find_element_by_class_name('dropdown-menu')
# for li in lis:
#     if '2016-06' in li.text:
#         li.click()
#         break
# time.sleep(2)





# driver.execute_script('dialog("会话失效，请重新登录")')



# driver.get_screenshot_as_file("D:\\py\\test\\error_page\\预约网络繁忙1.png")










# # 会员营销
# driver.find_element_by_link_text(u"会员营销").click()
# time.sleep(2)
# driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[1]").click()
# time.sleep(2)
# driver.find_element_by_id("changeInfoBtn").click()
# time.sleep(2)
# # 会员分组
# driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[2]").click()
# time.sleep(2)
# # 会员卡设置
# driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[3]").click()
# time.sleep(2)
# # 微门店设置
# driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[4]").click()
# time.sleep(2)
# # 营销方案库设置
# driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[5]").click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="tabs"]/ul/li[2]/a').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="tabs"]/ul/li[3]/a').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="tabs"]/ul/li[4]/a').click()
# time.sleep(2)
# # 优惠券管理
# driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[6]").click()
# time.sleep(2)
# # 自动回复
# driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[7]").click()
# time.sleep(2)
# # 连锁店会员
# driver.find_element_by_xpath("//div[4]/div[2]/ul[2]/li[8]").click()
# time.sleep(2)


# 流水查询
#
# driver.find_element_by_link_text(u"流水查询").click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="yesterday"]').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="totday"]').click()
# time.sleep(3)
# driver.find_element_by_xpath('//tr/td[1]/button[5]').click()
# time.sleep(3)



# u"""会员赠送卡金测试"""
#
# # driver.find_element_by_link_text(u"预约中心").click()
# # time.sleep(3)
#
# driver.find_element_by_link_text(u"开支记账").click()
# time.sleep(3)
# driver.find_element_by_name("flowAmount").click()
# time.sleep(1)
# driver.find_element_by_name("flowAmount").send_keys("100")
# time.sleep(1)
#
# driver.find_element_by_link_text(u"选择记账类别").click()
# time.sleep(2)
# lis = driver.find_elements_by_xpath('//div/ul')
# for li in lis:
#     if '固定支出' in li.text:
#         li.click()
#         break
# time.sleep(2)
#
# driver.find_element_by_link_text(u"选择记账项目").click()
# time.sleep(2)
# lis = driver.find_elements_by_xpath('//div/ul')
# for li in lis:
#     if '宿舍租金' in li.text:
#         li.click()
#         break
# time.sleep(2)
#
# driver.find_element_by_link_text(u"选择收支来源").click()
# time.sleep(2)
# lis = driver.find_elements_by_xpath('//div/ul')
# for li in lis:
#     if u"备用金" in li.text:
#         li.click()
#         break
# time.sleep(2)
#
# driver.find_element_by_link_text(u"选择经手人").click()
# time.sleep(2)
# lis = driver.find_elements_by_xpath('//div/ul')
# for li in lis:
#     if u"1101 杨洋" in li.text:
#         li.click()
#         break
# time.sleep(2)
# driver.find_element_by_name("businessDesc").click()
# time.sleep(1)
# driver.find_element_by_name("businessDesc").send_keys(u"自动化测试")
# time.sleep(2)
# driver.find_element_by_id("save").click()
# time.sleep(2)



# driver.find_element_by_xpath('(//input[@id="searchBox"])[6]').clear()
# driver.find_element_by_xpath('(//input[@id="searchBox"])[6]').send_keys("18684940192")
# driver.find_element_by_xpath('(//button[@onclick="newSeachMember(this)"])[6]').click()
# time.sleep(2)
# driver.find_element_by_name("zsIntegralAmount").send_keys("100")
# driver.find_element_by_name("zsGiftmoneyAmount").send_keys("100")
# time.sleep(2)
# driver.find_element_by_name("zsReason").send_keys("测试")
# time.sleep(2)
# driver.find_element_by_name("zsReason").click()


# 充值
# driver.find_element_by_link_text(u"开卡充值").click()
# time.sleep(5)
# driver.find_element_by_xpath("(//input[@id='searchBox'])[2]").click()
# driver.find_element_by_xpath("(//input[@id='searchBox'])[2]").clear()
# driver.find_element_by_xpath("(//input[@id='searchBox'])[2]").send_keys("18684940192")
# time.sleep(5)
# driver.find_element_by_xpath("(//button[@onclick='newSeachMember(this)'])[2]").click()
# time.sleep(5)
# driver.find_element_by_name("czCashAmount").clear()
# driver.find_element_by_name("czCashAmount").send_keys("500")
# time.sleep(3)
# driver.find_element_by_link_text(u"选择部门").click()
# time.sleep(5)
# lis=driver.find_elements_by_xpath('//div/ul')
# for li in lis:
#     if u"美容部" in li.text:
#         li.click()
#         break
# time.sleep(2)
# driver.find_element_by_xpath('//button[@onclick="czConfirm(1,this,2)"]').click()





# m=driver.find_element_by_id('selNS6_chzn')
# m.find_element_by_id("selNS6_chzn_o_1").click()
# time.sleep(5)
# selBPM_chzn_o_1

# driver.find_element_by_xpath("//div/div[1]/div[3]/div[2]/div[1]/div[1]/ul/li[3]").click()
# driver.find_element_by_xpath("//div[7]/ul/li[1]").click()
# time.sleep(5)
# driver.find_element_by_xpath("//div[@onclick='save()']").click()
# time.sleep(5)
# driver.find_element_by_link_text("立即买单").click()
# time.sleep(5)
# driver.find_element_by_xpath("//td[7]/div[3]").click()
# time.sleep(5)
# driver.find_element_by_link_text("结账").click()




# #找到 id 为 dropdown1的父元素
# WebDriverWait(driver, 10).until(lambda the_driver:the_driver.find_element_by_class_name('chzn-results').is_displayed())
# #在父亲元件下找到 link 为 Action 的子元素
# menu = driver.find_element_by_class_name('chzn-results').find_element_by_link_text('美容部')
# #鼠标定位到子元素上
# webdriver.ActionChains(driver).move_to_element(menu).perform()
# time.sleep(2)

# driver.find_element_by_xpath("(//button[@onclick='newSeachMember(this)'])[2]").click()
# time.sleep(5)
# driver.find_element_by_name("czCashAmount").clear()
# driver.find_element_by_name("czCashAmount").send_keys("100")
# time.sleep(3)
# driver.find_element_by_link_text(u"选择部门").click()
# time.sleep(3)
# driver.find_element_by_css_selector("a.chzn-single.chzn-single-with-drop > div > b").click()
# # driver.find_element_by_css_selector('div.chzn-drop ul.chzn-results li#sel8QA_chzn_o_1.active-result').click()
# time.sleep(3)
# driver.find_element_by_xpath("//button[@onclick='czConfirm(1,this,2)']").click()
# time.sleep(3)



# from selenium.webdriver.support.select import  Select
# select=Select(driver.find_element_by_id('XXXXXXX'))
# select.select_by_visible_text('美容部')

#鼠标移动到子元素上
# webdriver.ActionChains(driver).move_to_element(menu).perform().click()
# time.sleep(5)


# # 开单项目操作
# time.sleep(5)
# driver.find_element_by_link_text(u"手工开单").click()
# time.sleep(5)
# driver.find_element_by_xpath("//div[1]/div[3]/div[2]/div[1]/div[2]/ul/li[2]").click()
# # /html/body/div[1]/div[4]/div[2]/ul[1]/li[2]/a
# # /html/body/div[1]/div[5]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[2]/ul/li[2]
# # /html/body/div[1]/div[5]/div[2]/div/div[1]/div[3]/div[2]/div[3]/ul/li[1]
# # /html/body/div[1]/div[5]/div[2]/div/div[1]/div[3]/div[2]/div[3]/ul/li[2]
# driver.find_element_by_xpath("//div[3]/ul/li[2]").click()
# time.sleep(5)

# 开单商品操作
# time.sleep(5)
# driver.find_element_by_link_text(u"手工开单").click()
# time.sleep(5)
# driver.find_element_by_xpath("//div/div[1]/div[3]/div[2]/div[1]/div[1]/ul/li[3]").click()
# # /html/body/div[1]/div[4]/div[2]/ul[1]/li[2]/a
# # /html/body/div[1]/div[5]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[1]/ul/li[3]
# # /html/body/div[1]/div[5]/div[2]/div/div[1]/div[3]/div[2]/div[7]/ul/li[1]
# driver.find_element_by_xpath("//div[7]/ul/li[1]").click()
# time.sleep(5)

# driver.find_element_by_xpath("//div[@onclick='save()']").click()
# time.sleep(5)
# driver.find_element_by_link_text("立即买单").click()
# time.sleep(5)
# driver.find_element_by_xpath("//td[7]/div[3]").click()
# time.sleep(5)
# driver.find_element_by_link_text("结账").click()
