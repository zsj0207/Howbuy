from appium import webdriver
import yaml
from selenium.common.exceptions import NoSuchElementException
import logging
import logging.config
import os


CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

# logging.basicConfig(level=logging.INFO,filename='runlog.log',
#                     format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s')

def appium_desired():
    with open('../config/desired_caps.yaml', 'r',encoding='UTF-8') as file:
        data = yaml.full_load(file)
    desired_caps = {}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']

    base_dir=os.path.dirname(os.path.dirname(__file__))
    app_path=os.path.join(base_dir,'app',data['app'])
    print(base_dir)
    print(app_path)
    desired_caps['app']=app_path
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']

    logging.info('start app...')
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    return driver

# def check_loginRegisterBtn():
#     logging.info("check loginRegisterBtn")
#     try:
#         loginRegisterBtn = driver.find_element_by_id('howbuy.android.piggy:id/register').click()
#     except NoSuchElementException:
#         logging.info('No loginRegisterBtn')
#     else:
#         loginRegisterBtn.click()
#
# def check_loginBtn():
#     logging.info("check loginBtn")
#     try:
#         loginBtn = driver.find_element_by_id('howbuy.android.piggy:id/btnLogin').click()
#     except NoSuchElementException:
#         logging.info('No loginBut')
#     else:
#         loginBtn.click()
#
# check_loginBtn()
# check_loginRegisterBtn()

if __name__ == '__main__':
    appium_desired()
    # with open('../config/desired_caps.yaml', 'r',encoding='UTF-8') as file:
    #     data = yaml.full_load(file)
    # print(os.path.dirname(__file__))
