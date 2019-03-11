from ..baseView.baseView import BaseView
from ..common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging.config
from selenium.webdriver.common.by import By
import os
import time
import csv


class Common(BaseView):
    # 跳过开始引导页
    btn_we_startBtn = (By.ID, 'howbuy.android.piggy: id / btn_we_start')
    # 跳过选择标签页面
    tv_jumBtn = (By.ID, 'howbuy.android.piggy: id / tv_jump')
    # 跳过引导按钮
    btnJump = (By.ID, 'howbuy.android.piggy:id/btnJump')


    def check_btn_we_startBtn(self):
        logging.info("============check_skipBtn===============")

        try:
            element = self.driver.find_element(*self.btn_we_startBtn)
        except NoSuchElementException:
            logging.info('btn_we_startBtn element is not found!')
        else:
            logging.info('click check_btn_we_startBtn')
            element.click()

    def check_tv_jumBtn(self):
        logging.info("==========check_tv_jumBtn===========")
        try:
            element = self.driver.find_element(*self.tv_jumBtn)
        except NoSuchElementException:
            logging.info('tv_jumBtn element is not found!')
        else:
            logging.info('click tv_jumBtn')
            element.click()

    def check_btnJump(self):
        logging.info("==========check_btnJump===========")
        try:
            element = self.driver.find_element(*self.btnJump)
        except NoSuchElementException:
            logging.info('btnJump element is not found!')
        else:
            logging.info('click btnJump')
            element.click()

    def get_screenSize(self):
        '''
        获取屏幕尺寸
        :return:
        '''
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return (x, y)

    def swipeLeft(self):
        logging.info('swipeLeft')
        l = self.get_screenSize()
        y1 = int(l[1] * 0.5)
        x1 = int(l[0] * 0.95)
        x2 = int(l[0] * 0.25)
        self.swipe(x1, y1, x2, y1, 1000)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    def get_csv_data(self, csv_file, line):
        '''
        获取csv文件指定行的数据
        :param csv_file: csv文件路径
        :param line: 数据行数
        :return:
        '''
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row


if __name__ == '__main__':
    driver = appium_desired()
    # c=Common(driver)
    # c.check_btn_we_startBtn()
    # # c.check_skipBtn()
    # c.swipeLef()
    # c.swipeLef()
    # c.getScreenShot("startApp")