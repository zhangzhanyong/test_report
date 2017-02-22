# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie(r"C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe")
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"

    def tearDown(self):
        self.driver.quit()

    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium ide")
        time.sleep(2)
        driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE * 4)
        #driver.find_element_by_id("su").click()
        driver.find_element_by_css_selector("#su").click()
        time.sleep(3)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(Baidu))

    fp = open('./test_result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'百度搜索测试报告',
                            description=u"测试用例执行情况：")
    runner.run(suite)
    fp.close()
