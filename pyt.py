from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

xbutton = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )


#button.click()
#message = browser.find_element_by_id("verify_message")

#input1 = browser.find_element_by_name("firstname")
#input1.send_keys("Ivan")
#input1 = browser.find_element_by_name("lastname")
#input1.send_keys("Pavlov")
#input1 = browser.find_element_by_name("email")
#input1.send_keys("@mai.ru")

#current_dir = os.path.abspath(os.path.dirname(__file__))    
#file_path = os.path.join(current_dir, 'test.txt')           

#element = browser.find_element_by_id('file')
#element.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()

#confirm = browser.switch_to.alert
#confirm.accept()

#new_window = browser.window_handles[1]
#browser.switch_to.window(new_window)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)

button = browser.find_element_by_id("solve")
button.click()

time.sleep(10)
browser.quit()
    
