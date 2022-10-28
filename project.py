from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import config

def openFile():
    mas_url =[]
    with open('list.csv', "r", encoding='cp1251') as fill:
        reader = csv.reader(fill, delimiter=';')
        for row in reader:
            mas_url.append(row)
    return mas_url

def saveFile(mas_url):
    with open('list.csv', "w", encoding='cp1251', newline='') as fill:
        writer = csv.writer(fill, delimiter=';')
        writer.writerows(mas_url)

def parse():
    mas_url = openFile()
    for i in mas_url:
        status = checkStatus(i[0])
        i.append(status)
        time.sleep(3)
        print(i,' status = ', status)
    saveFile(mas_url)


def checkStatus(link):
    try:
        time.sleep(2)
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR,'span[class="GovernmentCommunityBadge GovernmentCommunityBadge--tooltip"]')
        return True
    except:
        print('error')
        return False

try:
    link_login='https://vk.com/'

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link_login)
    input_email = browser.find_element(By.ID,'index_email')
    input_email.send_keys(config.login)

    button_go_to_password = browser.find_element(By.CSS_SELECTOR,'button[class="FlatButton FlatButton--primary FlatButton--size-l FlatButton--wide VkIdForm__button VkIdForm__signInButton"]')
    button_go_to_password.click()

    input_password = browser.find_element(By.CSS_SELECTOR,'input[placeholder="Введите пароль"]')
    input_password.send_keys(config.pasword)

    time.sleep(3)
    button_auto = browser.find_element(By.CSS_SELECTOR,'button[type="submit"]')
    button_auto.click()

    parse()

finally:
    time.sleep(10)
    browser.quit()


