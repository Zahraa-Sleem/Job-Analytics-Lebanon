import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json
#environment name is myenv currently.
#OPEN THE WEBSITE
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.jobsforlebanon.com/')
while True:
        try:
            newScan=driver.find_element(By.XPATH, '//*[@id="section-jobs-catalogue"]/div/div[2]/div/div/div[1]/a[2]') #locates the new scan button
            newScan.click()# clicks the new scan button
            break
        except:
            pass
while True:
        try:
            parent_element=driver.find_element(By.XPATH, '//*[@id="results"]/div[1]/div[2]')
            break
        except:
            pass
child_inner_html_list = []
child_elements = parent_element.find_elements(By.XPATH,"./*")
for child in child_elements:
    inner_html = child.get_attribute("innerHTML")
    child_inner_html_list.append(inner_html)
child_dict = {
    "children": child_inner_html_list
}
with open("child_elements.json", "w") as f:
    json.dump(child_dict, f, indent=2)   






