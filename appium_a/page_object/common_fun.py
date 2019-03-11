from appium_a.page_object.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from appium_a.page_object.desired_caps import appium_desired

class Common(BaseView):

    loginRegisterBtn = (By.ID,'howbuy.android.piggy:id/tv_login_register')
    loginBtn = (By.ID,'howbuy.android.piggy:id/btnLogin')
    change_login_typeBtn=(By.ID,'	howbuy.android.piggy:id/tv_pwd_login')

    def check_loginRegisterBtn(self):
        logging.info("============loginRegisterBtn===============")

        try:
            element = self.driver.find_element(*self.loginRegisterBtn)
        except NoSuchElementException:
            logging.info('loginRegisterBtn element is not found!')
        else:
            logging.info('click loginRegisterBtn')
            element.click()

    def check_loginBtn(self):
        logging.info("==========check_loginBtn===========")
        try:
            element = self.driver.find_element(*self.loginBtn)
        except NoSuchElementException:
            logging.info('loginBtn element is not found!')
        else:
            logging.info('click loginBtn')
            element.click()

    def check_change_login_typeBtn(self):
        logging.info("==========check_change_login_typeBtn===========")
        try:
            element = self.driver.find_element(*self.change_login_typeBtn)
        except NoSuchElementException:
            logging.info('change_login_typeBtn element is not found!')
        else:
            logging.info('click change_login_typeBtn')
            element.click()

if __name__ == '__main__':

    driver = appium_desired()
    com = Common(driver)
    com.check_loginRegisterBtn()
    com.check_loginBtn()
    com.check_change_login_typeBtn()