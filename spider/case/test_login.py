import unittest
import time
from selenium import webdriver
from base.login import login
import pytest


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://user.tungee.com/users/sign-in")
    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        login(self,"17802198459","Hgt_17802198459")
        title=self.driver.title
        url=self.driver.current_url
        self.assertEqual((title,url),("账号登录","https://user.tungee.com/users/sign-in"))


if __name__=="__main__":
    unittest.main()