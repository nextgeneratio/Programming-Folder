import requests 
from bs4 import BeautifulSoup 
from win10toast import ToastNotifier 


n = ToastNotifier() 
def getdata(url): 
	
	r = requests.get(url) 
	
	return r.text
htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/") 

soup = BeautifulSoup(htmldata, 'html.parser') 

print(soup.prettify()) 

