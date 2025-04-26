import requests 
from bs4 import BeautifulSoup 
from win10toast import ToastNotifier 


n = ToastNotifier() 
def getdata(url): 
	
	r = requests.get(url) 
	
	return r.text

