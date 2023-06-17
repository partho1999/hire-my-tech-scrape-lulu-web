from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time


browser = webdriver.Firefox()

browser.get('https://www.luluhypermarket.com/en-ae/department-store-electronics-tv/c/HY00214796')
soup=BeautifulSoup(browser.page_source,"html.parser")

yCmsComponent=soup.find("div", {"class": "row product-listing-sectionfashion-products"})
#print(yCmsComponent)


#Product-links
p_links=[]
for l in yCmsComponent.find_all("a"):
    #print(l.get('href'))
    p_links.append("https://www.luluhypermarket.com"+l.get('href'))

    

p_name=[]
for pn in yCmsComponent.find_all("h3"):
    #print(pn.text)
    p_name.append(pn.text.replace("\n", ""))



dict3 = {'Product-Name': p_name, 'Product-links':p_links} 
    
df3 = pd.DataFrame(dict3)
timestr = time.strftime("%Y%m%d-%H%M%S")    
df3.to_csv("products"+"-"+timestr+".csv")


for link in p_links:

    browser = webdriver.Firefox()
    browser.get(link)
    soup=BeautifulSoup(browser.page_source,"html.parser")

    #product-description
    p_desc=soup.find("div", {"class": "product-description"})
    #print(p_desc)

    p_nam=[]
    product_name=soup.find("h1", {"class": "product-name"})
    print(product_name.text)
    p_nam.append(product_name.text)

    n_o_r=[]
    num_of_reviews= soup.find("div", {"class": "col-lg-auto reviews-count"})
    if num_of_reviews is None:
        n_o_r.append('no-reviews')
    else:
        print(num_of_reviews.text)
        n_o_r.append(num_of_reviews.text)

    price_tag_detail= soup.find("div", {"class": "price-tag detail"})
    #print(price_tag_detail)
    if price_tag_detail is None:
        pass
    #off price
    o_p=[]
    off_price= soup.find("span", {"class": "off"})
    if off_price is None:
        o_p.append('no-off-price')
    else:
        print('off-price:',off_price.text)
        o_p.append(off_price.text)

    #current-price
    c_p=[]
    current_price= soup.find("span", {"class": "item price"})
    print('current-price:',current_price.text.replace("\n",""))
    c_p.append(current_price.text.replace("\n",""))

    #item-off-percent
    i_o_p=[]
    item_off_percent= soup.find("span", {"class": "item off-percent"})
    if item_off_percent is None:
        i_o_p.append('no-off')
    else:
        print('item-off-percent:',item_off_percent.text)
        i_o_p.append(item_off_percent.text.replace("\n",""))

    #warranty
    warr=soup.find("div", {"class": "row tax-instituion tooltipwarranty badgeenglishae"})
    if warr is None:
        pass
    else:
        war=[]
        for warranty in soup.find("div", {"class": "row tax-instituion tooltipwarranty badgeenglishae"}):
            #print('warranty:',warranty.text)
            war.append(warranty.text.replace("\n",""))

        print('warranty:',war[0])
    

    dict5 = {'Product-Name': p_nam, 'Number-of-reviews':n_o_r, 'Off-price':o_p, 'Current-price':c_p, 'Item-off-percent':i_o_p, 'warranty':war[0]} 
        
    df5 = pd.DataFrame(dict5)
    timestr = time.strftime("%Y%m%d-%H%M%S")    
    df5.to_csv("product_details"+"-"+timestr+".csv")
    

    product_imgs=soup.find("div", {"class": "thumbnail-wrapper owl-carousel owl-theme product-detail-carousel owl-loaded"})
    #print(product_imgs)

    #img
    imgs=[]
    for img in product_imgs.find_all('img') :  
        #print(img.get('src'))
        imgs.append(img.get('src'))

    df6 = pd.DataFrame(imgs,  columns =['Product_img_links'])
    timestr = time.strftime("%Y%m%d-%H%M%S")
    df6.to_csv('Product_img_links'+'-'+timestr+'.csv')
    