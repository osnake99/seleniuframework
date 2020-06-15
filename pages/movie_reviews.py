from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MovieReviews(BasePage):
    URL = "https://www.douban.com/"
    MOVIE_TAG = (By.CLASS_NAME, "lnk-movie")
    SEARCH_BAR = (By.ID, "inp-query")
    SEARCH_KEYS = "天气之子"
    SEARCH_BUTTON = (By.XPATH, "//input[@type='submit']")
    ITEMS = (By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/a")

    def __init__(self, driver):
        super().__init__(driver=driver,url=self.URL)

    def search(self):
        self.open() # 打开网站
        self.click_element(webelement=self.find_element(*self.MOVIE_TAG)) # 点击电影标签
        self.switch_new_window() # 切换到新窗口
        self.send_keys(webelement=self.find_element(*self.SEARCH_BAR),keys=self.SEARCH_KEYS) # 输入搜索关键字
        self.click_element(webelement=self.find_element(*self.SEARCH_BUTTON)) # 点击搜索按钮
        self.click_element(webelement=self.find_element(*self.ITEMS)) # 点击第一条搜索结果
