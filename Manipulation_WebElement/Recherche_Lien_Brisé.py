#import selenium
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(4)
list_link=driver.find_elements(By.TAG_NAME,"a")
compteur=0
for link in list_link:
    url=link.get_attribute("href")
    try:
        response=requests.head(url)
    except:
        None
    if response.status_code>=400:
        print(url,"est un lien brisé")
    else:
        print(url,"est un lien valide")
    print("le nombre de lien brisé est :",compteur)
driver.close()