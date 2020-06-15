from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.douban.com/"
    IFRAME_TAG = (By.TAG_NAME, "iframe")
    LOGIN_TYPE = (By.CLASS_NAME, "account-tab-account")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    PHONE = (By.NAME, "phone")
    LOGIN_BUTTON = (By.CLASS_NAME, "account-form-field-submit")

    def __init__(self, driver):
        super().__init__(driver=driver, url=self.URL)

    def login(self):
        self.open()
        self.switch_frame(webelement=self.find_element(*self.IFRAME_TAG, timeout=5))
        self.click_element(webelement=self.find_element(*self.LOGIN_TYPE, timeout=5))
        self.send_keys(webelement=self.find_element(*self.USERNAME), keys="aaaaaa")
        self.send_keys(webelement=self.find_element(*self.PASSWORD), keys="bbbbbb123")
        self.click_element(webelement=self.find_element(*self.LOGIN_BUTTON))
