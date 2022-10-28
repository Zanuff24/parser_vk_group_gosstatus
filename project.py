from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import csv
import config


#opensiteVK()
#def opensiteVK():
try:
    link_login='https://vk.com/'
    link_pass=''
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link_login)
    input_email = browser.find_element(By.ID,'index_email')
    input_email.send_keys(config.login)

    button_go_to_password = browser.find_element(By.CSS_SELECTOR,'button[class="FlatButton FlatButton--primary FlatButton--size-l FlatButton--wide VkIdForm__button VkIdForm__signInButton"]')
    button_go_to_password.click()

    input_password = browser.find_element(By.CSS_SELECTOR,'input[placeholder="Введите пароль"]')
    input_password.send_keys(config.pasword)

    time.sleep(5)
    button_auto = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    button_auto.click()
finally:
    time.sleep(10)
    #browser.quit()


