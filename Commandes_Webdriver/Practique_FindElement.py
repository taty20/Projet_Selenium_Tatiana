#import selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.google.ca/")
time.sleep(4)
driver.find_elements(By.XPATH,"//ul[@role='lisbox']//li//descedant::div[@role='option']/div/span")
time.sleep(4)
print(len(list_elements))
    if element.text=="selenium webdriver"
        element.click()
    break
time.sleep(4)


#driver.close()