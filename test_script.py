"""
A simple selenium test example written by python
"""

import unittest
# import numpy as np
# import cv2
# import pyautogui

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class TestTemplate(unittest.TestCase):
    """Include test cases on a given url"""

    def setUp(self):
        """Start web driver"""
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        """Stop web driver"""
        self.driver.quit()

    def test_case_1(self):
        """Find and click top-left logo button"""
        try:
            self.driver.get('https://www.dotprs.nyc/')
            el = self.driver.find_element_by_class_name('navbar-toggle')
            el.click()
            self.driver.save_screenshot("some_file.png")
            # # take screenshot using pyautogui
            # image = pyautogui.screenshot()
            
            # # since the pyautogui takes as a 
            # # PIL(pillow) and in RGB we need to 
            # # convert it to numpy array and BGR 
            # # so we can write it to the disk
            # image = cv2.cvtColor(np.array(image),
            #                     cv2.COLOR_RGB2BGR)
            
            # # writing it to the disk using opencv
            # cv2.imwrite("image1.png", image)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

    # def test_case_2(self):
    #     """Find and click top-right Start your project button"""
    #     try:
    #         self.driver.get('https://www.oursky.com/')
    #         el = self.driver.find_element_by_class_name("header__cta")
    #         el.click()
    #     except NoSuchElementException as ex:
    #         self.fail(ex.msg)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
