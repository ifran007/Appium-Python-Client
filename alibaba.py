from appium import webdriver
from appium import webdriver
import unittest
from time import sleep


class AliBabaAPI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={'platformName': 'Android',
                                  'automationName': 'UiAutomator2',
                                  'app-package': 'com.alibaba.intl.android.apps.poseidon',
                                  'app-activity': 'com.alibaba.intl.android.apps.poseidon.app.activity.ActivityMainMaterial',
                                  'noReset': True,
                                  'fullReset': False,
                                  'app': 'C:/Users/Ifran Uddin/PycharmProjects/Appium-Python-Client/apk/Alibaba com Leading online B2B Trade Marketplace_v7.40.1_apkpure.com.xapk'
                                  })

    def test_001_CusElec(self):
        sleep(5)
        self.driver.find_element_by_id(
            'com.alibaba.intl.android.apps.poseidon:id/id_bottom_bar_v_activity_main_material').click()

    def tearDown(self):
        self.driver.quit()
        print("Test concluded")


if __name__ == '__main__':
    unittest.main()
