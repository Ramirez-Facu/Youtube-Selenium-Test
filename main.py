
import os
from tkinter import E
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def skip_if_add(driver):
    try:
        wait = WebDriverWait(driver, 20*60)
        element = wait.until(EC.element_to_be_clickable(driver.find_element(By.CLASS_NAME, "ytp-ad-skip-button-container")))
        element.click()
        print("1")
    except:
        
        pass

def check_vid(driver):
    Element_Content= driver.find_elements(By.ID, "content")[0]
    Element_Content.click()

def check_login(driver):
    driver.find_element(By.XPATH, '//*[@id="buttons"]/ytd-button-renderer').click()
    driver.implicitly_wait(5)
    time.sleep(2)
    driver.back()

def check_volume_mute(driver):
    Element_mute=driver.find_element(By.CLASS_NAME, 'ytp-volume-area')
    Element_mute.click()

def launchBrowser():
    edge_options = Options()
    edge_options.add_experimental_option("detach", True)
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(options=edge_options)
    driver.get('https://www.youtube.com')
    time.sleep(10)
    
    driver.implicitly_wait(5)
    check_login(driver)
    time.sleep(5)
    driver.implicitly_wait(5)
    check_vid(driver)
    skip_if_add(driver)
    skip_if_add(driver)
    driver.implicitly_wait(5)   
    check_volume_mute(driver)
    time.sleep(15)
    driver.back()
    driver.close()
    while(True):
        pass
    
launchBrowser()
