from lib2to3.pgen2 import driver
import time 
import selenium
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import os
import pandas
from time import sleep as s
def tewtter():
    driver_location="F:\\seli\\driver\\chromedriver.exe" # chrome driver location in my device
    os.environ["wd.chrome.driver"]=driver_location
    driver=wd.Chrome(driver_location)
    driver.delete_all_cookies()
    driver.get("https://twitter.com/sachin_rt")
    s(10)
    name=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span[1]/span').text
    dateOfJoin=driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[4]/div/span[3]/span').text
    folloing=driver.find_element(By.XPATH ,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[1]/a/span[1]/span').text
    followers=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div/div/div[5]/div[2]/a/span[1]/span').text
    print("name= ",name)
    print("date of join is : ",dateOfJoin)
    print("following :",folloing)
    print("followers: ",followers)
    driver.close()

tewtter()