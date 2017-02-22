# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from HTMLTestRunner import HTMLTestRunner
import unittest, time
# import sys


class TestMountain(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_it_is_true(self):
        self.assertTrue(1 == 0)
        #self.assertTrue(1 != 0)

    def test_it_is_false(self):
        self.assertFalse(1 == 0)

    # def suite():
    # loader = unittest.TestLoader()
    # suite = unittest.TestSuite()
    # suite.addTests(loader.loadTestsFromTestCase(TestMountain))
    # return suite

def fun_suite():
    suite = unittest.TestSuite()#创建测试套
    loader = unittest.TestLoader() #加载
    suite.addTest(loader.loadTestsFromTestCase(TestMountain))#把用例加载到测试套
    return suite #返回测试套

if __name__ == "__main__":
    #自定义报告
    fp = open('./test_result_%s.html'% time.strftime("%Y-%m-%d %H-%M-%S"),'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u"测试报告",
                            description=u"测试的执行情况：")
    runner.run(fun_suite())
    fp.close()
    # sys.exit(0)