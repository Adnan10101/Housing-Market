import requests
import csv
import numpy as np

from bs4 import BeautifulSoup




with open("house_details.csv","w") as file:
    w = csv.writer(file)
    w.writerow(["Price","Area","Bedrooms","Bathrooms","Location","Builder","Status"])

def scrapper(names):

    for name in names:
        
        for i in range(1,6):
            #print(name)
            #print(i)
            page = name+"&page={}".format(i)
            request = requests.get(page)
            soup = BeautifulSoup(request.content,"html.parser")
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
                    bed = bed_div.find("span",class_ = "val")
                    if bed:
                        bed = bed.text
                    else:
                        bed = np.nan
                    
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


    
def get_url(link):
    request = requests.get(link)
    main_url = "https://www.makaan.com"
    
    soup = BeautifulSoup(request.text,"html.parser")
    all_urls = []
    bb = soup.find("div",class_ = "tbl-wrap") 
    
    for url in bb.find_all("tr", itemtype = "http://schema.org/Place"):
        get_url = url.find_all(attrs = {"data-url":True})
        if get_url:
            get_url = main_url + get_url[0]["data-url"]
            all_urls .append(get_url)
    
    return all_urls


source = "https://www.makaan.com/price-trends/property-rates-for-buy-in-chennai"

urls = get_url(source)
scrapper(urls)














        

    
    








