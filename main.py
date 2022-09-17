
import os
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
## agregue este comentario

import time

def launchBrowser():
    edge_options = Options()
    edge_options.add_experimental_option("detach", True)
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(options=edge_options)
    driver.get('https://www.youtube.com')
    time.sleep(10)
    Element_loggin= driver.find_elements(By.ID, "content")[0]
    print(Element_loggin.tag_name)
    
    driver.implicitly_wait(5)
    Element_loggin.click()
    time.sleep(5)
    try:
        Element_add=WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="skip-button:p"]/span/button')))# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id="skip-button:p"]/span/button"))
        Element_add.clic()
    except:
        pass

   
    try:
        Element_add2=WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="skip-button:p"]/span/button')))# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id="skip-button:p"]/span/button"))
        Element_add2.clic()
    except:
        pass
    
    Element_mute = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[28]/div[2]/div[1]/span/button')
    Element_mute.click()
    time.sleep(5)
    time.sleep(15)
    driver.back()

    while(True):
        pass
    
    
def closeBrowser():
    pass

launchBrowser()

# def launchBrowser():
#     #user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/105.0.0.0'
# # os.environ['PATH'] += os.pathsep + "C:/SeleniumDrivers"
#     edge_driver_path= os.path.join(os.getcwd(), 'msedgedriver.exe')
#     edge_service = Service(edge_driver_path)
#     edge_options= Options()
#     #edge_options.add_argument(f'user-agent={user_agent}')
#     browser = webdriver.Edge(service= edge_service, options=edge_options)
#     edge_options.add_experimental_option("detach", True)
#     browser.get("http://www.google.com/")
#     return browser
# Edge= launchBrowser()
