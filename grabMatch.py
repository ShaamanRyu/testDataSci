import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup


URL = 'https://www.uefa.com/uefaeuro-2020/fixtures-results/'
page = requests.get(URL)

round="MD1"
#"MD2"
#"MD3"
#"r16"
#"qf"
#"sf"
#"final"

soup = BeautifulSoup(page.content, 'html.parser')
r16_results = soup.find_all('a')
for result in r16_results:
	#print(result.get('data-label')
	if(result.get('data-label')==round):
		#print(result.get('data-round'))
		newURL = URL + "#/rd/" + result.get('data-round')

requests = HTMLSession()
page=requests.get(newURL)
page.html.render()
newsoup = BeautifulSoup(page.html.html, 'html.parser')
match_results = newsoup.find_all('a','match-row_link')
for resulta in match_results:
	print(resulta.get('href'))
	
