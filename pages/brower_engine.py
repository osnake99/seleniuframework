from selenium import webdriver

import settings


class BrowerEngine:
    def init_driver(self):
        option = webdriver.ChromeOptions()
        # 去掉“chrome正受到自动测试软件的控制”信息栏显示配置
        option.add_experimental_option("excludeSwitches", ['enable-automation'])
        option.add_experimental_option("useAutomationExtension", False)

        driver = webdriver.Chrome(chrome_options=option,
                                  executable_path=settings.EXECUTABLE_PATH)
        return driver