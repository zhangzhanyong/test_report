# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TwoTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_two_test_case(self):
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/bug/list/1?productmodule_id=0")
        driver.find_element_by_link_text(u"测试").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectPopUp |  | ]]
        driver.find_element_by_name("yt2").click()
        driver.find_element_by_id("BugInfoView_title").clear()
        driver.find_element_by_id("BugInfoView_title").send_keys(u"测试")
        driver.find_element_by_name("yt0").click()
        driver.find_element_by_name("yt1").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
