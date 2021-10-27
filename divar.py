from bs4 import BeautifulSoup
import requests
import time

oldapartment=" "
base_url="https://divar.ir/s/tehran/buy-apartment"
pre_href_url="https://divar.ir"

def load():
	page = requests.get(base_url)
	soup = BeautifulSoup(page.content, 'html.parser')
	return soup.find_all(class_="post-card-item kt-col-6 kt-col-xxl-4")

def checklink(link):
	print('href: ', link['href'])
	request_href = requests.get(pre_href_url + link['href'])
	soup = BeautifulSoup(request_href.content, 'html.parser')
	tell = soup.find(class_="kt-button kt-button--primary post-actions__get-contact")
	print(tell.prettify())
	return

while True:

	for newapartment in load():
		if  'اندیشه' in newapartment.get_text():
			if oldapartment!=newapartment.get_text():
				print(newapartment.get_text())
				link=newapartment.find('a', class_ = 'kt-post-card kt-post-card--outlined', href = True)
				if link:
					checklink(link)
				oldapartment=newapartment.get_text()
	time.sleep(3)
