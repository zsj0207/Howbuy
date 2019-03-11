from appium import webdriver
import yaml
from selenium.common.exceptions import NoSuchElementException
import logging
import  logging.config

file = open('../yaml/desired_caps.yaml','r')
data = yaml.full_load(file)

CON_LOG = 'log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

# logging.basicConfig(level=logging.INFO,filename='runlog.log',
#                     format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s')

desired_caps = {}
desired_caps['platformName']=data['platformName']
desired_caps['platformVersion']=data['platformVersion']
desired_caps['deviceName']=data['deviceName']

desired_caps['app']=data['app']
desired_caps['appPackage']=data['appPackage']
desired_caps['appActivity']=data['appActivity']
desired_caps['noReset']=data['noReset']
desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
desired_caps['resetKeyboard'] = data['resetKeyboard']

logging.info('start app...')
driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)

def check_loginRegisterBtn():
    logging.info("check loginRegisterBtn")
    try:
        loginRegisterBtn = driver.find_element_by_id('howbuy.android.piggy:id/register').click()
    except NoSuchElementException:
        logging.info('No loginRegisterBtn')
    else:
        loginRegisterBtn.click()

def check_loginBtn():
    logging.info("check loginBtn")
    try:
        loginBtn = driver.find_element_by_id('howbuy.android.piggy:id/btnLogin').click()
    except NoSuchElementException:
        logging.info('No loginBut')
    else:
        loginBtn.click()

check_loginBtn()
check_loginRegisterBtn()