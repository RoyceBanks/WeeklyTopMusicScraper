from bs4 import BeautifulSoup                         ### 
import requests                                  REQUIREMENTS
import re                                            ###

url = "https://www.americantop40.com/music/top-songs/"
url_3 = "https://top40weekly.com/"      

print("--------------AmericanTop40.com--------------\n")
results = requests.get(url)
page = BeautifulSoup(results.text, "html.parser")
charts = page.find_all("span")[2:]
charts = (str(charts).replace("<span>","").replace("</span>","")[1:-1])
li = list(charts.split(", "))

for names in li:  
    name = str(names)
    print(name)
 

print("------------Top40.com------------- \n")

results_3 = requests.get(url_3)
page_3 = BeautifulSoup(results_3.text, "html.parser")
chart_3 = page_3.find_all("p")
parent_3 = chart_3[3].parent
ptags = str(parent_3.find_all("p")).replace("[","").replace("]", "")
cleanlist = ptags.replace("<p>", "").replace("<br/>", "").replace("</p>", "" )
top40 = cleanlist

print(top40)
