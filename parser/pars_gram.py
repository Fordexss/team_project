import requests
from bs4 import BeautifulSoup
from aiogram import Dispatcher

additionally = {}

async def pars_gram(dp: Dispatcher):
    forA1 = ['Простий майбутній час', 'Простий минулий час', 'Простий теперішній час', 'Негативні речення', 'Види запитань', 'Певний артикль',
         'Невизначений артикль',  'Присвійні займенники', ]
    forA2 = ['Особисті займенники', 'Прикметник (Adjective)', 'Прислівник (Adverb)', 'Питальні займенники', 'Структура речення (Sentence Structure)',
            'Множина іменників', 'Умовні речення (Conditionals)', 'Умовні речення нульового типу', 'Присвійні займенники']
    forB1 = ['Теперішнй тривалий час', 'Теперішнй доконаний час', 'Минулий тривалий час', 'Нульовий артикль', 'Прийменники з іншими значеннями',
            'Прийменники після дієслів і прикметників (фіксовані прийменники)', 'Умовні речення другого типу', 'Умовні речення першого типу',
            'Дієслово (Verb)', 'Типи дієслів', 'Сполучники (Conjunctions)', 'Присвійний відмінок іменників']
    forB2 = ['Майбутній тривалий час', 'Майбутній доконаний час', 'Взаємні займенники', 'Невизначені займенники', 'Відносні займенники',
            'Вказівні займенники', 'Зворотні займенники', 'Категорія роду іменників', 'Місце прислівника в реченні', 'Ступені порівняння прислівників', 
            'Ступені порівняння прикметників', 'Порядок прикметників перед іменниками', 'Майбутній тривалий час', 'Майбутній доконаний час',
            'Минулий доконаний час', 'Модальні дієслова (Modal Verbs)']

    a1 = {}
    a2 = {}
    b1 = {}
    b2 = {}
    
    res = requests.get('https://teacheng.info/theory/grammar')
    soup =  BeautifulSoup(res.content, "html.parser")
    items = soup.find('div', class_ = 'post-content')
    for a in items.find_all('a'):
        if a.text in forA1:
            href = a.get("href")
            link = 'https://teacheng.info/' + href
            req = requests.get(link)
            new_soup = BeautifulSoup(req.content, "html.parser")
            theme = new_soup.find('h1', class_ = 'post-title')
            text = new_soup.find('div', class_ = 'post-content')
            a1[a.text] = {'text': text.text, 'theme': theme.text}
        
        elif a.text in forA2:
            href = a.get("href")
            link = 'https://teacheng.info/' + href
            req = requests.get(link)
            new_soup = BeautifulSoup(req.content, "html.parser")
            theme = new_soup.find('h1', class_ = 'post-title')
            text = new_soup.find('div', class_ = 'post-content')
            a2[a.text] = {'text': text.text, 'theme': theme.text}
        
        elif a.text in forB1:
            href = a.get("href")
            link = 'https://teacheng.info/' + href
            req = requests.get(link)
            new_soup = BeautifulSoup(req.content, "html.parser")
            theme = new_soup.find('h1', class_ = 'post-title')
            text = new_soup.find('div', class_ = 'post-content')
            b1[a.text] = {'text': text.text, 'theme': theme.text}
            
        elif a.text in forB2:
            href = a.get("href")
            link = 'https://teacheng.info/' + href
            req = requests.get(link)
            new_soup = BeautifulSoup(req.content, "html.parser")
            theme = new_soup.find('h1', class_ = 'post-title')
            text = new_soup.find('div', class_ = 'post-content')
            b2[a.text] = {'text': text.text, 'theme': theme.text}
        
        else:
            href = a.get("href")
            link = 'https://teacheng.info/' + href
            req = requests.get(link)
            new_soup = BeautifulSoup(req.content, "html.parser")
            theme = new_soup.find('h1', class_ = 'post-title')
            text = new_soup.find('div', class_ = 'post-content')
            additionally[a.text] = {'text': text.text, 'theme': theme.text}
        
    await dp.bot.send_message(text=a1["Присвійні займенники"]['text'], chat_id=1011382984, parse_mode="html")
        
