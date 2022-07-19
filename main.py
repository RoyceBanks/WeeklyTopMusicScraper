from bs4 import BeautifulSoup                                                   
import requests                                                             #REQUIREMENTS
import re                                                                       

url = "https://www.americantop40.com/music/top-songs/"                      #Websites 1 URL 
url_3 = "https://top40weekly.com/"                                          #Websites 3 URL

print("--------------AmericanTop40.com--------------\n")                    #Draws Boarder
results = requests.get(url)                                                 #Goes to URL 1
page = BeautifulSoup(results.text, "html.parser")                           #Converts HTML to TEXT
charts = page.find_all("span")[2:]                                          #Grabs All <span> HTML tags
charts = (str(charts).replace("<span>","").replace("</span>","")[1:-1])     #Removes HTML tags and unwated char and turns into STR
li = list(charts.split(", "))                                               #Converts STR into LIST seperated by ,

for names in li:                                                            #Goes thur LIST
    name = str(names)                                                       #Makes LIST a STR
    print(name)                                                             #Prints 
 

print("------------Top40.com------------- \n")                              #Draws Boarder
    
results_3 = requests.get(url_3)                                             #Goes to URL 3
page_3 = BeautifulSoup(results_3.text, "html.parser")                       #Converts HTML to TEXT
chart_3 = page_3.find_all("p")                                              #Grabs All <p> HTML tags
parent_3 = chart_3[3].parent                                                
ptags = str(parent_3.find_all("p")).replace("[","").replace("]", "")        #Converts List into STR
cleanlist = ptags.replace("<p>", "").replace("<br/>", "").replace("</p>", "") #Removes unwanted char
top40 = cleanlist                                                           #Useless Rename

print(top40)                                                                #Prints
