from appium import webdriver
import unittest
from time import sleep


class MeenaBazarAPI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={'platformName': 'Android',
                                  'automationName': 'UiAutomator2',
                                  'app-package': 'com.meenaclick.customer',
                                  'app-activity': 'com.meenaclick.customer.MainActivity',
                                  'noReset': True,
                                  'fullReset': False,
                                  'app': 'C:/Users/Ifran Uddin/PycharmProjects/Appium-Python-Client/apk/MeenaClick_2.1.7.apk'
                                  })

    # def test_003_Contact_Us(self):
    #     self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Customer Support"]').click()
    #     self.driver.find_element_by_accessibility_id('Call for Order').click()
    #     # self.driver.refresh()
    #
    # def test_001_product_search(self):
    #     self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Search"]').click()
    #     sleep(1)
    #     self.driver.hide_keyboard()
    #     sleep(1)
    #
    #     # self.driver.find_element_by_xpath('//android.view.View/android.widget.EditText[text(), "Search Products"]').click()
    #     # sleep(3)
    #     # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()
    #     # self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys('A')
    #     # self.driver.find_element_by_xpath('//*[@class= android.widget.EditText]').send_keys('Aarong Ghee')
    #     sleep(3)
    #
    # def test_Offer(self):
    #     self.driver.find_element_by_accessibility_id('Offers 87').click()
    # self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Offers 87"]"]').click()

    #
    # def test_002_Menu(self):
    #     self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Menu"]').click()

    # def test_004_User(self):
    #     # sleep(5)
    #     self.driver.find_element_by_xpath('//android.view.View[@content-desc="User Tab 4 of 5"]').click()
    #     self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Tap to Login"]').click()
    #     self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="Log In"]').click()
    #     sleep(2)

    # def test_005_Menu_BabyCare(self):
    #     self.driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Menu"]').click()
    #     self.driver.find_element_by_xpath('//android.view.View[@content-desc="Baby Care"]').click()

    def test_006_Menu_Area(self):
        self.driver.find_element_by_accessibility_id('Area: Select Delivery Area').click()

    def tearDown(self):
        self.driver.quit()
        print("Test concluded")


if __name__ == '__main__':
    unittest.main()
