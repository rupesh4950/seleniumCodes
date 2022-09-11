import os
import selenium
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from time import sleep as sp
import pandas as pd
def scrap():
    dl="F:\\seli\\driver\\chromedriver.exe" # its better to store the driver path in a separate variable
    os.environ["wd.chrome.driver"]=dl #creating the environmental variable int to run the driver
    driver=wd.Chrome(dl) #using the built in function of chrome driver to run the driver
    driver.delete_all_cookies
    # to create a list of rool no
    l=[] # to store roll numbers
    d=[] # to store cgpa and sgpa
    names=[]#to store name
    pf=[]#to store pass or fail
    c=0#to count the pass members
    for i in range(1,10):
        l.append("19F61A060"+str(i))
    for i in range(10,56):
        l.append("19F61A06"+str(i))
    l.remove("19F61A0616")#to remove the roll no 16 its not presented

    for i in l:
        driver.delete_all_cookies
        driver.get('http://siddharthgroup.ac.in/aut3btech2r19sep2022.php?dbn=aut3btech2r19sep2022')#to open the browser in the link
        sp(1)
        idno=i
        #now onward it should be in the loop
        driver.find_element(By.XPATH,'/html/body/main/section/form/center/table/tbody/tr[1]/td[2]/input').send_keys(idno)#to fill the rool no in the box
        sp(1)
        driver.find_element(By.XPATH,'/html/body/main/section/form/center/table/tbody/tr[3]/td[2]/input').click()#to click the submit butten
        sp(1)
        gpa=driver.find_element(By.XPATH,'/html/body/main/section/span').text #to scrap the data
        name=driver.find_element(By.XPATH,'/html/body/main/section/center[2]/div/b/font[2]').text
        d.append(gpa)
        names.append(name)
        if(gpa[6:9]=="0 C"):
            pf.append("fail")
        else:
            pf.append("pass")
            c=c+1
    names.append("total pass")
    l.append(" ")
    d.append(" ")
    pf.append(c)
    result={"NAME" :names, "Roll NO ":l,"CGPA AND SGPA":d,"result":pf}
    resu=pd.DataFrame(result)
    resu.to_html("F:\seli\output\CSIT3-2result.html")
    print(result)

scrap()#to call the scrap function

