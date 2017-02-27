#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class Firefox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        self.driver.quit()

    def test_open_and_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(5)

        # move mouse to setting link
        link = driver.find_element_by_link_text(u"设置")
        ActionChains(driver).move_to_element(link).perform()
        time.sleep(3)

        # click search setting
        #driver.find_element_by_class_name("setpref").click()
        driver.find_element_by_link_text(u"搜索设置").click()
        time.sleep(3)

        # save setting
        driver.find_element_by_class_name("prefpanelgo").click()
        time.sleep(3)

        # accept alert dialog
        # driver.switch_to_alert().accept()
        driver.switch_to.alert.accept()
        time.sleep(3)
        

if __name__ == "__main__":
    unittest.main()
