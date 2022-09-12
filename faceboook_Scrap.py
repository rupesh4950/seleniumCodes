from lib2to3.pgen2 import driver
import selenium
from selenium import webdriver as wd
from selenium.webdriver.common.by import By 
import os 
from time import sleep as s

def  FbScrap():
    dl="F:\\seli\\driver\\chromedriver.exe" # chrome driver location in my device
    os.environ["webdriver.chrome.driver"]=dl
    driver=wd.Chrome(dl)
    driver.delete_all_cookies
    driver.get("https://www.facebook.com/SachinTendulkar")
    s(10)
    name=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div/div/span/div/h1').text
    followers=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a[1]').text
    following=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a[2]').text
    print("name : ",name)
    print("followers : ",followers)
    print("following : ",following)
    driver.quit
FbScrap()