import pickle
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait
# from PIL import Image

chrome_options = Options()
chrome_options.headless = True #to see actual browser window

# chrome_options.en
chrome_options.add_argument("--window-size=1920,1200")

# DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(options= chrome_options)
driver.implicitly_wait(10) #so browser wait for 10 seconds (implicit wait)
driver.get("https://www.emirates.com/english/")


# driver.add_cookie({"name": "key", "value": "value"})
# pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
# print(driver.page_source)
# el = driver.find_element("id","onetrust-accept-btn-handler")
cookie_accept = driver.find_element(By.ID,"onetrust-accept-btn-handler")
WebDriverWait(driver,timeout=5).until(lambda a: cookie_accept is not None,"no element found")
cookie_accept.click()
# departure_airport = driver.find_element(By.NAME,"Departure airport")
# departure_airport.clear()
# departure_airport.send_keys("Toronto" + Keys.ENTER)


arrival_airport = driver.find_element(By.NAME,"Arrival airport").send_keys("Ahmedabad" + Keys.ENTER)
# arrival_airport.click()

continue_search = driver.find_element(By.CLASS_NAME,"search-flight__continue--cta").click()

# print(driver.save_screenshot("/screenshot/Step1.png"))

depart_date = driver.find_element(By.ID,"search-flight-date-picker--depart")
# depart_date.send_keys("25  Dec 22")
depart_date.click()

# calendar_depart = driver.find_elements(By.LINK_TEXT,"25")[1]
calendar_depart = driver.find_element(By.XPATH,"//a[@data-string='25112022']")
# print(calendar_depart.get_attribute("aria-label").__str__())
driver.execute_script("arguments[0].click();", calendar_depart) # clicking using js because selenium was not able to find context https://stackoverflow.com/questions/52400233/error-other-element-would-receive-the-click-in-python
# calendar_depart.click()
# calendar_depart

calendar_return = driver.find_element(By.XPATH,"//a[@data-string='2502023']")
driver.execute_script("arguments[0].click();", calendar_return)

search_flight = driver.find_element(By.XPATH,"//button[@type='submit']")
# print(search_flight.get_attribute("value").__str__())
search_flight.click()
# print(driver.page_source)

ele = driver.find_element(By.CSS_SELECTOR,"#ctl00_c_gridTableMain") 
print(ele.text.__str__())

#ctl00_c_gridTableMain > tbody > tr:nth-child(3) > td:nth-child(3) > div > a > span.fare-currency-container > strong > span.Converted-Currency-Span.converted-fare



# return_date = driver.find_element(By.ID,"search-flight-date-picker--return")
# return_date.send_keys("24  Jan 22")

# submit = driver.find_element(By.CSS_SELECTOR,"button.js-widget-submit")
# print(submit.get_attribute("type").__str__())
# WebDriverWait(driver,timeout=5).until(lambda a: submit is not None,"no element found")


# submit.click()
time.sleep(10)

# new_search_elememnt = driver.find_element(By.CLASS_NAME,"ts-session-expire--link")
# new_search_elememnt.click()
# driver.save_screenshot("/screenshot/Step3.png")
# Image.open("/screenshot/Step3.png")


# print(driver.page_source)
# driver.quit()