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

    def find_elements(self, *locator, index=0, timeout=None):
        try:
            elements = self._driver.find_elements(*self.locator)
            # self._init_wait(timeout).until(EC.visibility_of_all_elements_located_located(locator=locator))
            return elements[index]
        except (NoSuchElementException, TimeoutException):
            self._driver.quit()
            raise TimeoutException(msg="定位元素失败，方式为{}".format(locator))

    # 在指定元素中输入文字
    def send_keys(self, webelement, keys):
        print(webelement)
        webelement.clear()
        webelement.send_keys(keys)

    # 点击指定元素
    def click_element(self, webelement):
        webelement.click()

    # 切换到指定的iframe框架
    def switch_frame(self, webelement):
        self._driver.switch_to.frame(webelement)
        print("已跳转iframe")

    # 切换到最新的标签页
    def switch_new_window(self):
        windows = self._driver.window_handles
        self._driver.switch_to.window(windows[-1])

    # 显示等待方法
    def _init_wait(self, timeout):
        if timeout is None:
            return WebDriverWait(driver=self._driver,
                                 timeout=settings.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self._driver, timeout=timeout)
