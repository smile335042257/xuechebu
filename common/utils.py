from appium import webdriver


def init_driver():
    capabilities = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "模拟器",
        "appPackage": "com.bjcsxq.chat.carfriend",
        "appActivity": ".MainActivity",
        'resetKeyboard': True,
        'unicodeKeyboard': True,
        # 'noReset': True   # 重置系统
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                              desired_capabilities=capabilities)
    driver.implicitly_wait(10)
    return driver


# 学车不 包名和启动名
# com.bjcsxq.chat.carfriend/.MainActivity
if __name__ == '__main__':
    init_driver()





