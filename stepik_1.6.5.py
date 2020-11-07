from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = str(math.ceil(math.pow(math.pi, math.e)*10000)) #переменная
    
    text = browser.find_element_by_partial_link_text(x) #подставить переменную на команду
    text.click()
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Meruyert")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Yechshan")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Aktau")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Kazakhstan")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла