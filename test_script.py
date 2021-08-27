"""
A simple selenium test example written by python
"""

import unittest
import logging
from datetime import datetime

# import numpy as np
# import cv2
# import pyautogui

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content = '''Try your luck now - https://www.dotprs.nyc/'''

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

    def getName(self):
        now = datetime.now() 
        name = now.strftime("%H:%M:%S")
        return name

    def clickSimpleAlertOK(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        print("alert accepted")

    def captureImage(self):
        """Capture Image"""
        self.driver.save_screenshot("some_file_"+self.getName()+".png")

    def sendEmail(self):
        #The mail addresses and password
        sender_address = 'womeninclouds@gmail.com'
        sender_pass = 'Urspkhxurs123'
        #receiver_address = 'iif3@cornell.edu'
        receiver_address = 'veredflis@gmail.com'
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Parking Automation'   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')

    # def test_case_1(self):
    #     """vered"""
    #     try:
    #         web_url = 'https://www.dotprs.nyc/'
    #         self.driver.get(web_url)
    #         print("Opened " +web_url+" /n")
    #         self.captureImage()
    #         el = self.driver.find_element_by_class_name('navbar-toggle')
    #         el.click()
    #         self.captureImage()
    #         self.sendEmail()
    #     except NoSuchElementException as ex:
    #         self.fail(ex.msg)

    # def test_case_2(self):
    #     """vered"""
    #     try:
    #         web_url = 'https://www.tutorialsteacher.com/codeeditor?cid=js-1'
    #         self.driver.get(web_url)
    #         print("Opened " +web_url+" /n")
            
    #         # Wait for 5 seconds to load the webpage completely
    #         time.sleep(2)
    #         # Find the button using text
    #         # buttons = self.driver.find_element_by_xpath('//button[contains(text(), "Try it")]').click()

    #         self.clickSimpleAlertOK()
    #         self.clickSimpleAlertOK()
    #         self.clickSimpleAlertOK()
    #         self.clickSimpleAlertOK()

    #         self.captureImage()
    #         self.sendEmail()
    #     except NoSuchElementException as ex:
    #         self.fail(ex.msg)

    def test_case_3(self):
        """vered"""
        try:
            web_url = 'https://www.dotprs.nyc/'
            self.driver.get(web_url)
            print("Opened " +web_url+" /n")
            
            # Wait for 5 seconds to load the webpage completely
            time.sleep(2)
            # Find the button using text
            # buttons = self.driver.find_element_by_xpath('//button[contains(text(), "Try it")]').click()

            # click OK on message:
            self.clickSimpleAlertOK()
            #click start
            el = self.driver.find_element_by_class_name('form-next')
            el.click()
            #click on relevat parking:
            el2 = self.driver.find_element_by_id('nid-31')
            el2.click()
            time.sleep(2)

            self.captureImage()
            # click Next
            self.driver.find_element_by_xpath("//input[@value='Next >']").click()

            #Fill in Form:
            firstName = self.driver.find_element_by_id('edit-field-first-name-und-0-value')
            firstName.send_keys("Keren")

            lastName = self.driver.find_element_by_id('edit-title')
            lastName.send_keys("Flis")

            phone = self.driver.find_element_by_id('edit-field-phone-number-und-0-value')
            phone.send_keys("6072622453")

            email = self.driver.find_element_by_id('edit-field-email-address-und-0-email')
            email.send_keys("iif3@cornell.edu")

            adress = self.driver.find_element_by_id('edit-field-address-und-0-value')
            adress.send_keys("24-12 42nd Rd, APT 4C")

            zip = self.driver.find_element_by_id('edit-field-zipcode-und-0-value')
            zip.send_keys("11101")

            dmv = self.driver.find_element_by_id('edit-field-dmv-number-und-0-value')
            dmv.send_keys("887991027")
             
            self.captureImage()

            submitBtn = self.driver.find_element_by_id('edit-submit--2')
            submitBtn.click()

            time.sleep(5)
            # self.captureImage()

            # self.sendEmail()
        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
