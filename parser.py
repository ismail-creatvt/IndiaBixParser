import requests
from bs4 import BeautifulSoup
from styles import document
from components import *

result = requests.get("https://developer.android.com/guide/components/fundamentals")
# result = requests.get('https://developer.android.com/training/basics/firstapp/creating-project')
page_content = result.content.decode('utf-8')

home = BeautifulSoup(page_content)

# page_links = []
#
# list = home.findAll('ul', attrs={'class': 'devsite-nav-list', 'menu':'_book'})[0]
# ul = list.findAll('li', attrs={'class': 'devsite-nav-item'})

# for a in ul:
#     for c in a.contents:
#         if c.name == 'a':
#             link = c['href']
#             if link[0] == '/':
#                 page_links.append('https://developer.android.com' + link)
#             else:
#                 page_links.append(link)


def parse_page_content(pcontent):
    soup = BeautifulSoup(pcontent)

    try:
        title = soup.findAll('h1', attrs={'class': 'devsite-page-title'})[0].text

        body = soup.findAll('div', attrs={'class': 'devsite-article-body'})[0]
    except IndexError:
        return

    elements = []
    for element in body.findAll(['p', 'ul', 'ol', 'img', 'devsite-heading', 'pre', 'h1', 'h2', 'h3', 'dd', 'dl'], recursive=False):
        if element.name == 'devsite-heading':
            print('devsite-heading' + str(element))
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
        elif el.name == 'pre':
            devsite_code(document, el)
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
        elif el.name == 'ol':
            ordered_list(document, el)
        elif el.name == 'img':
            img(document, el['src'])


parse_page_content(page_content)

# count = 0
# for link in page_links:
#     page_content = requests.get(link).content.decode('utf-8')
#     print('link:' + link.replace('https://developer.android.com', ''))
#     parse_page_content(page_content)
#     count += 1
#     print('-------------parse ended ' + str(count) + '---------------------------------')
#     if count > 20:
#         break

document.save('android.docx')
