from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time

driver=webdriver.Firefox()
driver.get('https://www.google.com/')

firstElement=driver.find_element('xpath','/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
firstElement.click()
firstElement.send_keys('IMDB')

time.sleep(1)
firstElement.send_keys(Keys.ENTER)
time.sleep(1)
WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[7]/div/div[7]/div[1]/div/div/div[2]/div/a[3]'))).click()
time.sleep(1)
WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.LINK_TEXT,'Top 250 Movies'))).click()

pageSource=driver.page_source
soup=BeautifulSoup(pageSource,'html')

with open('data.txt','w') as f:
    for cup in soup.find_all('td',attrs={'class':'titleColumn'}):
        f.write(cup.get_text()+'\n')
        
time.sleep(1)
driver.close()