#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


"""
导入 from selenium.webdriver.commom.action_chains import ActionChains
setUp , TearDown,打开百度
鼠标悬停设置 ActionChains().move_to_element().perform
点击“搜索设置”
保存设置--再处理弹出框driver.swith_to_alert().accept()或者driver.swith_to.alert.accept()
33行 hagperform()的作用???
"""
class baidu_setting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie(r"C:\Program Files (x86)\Internet Explorer"
                                   r"\IEDriverServer.exe")
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)#只能等待
        self.driver.maximize_window() #窗口最大化
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        self.driver.quit()

    def baidu_openAndsearch(self):#打开、搜索
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(3)

        #move mouse to setting link 鼠标移动到设置上
        link = driver.find_element_by_link_text(u"设置").click()
        ActionChains(driver).move_to_element(link).perform() #.perform()的作用
        time.sleep(3)

        #click search setting  点击搜索设置
        # driver.find_element_by_class_name("setpref").click()
        driver.find_element_by_link_text(u"搜索设置").click()
        time.sleep(3)

        #save setting 保存设置
        # driver.find_element_by_class_name("prefpanelgo").click()
        driver.find_element_by_link_text(u"保存设置").click()
        time.sleep(3)

        #处理弹框
        # driver.switch_to_alert().accept()#已过时，可以用
        driver.switch_to.alert.accept()
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
