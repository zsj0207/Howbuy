import logging
from Howbuy.common.desired_caps import  appium_desired
from Howbuy.common.common_fun import Common, By
from selenium.common.exceptions import NoSuchElementException

class LoginView(Common):
    # 登录界面元素
    username_type = (By.ID, 'howbuy.android.piggy:id/input_userid')
    password_type = (By.ID, 'howbuy.android.piggy:id/input_password')
    loginBtn = (By.ID, 'howbuy.android.piggy:id/tv_login')

    # 跳过设置指纹
    skipBtn = (By.ID, 'howbuy.android.piggy:id/tv_skip')

    # 退出操作相关元素
    settingBtn = (By.ID, 'howbuy.android.piggy:id/lay_acctmgr')
    logoutBtn = (By.ID, 'howbuy.android.piggy:id/btn_logout')
    tip_commit = (By.ID, 'android:id/button1')

    def login_action(self, username, password):
        self.check_change_login_typeBtn()
        # self.check_btn_we_startBtn()
        self.check_tv_jumBtn()
        self.check_btnJump()

        logging.info('============login_action==============')
        logging.info('username is:%s' % username)
        self.driver.find_element(*self.username_type).clear()
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('password is:%s' % password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished!')

    def check_loginStatus(self):
        logging.info('==========check_loginStatus===========')
        try:
            self.driver.find_element(*self.skipBtn).click()
            self.driver.find_element(*self.username)
        except NoSuchElementException:
            logging.error('login Fail!')
            self.getScreenShot('login Fail')
            return False
        else:
            logging.info('login success!')
            l.logout_action()
            return True

    def logout_action(self):
        logging.info('=========logout_action==========')
        self.driver.find_element(*self.settingBtn).click()
        self.driver.find_element(*self.logoutBtn).click()
        self.driver.find_element(*self.tip_commit).click()


if __name__ == '__main__':
    driver = appium_desired()
    l = LoginView(driver)
    l.login_action('18367344667', 'qq1111')
    l.check_loginStatus()