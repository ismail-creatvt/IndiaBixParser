from sqlite3 import ProgrammingError

import requests
from bs4 import BeautifulSoup

from db import create_connection, insert_question

conn = create_connection(r"./indiabix.db")

result = requests.get("https://www.indiabix.com/")
page_content = result.content.decode('utf-8')

home = BeautifulSoup(page_content, 'lxml')
page_links = []

question_list = home.findAll('ul', attrs={'class': 'ques-ans'})

for item in question_list:
    ul = item.findAll('li')
    for a in ul:
        for c in a.contents:
            if c.name == 'a':
                link = c['href']
                if link[0] == '/':
                    page_links.append('https://www.indiabix.com/' + link)
                else:
                    page_links.append(link)


def parse_page_content(p_content):
    soup = BeautifulSoup(p_content, 'lxml')

    div = soup.findAll('div', attrs={'class': 'div-topics-index'})
    p_links = []

    question_containers = soup.findAll('div', attrs={'class': 'bix-div-container'})
    for container in question_containers:
        question = container.findAll('td', attrs={'class': 'bix-td-qtxt'})[0]
        options = container.findAll('td', attrs={'class': 'bix-td-option'},  id=lambda x: x and x.startswith('tdOptionDt'))
        option_texts = []
        for o in options:
            option_texts.append(o.text)
        if len(option_texts) < 5:
            for i in range(0, 5-len(option_texts)):
                option_texts.append(None)

        correct_option = container.findAll('div', attrs={'class': 'bix-div-answer'})[0].text
        answer = correct_option.split('Explanation:')[0].replace('Answer: Option ', '')
        explanation = correct_option.split('Explanation:')[1].replace('Let us discuss.','')
        fields = (question.text, *option_texts, answer, explanation)
        try:
            insert_question(conn, fields)
        except ProgrammingError:
            print("Sqlite Error" + " Question texts : " + str(len(option_texts)))

    for d in div:
        for element in d.findAll('li'):
            for con in element.contents:
                if con.name == 'a':
                    li = con['href']
                    if li[0] == '/':
                        p_links.append('http://www.indiabix.com' + li)

    for pl in p_links:
        pg_content = requests.get(pl).content.decode('utf-8')
        parse_page_content(pg_content)
        print('link inside link : ' + pl)


for link in page_links:
    page_content = requests.get(link).content.decode('utf-8')
    print('link:' + link.replace('https://www.indiabix.com/', ''))
    try:
        parse_page_content(page_content)
    except UnicodeDecodeError:
        print("Exception")

conn.close()
