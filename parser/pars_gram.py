import time
from selenium import webdriver
import os
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from constant import DB_FILE, DRIVER
from db_for_parsind import DbParsingInterface 
import requests
from bs4 import BeautifulSoup

forA1 = ['Простий майбутній час', 'Простий минулий час', 'Простий теперішній час', 'Негативні речення', 'Види запитань', 'Певний артикль',
         'Невизначений артикль',  'Присвійні займенники', 'Артикль (Artіcle)']
forA2 = ['Особисті займенники', 'Прикметник (Adjective)', 'Прислівник (Adverb)', 'Питальні займенники', 'Структура речення (Sentence Structure)',
            'Множина іменників', 'Умовні речення (Conditionals)', 'Умовні речення нульового типу', 'Присвійні займенники']
forB1 = ['Теперішнй тривалий час', 'Теперішнй доконаний час', 'Минулий тривалий час', 'Нульовий артикль', 'Прийменники з іншими значеннями',
            'Прийменники після дієслів і прикметників (фіксовані прийменники)', 'Умовні речення другого типу', 'Умовні речення першого типу',
            'Дієслово (Verb)', 'Типи дієслів', 'Сполучники (Conjunctions)', 'Присвійний відмінок іменників']
forB2 = ['Майбутній тривалий час', 'Майбутній доконаний час', 'Взаємні займенники', 'Невизначені займенники', 'Відносні займенники',
            'Вказівні займенники', 'Зворотні займенники', 'Категорія роду іменників', 'Місце прислівника в реченні', 'Ступені порівняння прислівників', 
            'Ступені порівняння прикметників', 'Порядок прикметників перед іменниками', 'Майбутній тривалий час', 'Майбутній доконаний час',
            'Минулий доконаний час', 'Модальні дієслова (Modal Verbs)']

s = Service(executable_path=DRIVER)
parse_db = DbParsingInterface(db_file_name=DB_FILE)

def pars_grammar():
    driver = webdriver.Edge(service=s)
    parse_db.open()
    parse_db.create_default_table_grammar()
    res = requests.get('https://teacheng.info/theory/grammar')
    soup =  BeautifulSoup(res.content, "html.parser")
    items = soup.find('div', class_ = 'post-content')
    url = 'https://www.youtube.com/results?search_query='
    for a in items.find_all('a'):
       
        href = a.get("href")
        link = 'https://teacheng.info/' + href
        req = requests.get(link)
        new_soup = BeautifulSoup(req.content, "html.parser")
        theme = new_soup.find('h1', class_ = 'post-title')
        text = new_soup.find('div', class_ = 'post-content')   
        print(a.text)
        try:
            search_querry = a.text + ' англійська мова'
            
            driver.get(url + search_querry.replace(' ', '+'))
            time.sleep(5)
            values = driver.find_elements(By.ID, 'video-title')
            try:
                    
                href = values[1].get_attribute('href')
                name = values[1].get_attribute('aria-label')
                print(search_querry)
                print(href)
                        
                values.clear()
            except Exception as ex:
                print(ex)
                            
        except Exception as ex:
            print(ex)
        if a.text in forA1:             
            parse_db.insert_into_grammar(level='A1', theme=theme.text, text=text.text, video=href)
        elif a.text in forA2:    
            parse_db.insert_into_grammar(level='A2', theme=theme.text, text=text.text, video=href)
        elif a.text in forB1:
            parse_db.insert_into_grammar(level='B1', theme=theme.text, text=text.text, video=href)
        elif a.text in forB2:   
            parse_db.insert_into_grammar(level='B2', theme=theme.text, text=text.text, video=href)
        else:
            parse_db.insert_into_grammar(level='additionally', theme=theme.text, text=text.text, video=href)
    parse_db.close()
    
pars_grammar()