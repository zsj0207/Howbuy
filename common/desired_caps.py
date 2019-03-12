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

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir,'app',data['appname'])
    print('====base_dir===='+base_dir)
    print('====app_path===='+app_path)

    desired_caps['app']=app_path
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']

    logging.info('start app...')
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    print(driver)
    return driver

if __name__ == '__main__':
    appium_desired()
    # with open('../config/desired_caps.yaml', 'r',encoding='UTF-8') as file:
    #     data = yaml.full_load(file)
    # print(os.path.dirname(__file__))
