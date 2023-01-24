from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

# initiate
driver = webdriver.Firefox() # initiate a driver, in this case Firefox
driver.get('https://home.shelly.cloud/#/login')

driver.implicitly_wait(15)

first_text = driver.page_source

username_box = driver.find_element(By.XPATH, "//input[@type='email']")
password_box = driver.find_element(By.XPATH, "//input[@type='password']")

username_box.send_keys('talos.uth.team@gmail.com')
password_box.send_keys('tal.osrobotix')

login_button = driver.find_element(By.TAG_NAME, 'button')
login_button.click()

room1 = driver.find_element(By.CSS_SELECTOR, 'div.list_item.svelte-jbz7rp')
time.sleep(1)
room1.click()

split_core1 = driver.find_element(By.CSS_SELECTOR, 'div.list_item.device.svelte-jbz7rp')
time.sleep(1)
split_core1.click()

while True:
    
    driver.refresh()
    time.sleep(5)
    values_page_text = driver.page_source
    soup = BeautifulSoup(values_page_text, 'lxml')
    Power_data_array = soup.find_all('span', class_ = 'svelte-nmuala')

    current_values_file = open('current_values.txt', 'w')
    i = 0
    while (i < 10):
        current_values_file.write(Power_data_array[i+1].text + ",")
        i = i +2

    current_values_file.close

    time.sleep(55)
