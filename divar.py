from bs4 import BeautifulSoup
import requests
page = requests.get("https://divar.ir/s/tehran/buy-apartment")
soup = BeautifulSoup(page.content, 'html.parser')
home_items = soup.find_all(class_="post-card-item kt-col-6 kt-col-xxl-4")
for apartment in home_items:
	if  'پونک' in apartment.get_text():
		print(apartment.get_text())
