from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome() #lauch browser window
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link) #open the link in the browser

try:
    x = browser.find_element(By.ID, "input_value") # 2.Считать значение для переменной x

    result = math.log(abs(12 * math.sin(int(x.text)))) #3.Посчитать математическую функцию от x.

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary") #ищем кнопку
    browser.execute_script("return arguments[0].scrollIntoView(true);", button) #4.Проскроллить страницу вниз.

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(str(result)) #Ввести ответ в текстовое поле.

    checkbox = browser.find_element(By.ID, "robotCheckbox") #Выбрать checkbox "I'm the robot".
    browser.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule") #Переключить radiobutton "Robots rule!".
    browser.execute_script("arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button.click() #Нажать на кнопку "Submit".

finally:
    time.sleep(5)
    browser.quit()