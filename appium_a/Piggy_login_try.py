from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

desired_caps={}
desired_caps['platformName']='Android'

#模拟器设备
desired_caps['platformVersion']='4.4.2'
desired_caps['deviceName']='127.0.0.1:62001'

#真机
# desired_caps['platformVersion']='8.0.0'
# desired_caps['deviceName']='Nexus 6P'
# desired_caps['udid']='84B5T15A10000334'

# desired_caps['app']=r'C:\Users\Administrator\Downloads\howbuy.android.palmfund_169.apk'
# desired_caps['appPackage']='howbuy.android.palmfund'
# desired_caps['appActivity']='com.howbuy.fund.init.AtyEntry'

desired_caps['app']=r'C:\Users\Administrator\Downloads\howbuy.android.piggy_68.apk'
desired_caps['appPackage']='howbuy.android.piggy'
desired_caps['appActivity']='com.howbuy.piggy.aty.AtyMain'


desired_caps['noReset']='True'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# loginRegisterBtn=driver.find_element_by_id('howbuy.android.piggy:id/tv_login_register')
# loginBtn=driver.find_element_by_id('howbuy.android.piggy:id/btnLogin')

def check_loginRegisterBtn():
    print("check loginRegisterBtn")
    try:
        # loginRegisterBtn=driver.find_element_by_id('howbuy.android.piggy:id/tv_login_register').click()
        loginRegisterBtn = driver.find_element_by_id('howbuy.android.piggy:id/tv_login_register').click()
    except NoSuchElementException:
        print('No loginRegisterBtn')
    else:
        loginRegisterBtn.click()


def check_loginBtn():
    print("check loginBtn")
    try:
        loginBtn = driver.find_element_by_id('howbuy.android.piggy:id/btnLogin').click()
    except NoSuchElementException:
        print('No loginBut')
    else:
        loginBtn.click()


check_loginRegisterBtn()
check_loginBtn()