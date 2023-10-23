from constant import DB_FILE, DRIVER
from db_for_parsind import DbParsingInterface 
import requests
from bs4 import BeautifulSoup

forA1 = ['Меблі та господарські приладдя', 'Одяг та особисті речі', 'Кольори', 'Числа']
forA2 = ['Телефон', 'Як описати людину', 'Подорожування', 'Їжа', 'В ресторані', 'Гід по меню', 'Їжа та напої']
forB1 = ['Дні тижня', 'Місяці й пори року', 'Свята та фестивалі', 'Комп\'ютери та Інтернет', 'Академічні предмети', 'Освіта',
            'Сфери діяльності', 'Професії', 'Зайнятість', 'Спорт та ігри', 'Подорожування водним транспортом', 'Подорожування літаком',
            'Подорожування автобусом та поїздом', 'Автомобілі', 'Погода', 'Тіло людини']
forB2 = ['Телефон', 'Музичні інструменти', 'Покупки', 'У місті', 'Прохолоджувальні напої', 'Алкоголь', 'Частини машини', 'Погода',
            'Родина', 'Континенти та регіони світу', 'Грошові одиниці', 'Мови', 'Господарські товари', 'Меблі та господарські приладдя', 'Тварини']
   
parse_db = DbParsingInterface(db_file_name=DB_FILE)

def pars_lexic():  
    parse_db.open()
    parse_db.create_default_table_lexic()
    link='https://uk.speaklanguages.com/%D0%B0%D0%BD%D0%B3%D0%BB%D1%96%D0%B9%D1%81%D1%8C%D0%BA%D0%B0/%D0%BB%D0%B5%D0%BA%D1%81%D0%B8%D0%BA%D0%B0/#:~:text=%D0%90%D0%BD%D0%B3%D0%BB%D1%96%D0%B9%D1%81%D1%8C%D0%BA%D0%B0%20%D0%BB%D0%B5%D0%BA%D1%81%D0%B8%D0%BA%D0%B0%2C%20%D1%80%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D0%B5%D0%BD%D0%B0%20%D0%BD%D0%B0%2065%20%D1%89%D0%BE%D0%B4%D0%B5%D0%BD%D0%BD%D0%B8%D1%85%20%D1%82%D0%B5%D0%BC%2C%20%D1%96%D0%B7,%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%BC%20%D0%BD%D0%BE%D1%81%D1%96%D1%8F%D0%BC%D0%B8%20%D0%BC%D0%BE%D0%B2%D0%B8.%20%D0%9F%D0%BE%D0%B2%D0%BD%D1%96%D1%81%D1%82%D1%8E%20%D0%BF%D0%B5%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%B4%D0%B5%D0%BD%D0%BE%20%D0%BD%D0%B0%2035%20%D0%BC%D0%BE%D0%B2.'
    req = requests.get(link)
    soup = BeautifulSoup(req.content, "html.parser")
    for a in soup.find_all('a'):
        link = a.get('href')
        req = requests.get(link)
        new_soup = BeautifulSoup(req.content, "html.parser")
        for table in new_soup.find_all('table', class_='bilingual'):
            for tr in table.find_all('tr'):
                if a.text in forA1:
                    if word_pairs:= tr.find_all('td'):
                        parse_db.insert_into_lexic(word = word_pairs[0].text, translate=word_pairs[1].text, level='A1')
                elif a.text in forA2:
                    if word_pairs:= tr.find_all('td'):
                        parse_db.insert_into_lexic(word = word_pairs[0].text, translate=word_pairs[1].text, level='A2')
                elif a.text in forB1:
                    if word_pairs:= tr.find_all('td'):
                        parse_db.insert_into_lexic(word = word_pairs[0].text, translate=word_pairs[1].text, level='B1')
                elif a.text in forB2:
                    if word_pairs:= tr.find_all('td'):
                        parse_db.insert_into_lexic(word = word_pairs[0].text, translate=word_pairs[1].text, level='B2')
                else:
                    if word_pairs:= tr.find_all('td'):
                        parse_db.insert_into_lexic(word = word_pairs[0].text, translate=word_pairs[1].text, level='additionally')
    parse_db.close()
                       
pars_lexic()