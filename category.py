from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

browser = webdriver.Firefox()

browser.get('https://www.luluhypermarket.com/en-ae/electronics')
soup=BeautifulSoup(browser.page_source,"html.parser")
#print(soup)

nav_inner = soup.find("div", {"class": "main-nav-inner"})
catagory=nav_inner.find_all('li', {'class': 'first-level with-dropdown'})
#print(catagory)
cate=[]
cat_link=[]
for cat in catagory:
    #print("item:",cat.select_one("a").text)
    c=cat.select_one("a").text
    cate.append(c)

    #print(cat.select_one("a").get('href'))
    cat_link.append("https://www.luluhypermarket.com"+cat.select_one("a").get('href'))
    

dict1 = {'Category': cate, 'category_link':cat_link} 
    
df1 = pd.DataFrame(dict1)
timestr = time.strftime("%Y%m%d-%H%M%S")    
df1.to_csv("category"+"-"+timestr+".csv")


## sub-category
section_container=soup.find("div", {"class": "section-container recommended-content"})
#print(section_container)



# link
links=[]
for link in section_container.find_all("a"):
    #print(link.get('href'))
    links.append(link.get('href'))

#img
imgs=[]
for img in section_container.find_all('img') :  
    #print(img.get('src'))
    imgs.append(img.get('src'))

#caption
caps=[]
for cap in section_container.find_all('div', class_='img-caption'):
    #print(cap.text)
    caps.append(cap.text)



dict2 = {'Sub-Category': caps, 'Images_link':imgs, 'Sub-category_urls':links} 
    
df2 = pd.DataFrame(dict2)
timestr = time.strftime("%Y%m%d-%H%M%S")    
df2.to_csv("sub-category"+"-"+timestr+".csv")



