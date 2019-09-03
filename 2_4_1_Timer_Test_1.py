import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
browser = webdriver.Firefox(capabilities={"marionette": False})
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")

house_enable = WebDriverWait(browser, 14).until(EC.text_to_be_present_in_element((By.ID, "price"),"10000 RUR"))
#button = browser.find_element_by_id("check")
button_house = browser.find_element(By.ID, "book")
button_house.click()

button = browser.find_element(By.CSS_SELECTOR, ".btn")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
time.sleep(0.7)
y_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
y = y_element.text
print(y_element)
print(y)

def calc(y):
  return str(math.log(abs(12*math.sin(int(y)))))

print(y)
print(calc(y))

input_form = browser.find_element(By.ID, "answer") ##input_value
input_form.send_keys(calc(y))


new_button = browser.find_element(By.ID, "solve")

new_button.click()
#message = browser.find_element_by_id("check_message")

#assert "успешно" in message.text