from selenium import webdriver
import os
from time import sleep as s
from selenium.webdriver.common.by import By as by
import pandas as pd

dl=r"C:\Users\narpa\OneDrive\Desktop\rupesh\chromedriver.exe"
#os.enve["webdriver.chrome.driver"]=dl
d=webdriver.Chrome(dl)
l=[]
names=[]
cgpa=[]
rl=[]
pf=[]
for i in range(1,55):
    if (i<10):
        l.append("19F61A060"+str(i))
    else:
        l.append("19F61A06"+str(i))
l.remove("19F61A0616")
l.remove("19F61A0625")

s(1)
for i in l :
   # if(i!="19F61A0625"):
    d.get("http://siddharthgroup.ac.in/aut4btech1r19nov2022.php?dbn=aut4btech1r19nov2022")
    d.find_element(by.XPATH,"/html/body/main/section/form/center/table/tbody/tr[1]/td[2]/input").send_keys(i)
    print (i)
    d.find_element(by.XPATH,"/html/body/main/section/form/center/table/tbody/tr[3]/td[2]/input").click()
    print("successfull")
    name=d.find_element(by.XPATH,"/html/body/main/section/center[2]/div/b/font[2]").text
    print("name",name)
    names.append(name)
    p=d.find_element(by.XPATH,"/html/body/main/section/span").text
    print("percentage",p)
    cgpa.append(p)
    rl.append(i)
    if(p[6:0]=="0 C"):
        pf.append("fail")
        print("inside if")
    else:
        pf.append("pass")
        print("inside else")

results={"Name":names,"rollno":rl,"cgpa & sgpa":cgpa,"status":pf}
new=pd.DataFrame(results)
new.to_html(r"C:\Users\narpa\OneDrive\Desktop\rupesh\r2.html")
print (results)