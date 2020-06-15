import unittest
from unittest import skip

from pages.brower_engine import BrowerEngine
from pages.login_page import LoginPage



class TestLogin(unittest.TestCase):
    driver = BrowerEngine().init_driver()

    def test_login(self):
        LoginPage(driver=self.driver).login()
