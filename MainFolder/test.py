# import requests
# from bs4 import BeautifulSoup as BS



# r = requests.get('https://matrx.herokuapp.com/db.html')
# html = BS(r.content, 'html.parser')

# for el in html.select('.user > .login'):
# 	print(el.get('id'))


# from recoder.cyrillic import Recoder
# rec = Recoder(depth=4)
# broken_text = u'''Îñíîâíàÿ Îëèìïèéñêàÿ äåðåâíÿ â'''
# # fixed_text = rec.fix_common(broken_text)
# print(rec.fix(broken_text))


import bencodepy


print(bencodepy.encode("Hello"))