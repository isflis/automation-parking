"""
A simple selenium test example written by python
"""

import unittest
import logging
import threading
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
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            print("alert accepted")
            return True
        except:
            print("Couldn't find OK button")
            return False

    def captureImage(self):
        """Capture Image"""
        self.driver.save_screenshot("some_file_"+self.getName()+".png")

    def clickOnCourtYard(self):
        try:
            el2 = self.driver.find_element_by_id('nid-31')
            el2.click()
            return True
        except:
            print("Couldn't click on Court Yard option...")
            return False
        

    def fillRegistrationForm(self):
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

    def submitForm(self):
        submitBtn = self.driver.find_element_by_id('edit-submit--2')
        submitBtn.click()

    def openWebSite(self, url):
        web_url = url 
        self.driver.get(web_url)
        print("Opened " +web_url+" /n")      

    def clickNextBtn(self):
        self.driver.find_element_by_xpath("//input[@value='Next >']").click()

    def startTask(self):
        try:
            print("Starting Filling Form")
            self.sendEmail("Starting Filling Registration Form")

            #click start
            el = self.driver.find_element_by_class_name('form-next')
            el.click()
            self.captureImage()

            #click on relevat parking:
            isSpaceLeft = self.clickOnCourtYard()
            if isSpaceLeft:
                time.sleep(2)
                self.captureImage()

                # click Next
                self.clickNextBtn()

                self.fillRegistrationForm()
                self.submitForm()
                time.sleep(5)
                return True
            else:
                print("No more space left on Court Yard parking")
                return False
            return False
        except:
            print("Task Failed")
            return False

    def sendEmail(self, text):
        mail_content = text # '''Starting Filling Registration Form for - https://www.dotprs.nyc/'''
        #The mail addresses and password
        sender_address = 'womeninclouds@gmail.com'
        sender_pass = 'Urspkhxurs123'
        receiver_address = 'iif3@cornell.edu'
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


    def test_case_3(self):
        """Starting Parking Automation"""
        # press ctrl+Z to stop the script
        try:
            while True:
                url='https://www.dotprs.nyc/';  
                self.openWebSite(url)
                # Wait for 2 seconds to load the webpage completely
                time.sleep(2)
                # click OK on message:
                while self.clickSimpleAlertOK() == False:
                    print("The registration is closed. Trying in 30sec")
                    time.sleep(30)
                    # add function to send email at 09:30am
                else:
                    print("The registration is now open")
                    isTaskCompleted = self.startTask()
                    if isTaskCompleted:
                        print("Finished Task")
                        self.sendEmail("The registration is completed")
                    else:
                        print("Finished Task")
                        self.sendEmail("Failed to register")
                    time.sleep(60*60*23*20)
        except NoSuchElementException as ex:
            self.fail(ex.msg)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTemplate)
    unittest.TextTestRunner(verbosity=2).run(suite)
