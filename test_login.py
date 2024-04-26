import time

from selenium import webdriver


def test_login():
    driver = webdriver.Chrome()
    base_url = 'https://www.saucedemo.com/'
    driver.get(base_url)
    time.sleep(5)

    print("Start Test")
    driver.find_element('xpath', '//input[@data-test="username"]').send_keys('standard_user')
    driver.find_element('xpath', '//input[@data-test="password"]').send_keys('secret_sauce')
    driver.find_element('xpath', '//input[@data-test="login-button"]').click()
    time.sleep(5)


