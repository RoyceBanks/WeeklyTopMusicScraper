from bs4 import BeautifulSoup
import requests
import re

url = "https://www.americantop40.com/music/top-songs/"
url_2 = "https://www.billboard.com/charts/hot-100/"
url_3 = "https://top40weekly.com/"

results = requests.get(url)
page = BeautifulSoup(results.text, "html.parser")
chart = page.find_all("span")
for names in chart:
    names = str(names).split(">")[1].split("<")[0]
    name = names
    #print(names)
    
#span = chart.find_all("span")
#parent = span[1].parent
#print(chart)


print("------------Top40.com------------- \n")

results_3 = requests.get(url_3)
page_3 = BeautifulSoup(results_3.text, "html.parser")
chart_3 = page_3.find_all("p")
parent_3 = chart_3[3].parent
ptags = str(parent_3.find_all("p")).replace("[","").replace("]", "")
cleanlist = ptags.replace("<p>", "").replace("<br/>", "").replace("</p>", "" )
top40 = cleanlist

print(top40)