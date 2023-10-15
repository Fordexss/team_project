import time
from selenium import webdriver
import os
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
<<<<<<< HEAD
from data.config import DRIVER, DB_FILE

import sqlite3

s = Service(executable_path=DRIVER)
=======
from data.config import DB_FILE
import sqlite3

s = Service(executable_path='C:\\Users\\HP\\Python_0\\team_project\\parser\\edge_driver\\msedgedriver.exe')
>>>>>>> origin/master

for_search = ['Простий майбутній час', 'Простий минулий час', 'Простий теперішній час', 'Негативні речення', 'Види запитань',
         'Невизначений артикль',  'Присвійні займенники', 'Особисті займенники', 'Прикметник (Adjective)', 'Прислівник (Adverb)', 'Питальні займенники', 'Структура речення (Sentence Structure)',
         'Множина іменників', 'Умовні речення (Conditionals)', 'Умовні речення нульового типу', 'Присвійні займенники', 'Теперішнй тривалий час', 'Теперішнй доконаний час', 'Минулий тривалий час', 'Нульовий артикль', 'Прийменники з іншими значеннями',
         'Прийменники після дієслів і прикметників (фіксовані прийменники)', 'Умовні речення другого типу', 'Умовні речення першого типу',
         'Дієслово (Verb)', 'Типи дієслів', 'Сполучники (Conjunctions)', 'Присвійний відмінок іменників', 'Майбутній тривалий час', 'Майбутній доконаний час', 'Взаємні займенники', 'Невизначені займенники', 'Відносні займенники',
         'Вказівні займенники', 'Зворотні займенники', 'Категорія роду іменників', 'Місце прислівника в реченні', 'Ступені порівняння прислівників', 
         'Ступені порівняння прикметників', 'Порядок прикметників перед іменниками', 'Майбутній тривалий час', 'Майбутній доконаний час',
         'Минулий доконаний час', 'Модальні дієслова (Modal Verbs)']

conn = sqlite3.connect(DB_FILE)
cr = conn.cursor()

def pars_video():
    edge_options = Options()
    edge_options.use_chromium = True  
    edge_options.add_argument("--headless")
    driver = webdriver.Edge(service=s, options=edge_options)
    link = 'https://www.youtube.com/results?search_query='
    try:
        
        for search_querry in for_search:
            driver.get(link + search_querry.replace(' ', '+'))
            time.sleep(5)
            values = driver.find_elements(By.ID, 'video-title')
            try:
                
                href = values[1].get_attribute('href')
                name = values[1].get_attribute('aria-label')
                
                cr.execute("""UPDATE grammar SET video = ? WHERE theme = ?""", (href, search_querry, ))
            except Exception as ex:
                print(ex)
                
            values.clear()
            
            
    except Exception as ex:
        print(ex)
        
    finally:
        driver.close()
        driver.quit()

    cr.execute("SELECT * FROM grammar WHERE video NOT NULL")
    res = cr.fetchone()
    print(len(res))
    conn.close()
<<<<<<< HEAD
=======
    
>>>>>>> origin/master
