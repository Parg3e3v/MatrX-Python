import requests
from bs4 import BeautifulSoup as BS



r = requests.get('https://matrx.herokuapp.com/db.html')
html = BS(r.content, 'html.parser')

for el in html.select('.user > .login'):
	print(el.get('id'))