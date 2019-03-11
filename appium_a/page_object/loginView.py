import  logging
from appium_a.page_object.common_fun import Common
from appium_a.page_object.desired_caps import appium_desired
from selenium.webdriver.common.by import By

class LoginView(Common):

    change_login_typeBtn=(By.ID,'	howbuy.android.piggy:id/tv_pwd_login')
    username_type=(By.ID,'howbuy.android.piggy:id/input_userid')
    password_type=(By.ID,'	howbuy.android.piggy:id/input_password')
    loginBtn=(By.ID,'	howbuy.android.piggy:id/tv_login')


    def login_action(self,username,password):
        self.check_loginBtn()
        self.check_loginRegisterBtn()
        # self.driver.find_element(*self.change_login_typeBtn).click()
        self.change_login_typeBtn()

        logging.info('===============login===============')
        logging.info('input username:%s'%username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('input password:%s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn.')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished ')

if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('13758070569','qq1111')