from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/alert_accept.html'
browser.get(link)

try:
    button_journey = browser.find_element(By.TAG_NAME, 'button')
    button_journey.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value")
    result = math.log(abs(12 * math.sin(int(x.text))))

    input_result = browser.find_element(By.ID, 'answer')
    input_result.send_keys(str(result))

    button_submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()