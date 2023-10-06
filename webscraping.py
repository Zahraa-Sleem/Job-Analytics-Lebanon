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
check=True
count=0
while check:
    while True:
        try:
            a_tag= driver.find_element(By.XPATH,"//a[text()='Load More Jobs']")
            a_tag.click()
            count+=1
            break
        except:
            try:
                more= driver.find_element(By.CLASS_NAME,"data-notfound")
                check=False
                break
            except:
                pass
child_inner_html_list = []
for j in range(2,count+2):
    while True:
        try:
            parent_element=driver.find_element(By.XPATH, f'//*[@id="results"]/div[1]/div[{j}]')
            break
        except:
            pass
    child_elements = parent_element.find_elements(By.XPATH,"./*")
    i=1
    for child in child_elements:
        try:
            element={ 
            "department":child.find_element(By.XPATH,f'//*[@id="results"]/div[1]/div[{j}]/div[{i}]/div/div[1]/span/span').get_attribute("innerHTML"),
            "location":child.find_element(By.XPATH,f'//*[@id="results"]/div[1]/div[{j}]/div[{i}]/div/div[2]/div/span/span').get_attribute("innerHTML"),
            "jobtitle":child.find_element(By.XPATH,f'//*[@id="results"]/div[1]/div[{j}]/div[{i}]/div/div[2]/a').get_attribute("innerHTML"),
            "time":child.find_element(By.XPATH,f'//*[@id="results"]/div[1]/div[{j}]/div[{i}]/div/div[3]/span[1]').get_attribute("innerHTML")
            }
            # print(element)
            child_inner_html_list.append(element)
            i=i+1
        except:
            pass

with open("objects.json", "w") as f:
    json.dump(child_inner_html_list, f, indent=2)   