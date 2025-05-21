from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/redirect_accept.html'
browser.get(link)

try:
    button_journey = browser.find_element(By.TAG_NAME, 'button')
    button_journey.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value')
    result = math.log(abs(12 * math.sin(int(x.text))))

    result_input = browser.find_element(By.ID, 'answer')
    result_input.send_keys(str(result))

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
