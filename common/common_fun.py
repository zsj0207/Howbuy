from baseView.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from common.desired_caps import appium_desired
import time,os

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

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    # def get_csv_data(self, csv_file, line):
    #     '''
    #     获取csv文件指定行的数据
    #     :param csv_file: csv文件路径
    #     :param line: 数据行数
    #     :return:
    #     '''
    #     with open(csv_file, 'r', encoding='utf-8-sig') as file:
    #         reader = csv.reader(file)
    #         for index, row in enumerate(reader, 1):
    #             if index == line:
    #                 return row


if __name__ == '__main__':

    driver = appium_desired()
    com = Common(driver)
    com.check_loginRegisterBtn()
    com.check_loginBtn()
    com.check_change_login_typeBtn()
    com.getScreenShot('startApp')