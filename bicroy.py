from appium import webdriver
import unittest
from time import sleep


class MeenaBazarAPI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={'platformName': 'Android',
                                  'automationName': 'UiAutomator2',
                                  # 'app-package': 'com.meenaclick.customer',
                                  # 'app-activity': 'com.meenaclick.customer.MainActivity',
                                  'app-package': 'com.bikroy.customer',
                                  'app-activity': 'com.bikroy.customer.MainActivity',
                                  'noReset': True,
                                  'fullReset': False,
                                  'app': 'C:/Users/Ifran Uddin/PycharmProjects/Appium-Python-Client/apk/Bikroy Sell Rent Buy Find Jobs_v1.2.09_apkpure.com.apk'
                                  })


    def test_001_Menu(self):
        self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Menu"]').click()



    def tearDown(self):
        self.driver.quit()
        print("Test concluded")


if __name__ == '__main__':
    unittest.main()
