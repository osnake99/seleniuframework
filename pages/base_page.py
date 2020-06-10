from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings


class BasePage(object):
    def __init__(self, driver, url):
        self._driver = driver
        self._url = url

    # 打开指定网页
    def open(self):
        # 浏览器窗口最大化
        self._driver.maximize_window()
        self._driver.get(url=self._url)

    # 定位元素并返回
    def find_element(self, *locator, timeout=None):
        try:
            return self._init_wait(timeout).until(EC.visibility_of_element_located(locator=locator))
        except (NoSuchElementException, TimeoutException):
            self._driver.quit()
            raise TimeoutException(msg="定位元素失败，方式为{}".format(locator))

    def send_keys(self, webElement, keys):
        print(webElement)
        webElement.clear()
        webElement.send_keys(keys)

    def click_element(self, webElement):
        webElement.click()

    def switch_frame(self, webElement):
        self._driver.switch_to.frame(webElement)
        print("已跳转iframe")

    # 显示等待方法
    def _init_wait(self, timeout):
        if timeout is None:
            return WebDriverWait(driver=self._driver,
                                 timeout=settings.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self._driver, timeout=timeout)
