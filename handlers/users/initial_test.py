from aiogram import types
from aiogram.dispatcher import FSMContext
import random

from keyboards.default import dynamic_reply_kb
from keyboards.inline import details, main_page_kb, prev_button, next_button, answers_markup
from loader import dp, ques, db_question, bot
from states import InitialTestStates
from aiogram.types import ReplyKeyboardRemove
from utils.misc import ROWS_PER_PAGE, TOTAL_PAGES, TOTAL_QUESTIONS, A1_LEVEL_DESC, A2_LEVEL_DESC, B1_LEVEL_DESC, B2_LEVEL_DESC, C1_LEVEL_DESC

data_pages_a = []

def question(prev_number, number, num_name, state_name, next_number_state):
    @dp.message_handler(text=ques[prev_number][4].split('&'), state=state_name)
    async def que(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            if message.text == ques[prev_number][5]:
                data['score'] += ques[number][6]
                data[f'answer_{prev_number}'] = f'✅ Ви правильно відповіли! Відповідь: {ques[prev_number][5]}'
            else:
                data[f'answer_{prev_number}'] = f"❌ Ви неправильно відповіли. Правильна відповідь: {ques[prev_number][5]}"
        await message.answer('📌 Ваша відповідь зарахована.')
        await message.answer(f'⬇️ {num_name} питання:') 
        await message.answer(ques[number][1], reply_markup=dynamic_reply_kb(ques[number][4].split('&')))
        await next_number_state.set()

def sort_by_lvl(cr, lvl, quality):
    my_qns = set()
    while len(my_qns) < quality:
        cr.execute(f"""SELECT * FROM question
        WHERE level == "{lvl}"
        """)
        questions_by_lvl = cr.fetchall()
        for _ in range(0, quality):
            my_qns.add(random.choice(questions_by_lvl))
    if lvl == 'A1':
        a = 1
        for q in my_qns:
            ques[a] = list(q)
            a += 1
    elif lvl == 'A2':
        a = 6
        for q in my_qns:
            ques[a] = list(q)
            a += 1
    elif lvl == 'B1':
        a = 11
        for q in my_qns:
            ques[a] = list(q)
            a += 1
    elif lvl == 'B2':
        a = 16
        for q in my_qns:
            ques[a] = list(q)
            a += 1
    elif lvl == 'C1':
        a = 21
        for q in my_qns:
            ques[a] = list(q)
            a += 1
    my_qns.clear()

@dp.message_handler(commands='test') 
async def first_question(message: types.Message, state: FSMContext):
    if db_question.user_in_db(message.from_user.id):
        async with state.proxy() as data:
            data['score'] = 0
        await message.answer('⬇️ Перше питання:')
        await message.answer(ques[1][1], reply_markup=dynamic_reply_kb(ques[1][4].split('&')))
        await InitialTestStates.second_q.set()
    else:
        await message.answer('Ви ще не зареєстровані, тож не можете пройти тест! Для раєстрації — /start')

@dp.message_handler(lambda message: message.text == "Звісно!", state=InitialTestStates.start_initial_test)
async def first_question(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['score'] = 0
    await message.answer('⬇️ Перше питання:')
    await message.answer(ques[1][1], reply_markup=dynamic_reply_kb(ques[1][4].split('&')))
    await InitialTestStates.second_q.set()

def init_questions():
    sort_by_lvl(db_question.cursor, 'A1', 5)
    sort_by_lvl(db_question.cursor, 'A2', 5)
    sort_by_lvl(db_question.cursor, 'B1', 5)
    sort_by_lvl(db_question.cursor, 'B2', 5)
    sort_by_lvl(db_question.cursor, 'C1', 5)
    question(1, 2, 'Друге', InitialTestStates.second_q, InitialTestStates.third_q)
    question(2, 3, 'Третє', InitialTestStates.third_q, InitialTestStates.fourth_q)
    question(3, 4, 'Четверте', InitialTestStates.fourth_q, InitialTestStates.fifth_q)
    question(4, 5, 'П\'яте', InitialTestStates.fifth_q, InitialTestStates.sixth_q)
    question(5, 6, 'Шосте', InitialTestStates.sixth_q, InitialTestStates.seventh_q)
    question(6, 7, 'Сьоме', InitialTestStates.seventh_q, InitialTestStates.eighth_q)
    question(7, 8, 'Восьме', InitialTestStates.eighth_q, InitialTestStates.ninth_q)
    question(8, 9, 'Дев\'яте', InitialTestStates.ninth_q, InitialTestStates.tenth_q)
    question(9, 10, 'Десяте', InitialTestStates.tenth_q, InitialTestStates.eleventh_q)
    question(10, 11, 'Одинадцяте', InitialTestStates.eleventh_q, InitialTestStates.twelfth_q)
    question(11, 12, 'Дванадцяте', InitialTestStates.twelfth_q, InitialTestStates.thirteenth_q)
    question(12, 13, 'Тринадцяте', InitialTestStates.thirteenth_q, InitialTestStates.fourteenth_q)
    question(13, 14, 'Чотирнадцяте', InitialTestStates.fourteenth_q, InitialTestStates.fifteenth_q)
    question(14, 15, 'П\'ятнадцяте', InitialTestStates.fifteenth_q, InitialTestStates.sixteenth_q)
    question(15, 16, 'Шістнадцяте', InitialTestStates.sixteenth_q, InitialTestStates.seventeenth_q)
    question(16, 17, 'Сімнадцяте', InitialTestStates.seventeenth_q, InitialTestStates.eighteenth_q)
    question(17, 18, 'Вісімнадцяте', InitialTestStates.eighteenth_q, InitialTestStates.nineteenth_q)
    question(18, 19, 'Дев\'ятнадцяте', InitialTestStates.nineteenth_q, InitialTestStates.twentieth_q)
    question(19, 20, 'Двадцяте', InitialTestStates.twentieth_q, InitialTestStates.twenty_first_q)
    question(20, 21, 'Двадцять перше', InitialTestStates.twenty_first_q, InitialTestStates.twenty_second_q)
    question(21, 22, 'Двадцять друге', InitialTestStates.twenty_second_q, InitialTestStates.twenty_third_q)
    question(22, 23, 'Двадцять третє', InitialTestStates.twenty_third_q, InitialTestStates.twenty_fourth_q)
    question(23, 24, 'Двадцять четверте', InitialTestStates.twenty_fourth_q, InitialTestStates.twenty_fifth_q)
    question(24, 25, 'Двадцять п\'яте', InitialTestStates.twenty_fifth_q, InitialTestStates.end_of_initial_test)


    @dp.message_handler(text=ques[25][4].split('&'), state=InitialTestStates.end_of_initial_test)
    async def que(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            if message.text == ques[25][5]:
                data['score'] += ques[25][6]
                data[f'answer_25'] = f'✅ Ви правильно відповіли! Відповідь: {ques[25][5]}'
            else:
                data[f'answer_25'] = f"❌ Ви неправильно відповіли. Правильна відповідь: {ques[25][5]}"
            if data['score'] < 5:
                data['level'] = 'Ви ще зовсім початківець'
            elif data['score'] >= 5 and data['score'] < 22.5:
                data['level'] = 'A1'
            elif data['score'] >= 22.5 and data['score'] < 45:
                data['level'] = 'A2'
            elif data['score'] >= 45 and data['score'] < 72.5:
                data['level'] = 'B1'
            elif data['score'] >= 72.5 and data['score'] < 95:
                data['level'] = 'B2'
            else:
                data['level'] = 'C1'
            level = data['level']
            user_id = message.from_user.id
            db_question.update_english_level(level=level, user_id=user_id)
        await message.answer('Ваша відповідь зарахована.')
        await message.answer(f'Вітаємо! Тест на визначення вашого рівня англійської завершено! Ваш результат: {data["score"]}. Ваш рівень — {data["level"]}.', reply_markup=ReplyKeyboardRemove())
        await message.answer('Додатково:', reply_markup=details(data['level']))

    @dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
    async def bot_echo_all(message: types.Message, state: FSMContext):
        my_state = await state.get_state()
        if my_state == 'InitialTestStates:start_initial_test':
            await message.answer('Щоб почати тест на визначення рівня володінння англійською мовою, напишіть "Звісно!"')
        elif my_state in InitialTestStates and my_state != 'InitialTestStates:end_of_initial_test':
            await message.answer("Будь ласка, оберіть відповідь із доступних!")
        else:
            pass

@dp.callback_query_handler(text='answers', state=InitialTestStates.end_of_initial_test)
async def check_answers(call: types.CallbackQuery, state: FSMContext):
    answers = ''
    async with state.proxy() as data:
        for n in range(1, 26):
            answer = f'{n}. ' + str(data[f'answer_{n}'])
            answers = answers + ' ' + answer + '\n'
    data_pages_a.extend(answers.split('\n'))
    current_page = 0
    await send_current_page(call, data_pages_a, current_page)

async def send_current_page(call, data_pages, current_page):
    if current_page < len(data_pages):
        start_index = current_page * ROWS_PER_PAGE
        end_index = (current_page + 1) * ROWS_PER_PAGE
        page_data = data_pages[start_index:end_index]
        text = '\n'.join(page_data)
        buttons = []
        if current_page > 0:
            buttons.append(prev_button)
        if current_page < TOTAL_PAGES - 1:
            buttons.append(next_button)
        await call.message.edit_text(text, reply_markup=answers_markup(buttons))

@dp.callback_query_handler(text='next_page', state=InitialTestStates.end_of_initial_test)
async def next_page(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        current_page = data.get('current_page', 0)
        if current_page < TOTAL_PAGES - 1:
            current_page += 1
            data['current_page'] = current_page
            await send_current_page(call, data_pages_a, current_page)

@dp.callback_query_handler(text='prev_page', state=InitialTestStates.end_of_initial_test)
async def prev_page(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        current_page = data.get('current_page', 0)
        if current_page > 0:
            current_page -= 1
            data['current_page'] = current_page
            await send_current_page(call, data_pages_a, current_page)

@dp.callback_query_handler(text='main', state=InitialTestStates.end_of_initial_test)
async def main_page(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await call.message.edit_text('Додатково:', reply_markup=details(data['level']))
        

@dp.callback_query_handler(text='about_lvl', state=InitialTestStates.end_of_initial_test)
async def check_answers(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        if data['level'] == 'Ви ще зовсім початківець':
            desc = 'Ви тільки почали вивчати англійську, тож ми не можемо точно визначити ваш рівень. Але віримо що у вас все попереду, успіхів!'
        elif data['level'] == 'A1':
            desc = A1_LEVEL_DESC
        elif data['level'] == 'A2':
            desc = A2_LEVEL_DESC
        elif data['level'] == 'B1':
            desc = B1_LEVEL_DESC
        elif data['level'] == 'B2':
            desc = B2_LEVEL_DESC
        elif data['level'] == 'C1':
            desc = C1_LEVEL_DESC
    await call.message.edit_text(desc, parse_mode='HTML', reply_markup=main_page_kb)