from typing import final

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    price = WebDriverWait(browser,20).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    if price == True:
        button = browser.find_element(By.ID, 'book')
        button.click()

    input_value = browser.find_element(By.ID, "input_value")
    x = math.log(abs(12*math.sin(float(input_value.text))))

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(x)

    submit = browser.find_element(By.ID, "solve")
    submit.click()

finally:
    time.sleep(7)
    browser.quit()