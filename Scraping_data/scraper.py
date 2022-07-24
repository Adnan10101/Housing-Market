import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
import csv
import numpy as np
import re




with open("house_details.csv","w") as file:
    w = csv.writer(file)
    w.writerow(["Price","Area","Bedrooms","Bathrooms","Location","Builder","Status"])

def scrapper(names):

    for name in names:
       

        for i in range(1,6):
            print(name)
            print(i)
            page = name+"&page={}".format(i)
            request = requests.get(page)
            soup = BeautifulSoup(request.content,"lxml")
            with open("house_details.csv","a") as file:
                w = csv.writer(file)
                
                for head in soup.find_all("li",class_ = "cardholder"):
                    tr_class = head.find_all("tr",class_ = "hcol")
                    price_td_class = tr_class[0].find("td",class_ = "price")
                    price = price_td_class.find("span", class_ = "val").text
                    price_unit = price_td_class.find("span",class_ = "unit").text
                    tot_price = str(price) + price_unit
                    
                    area_td_class = tr_class[1].find("td", class_ ="size")
                    area = area_td_class.find("span",class_ = "val").text
                    
                    bed_div = head.find("div",class_ = "title-line")
                    bed = bed_div.find("span",class_ = "val").text
                    
                    bath_ul = head.find("ul",class_ = "listing-details")
                    bath = bath_ul.find("li",title = "Bathrooms")
                    if bath:
                        bath = bath.text
                    else:
                        bath = np.nan
                        
                    location = head.find("span",itemprop = "addressLocality").text
                    builder = bed_div.find("a",class_ = "projName")
                    if builder:
                        builder = builder.text
                    else:
                        builder = np.nan
                        
                    status_tr = head.find("tr",class_ = "hcol w44")
                    status = status_tr.find("td",class_ = "val").text
                    
                    w.writerow([tot_price,area,bed,bath,location,builder,status])

def get_url(source):
    url = re.findall('https://www.makaan.com/price-trends/property-rates-for-buy-in-chennai')
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        print(link.get('href'))

    


source = "https://www.makaan.com/price-trends/property-rates-for-buy-in-chennai"


# Selenium driver

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome("D:/chromedriver.exe",chrome_options=opts)


locations_name = ["https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50420&localityName=avadi&suburbId=10015&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50307&localityName=sholinganallur&suburbId=10257&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51578&localityName=perungalathur&suburbId=10263&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50288&localityName=medavakkam&suburbId=10257&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51578&localityName=perungalathur&suburbId=10263&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51578&localityName=perungalathur&suburbId=10263&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50346&localityName=porur&suburbId=10015&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50403&localityName=kelambakkam&suburbId=10257&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51276&localityName=chengalpattu&suburbId=10263&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50300&localityName=poonamallee&suburbId=10015&listingType=buy&propertyType=apartment"
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50314&localityName=mogappair&suburbId=10015&listingType=buy&propertyType=apartment"

"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=52047&localityName=selaiyur&suburbId=10016&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51142&localityName=madipakkam&suburbId=10257&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50352&localityName=navallur&suburbId=10257&suburbName=omr&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50315&localityName=kolathur&suburbId=10013&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50312&localityName=urapakkam&suburbId=10263&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51076&localityName=ambattur&suburbId=10015&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51627&localityName=perungudi&suburbId=10257&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51532&localityName=siruseri&suburbId=10257&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50349&localityName=pallavaram&suburbId=10263&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51229&localityName=west-tambaram&suburbId=10263&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=52316&localityName=padur&suburbId=10257&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50306&localityName=velachery&suburbId=10257&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51151&localityName=perumbakkam&suburbId=10016&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50286&localityName=chromepet&suburbId=10263&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=50310&localityName=pallikaranai&suburbId=10257&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=52276&localityName=neelankarai&suburbId=10259&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51668&localityName=madambakkam&suburbId=10257&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51571&localityName=singaperumal-koil&suburbId=10263&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51280&localityName=thoraipakkam-omr&suburbId=10257&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51618&localityName=t-nagar&suburbId=10202&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51697&localityName=choolaimedu&suburbId=10202&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=51248&localityName=adyar&suburbId=10202&listingType=buy&propertyType=apartment",
"https://www.makaan.com/listings?cityId=5&cityName=chennai&localityId=52056&localityName=karapakkam&suburbId=10257&listingType=buy&propertyType=apartment"







]
scrapper(locations_name)










        

    
    








