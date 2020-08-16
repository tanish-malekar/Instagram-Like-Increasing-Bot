import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import random

username = "tanish_malekar"
password = "Tanman#123"

driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Desktop\chromedriver.exe')
driver.get("https://www.instagram.com/")

username_input = WebDriverWait(driver,60).until(lambda driver: driver.find_element_by_xpath(r'//*[@id="loginForm"]/div/div[1]/div/label/input'))
username_input.click()
username_input.send_keys(username)

password_input = WebDriverWait(driver,60).until(lambda driver: driver.find_element_by_xpath(r'//*[@id="loginForm"]/div/div[2]/div/label/input'))
password_input.click()
password_input.send_keys(password)

login_button = WebDriverWait(driver,60).until(lambda driver: driver.find_element_by_xpath(r'//*[@id="loginForm"]/div/div[3]/button/div'))
login_button.click()

try:
    not_now_button=WebDriverWait(driver,60).until(lambda driver: driver.find_element_by_xpath(r'//*[@id="react-root"]/section/main/div/div/div/div/button'))
    not_now_button.click()
except selenium.common.exceptions.NoSuchElementException:
    pass

try:
    not_now_button=WebDriverWait(driver,60).until(lambda driver: driver.find_element_by_xpath(r'/html/body/div[4]/div/div/div/div[3]/button[2]'))
    not_now_button.click()
except selenium.common.exceptions.NoSuchElementException:
    pass

search = WebDriverWait(driver,60).until(lambda driver: driver.find_element_by_xpath(r'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div'))
search.click()

search = WebDriverWait(driver,60).until(lambda driver: driver.find_element_by_xpath(r'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input '))
search.send_keys("likeforlikes")
time.sleep(4)
search.send_keys(Keys.RETURN)
search.send_keys(Keys.RETURN)

time.sleep(random.randint(4, 12))
picture = WebDriverWait(driver,60).until(lambda driver: driver.find_element_by_xpath(r'//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div'))
picture.click()

next_button = WebDriverWait(driver,60).until(lambda driver: driver.find_element_by_xpath(r'/html/body/div[4]/div[1]/div/div/a'))
for i in range(50000):
    time.sleep(random.randint(2,4))
    try:
        like_button=WebDriverWait(driver,60).until(lambda driver: driver.find_element_by_css_selector("span.fr66n > button > div > span > svg"))
    except selenium.common.exceptions.TimeoutException:
        print("Timeout Error")
        next_button.click()
        continue
    if(like_button.get_attribute('aria-label')=="Like"):
        like_button.click()
        time.sleep(random.randint(1, 2))
        next_button.click()
    else:
        next_button.click()
    print(i)



