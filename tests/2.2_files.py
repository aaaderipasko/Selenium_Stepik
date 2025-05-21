from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    link = 'https://suninjuly.github.io/file_input.html'
    browser.get(link)

    name = browser.find_element(By.NAME, 'firstname')
    name.send_keys('Name')

    lastname = browser.find_element(By.NAME, 'lastname')
    lastname.send_keys('Lastname')

    email = browser.find_element(By.NAME, 'email')
    email.send_keys('test@test.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text_file.txt')
    choose_file_btn = browser.find_element(By.ID, 'file')
    choose_file_btn.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button.click()

finally:
    time.sleep(10)
    browser.quit()
