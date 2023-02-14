#import selenium
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(4)
# recupération des nbres de lignes et de collones de la table
nombres_lignes=driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr')
print(len(nombres_lignes))
nombres_colonnes=driver.find_elements(By.XPATH,'//table[@name="BookTable"]//th')
print(len(nombres_colonnes))
#récupérer la valeur d'une cellule de la table
valeur_cellule=driver.find_element(By.XPATH,'//table[@name="BookTable"]//tr[3]/td[1]')
print(valeur_cellule.text)

#récupérer toutes les données du tableau
nb_lignes=len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//tr'))
nb_colonnes=len(driver.find_elements(By.XPATH,'//table[@name="BookTable"]//th'))
valeur_head=driver.find_elements(By.XPATH,'//table[@name="BookTable"]//th')
"""for h in range(1,len(valeur_head)+1):
    data_head = driver.find_element(By.XPATH, "//table[@name='BookTable']//th[" + str(h) + "]").text
    print(data_head)"""

time.sleep(4)
for r in range(2,nb_lignes+1):

    """for c in range(1,nb_colonnes+1):
        #data=driver.find_element(By.XPATH,'//table[@name="BookTable"]//tr["+str(r)+"]/td["+str(c)+"]').text
        #print(data)
        data1=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data1,end="       ")
    print()"""

#ici on veut chercher ce que l'auteur Amit a comme livre et c'est quoi le prix
auteur=driver.fin




driver.close()