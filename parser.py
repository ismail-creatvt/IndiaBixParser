import requests
from bs4 import BeautifulSoup
from styles import document
from components import *

result = requests.get("https://developer.android.com/guide/components/fundamentals")

page_content = result.content.decode('utf-8')

soup = BeautifulSoup(page_content, features='lxml')

title = soup.findAll('h1', attrs={'class': 'devsite-page-title'})[0].text

body = soup.findAll('div', attrs={'class': 'devsite-article-body'})[0]

elements = []
for element in body.findAll(['p', 'ul', 'devsite-heading', 'dd', 'dl'], recursive=False):
    if element.name == 'devsite-heading':
        elements.append(element.contents[0])
    else:
        elements.append(element)

h1(document, title)

for el in elements:
    if el.name == 'p':
        if el.has_attr('class'):
            if el['class'][0] == 'caution':
                caution(document, el)
            elif el['class'][0] == 'note':
                note(document, el)
        else:
            paragraph(document, el)
    elif el.name == 'dl':
        data_dictionary(document, el)
    elif el.name == 'h2':
        h2(document, el.text)
    elif el.name == 'h3':
        h3(document, el.text)
    elif el.name == 'h1':
        h1(document, el.text)
    elif el.name == 'ul':
        unordered_list(document, el)

document.save('android.docx')
