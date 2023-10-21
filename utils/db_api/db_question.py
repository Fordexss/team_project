from utils.db_api.db import BasicInterface

class DbQuestionInterface(BasicInterface):
    def create_question_table(self, cr):
        cr.execute('''
            CREATE TABLE IF NOT EXISTS question (
                id INTEGER PRIMARY KEY,
                question TEXT,
                level VARCHAR,
                question_translation TEXT,
                answers TEXT,
                right_answer TEXT,
                points INTEGER)''')

    def initialize_database(self):
        cr = self.cursor
        self.create_question_table(cr)
        cr.execute('SELECT id FROM question WHERE id = 1')
        if not cr.fetchone():
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your name?', 'A1', 'Як тебе звати?', 'John&Blue&Name', 'John', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How old are you?', 'A1', 'Скільки тобі років?', 'Yes&I''m 25 years old&Cat', 'I''m 25 years old', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Where are you from?', 'A1', 'Звідки ти?', 'Good morning&I''m from France&Banana', 'I''m from France', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What time is it?', 'A1', 'Котра година?', 'Yellow&It''s 2 o''clock&Dog', 'It''s 2 o''clock', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Do you like pizza?', 'A1', 'Тобі подобається піца?', 'No, thank you&Yes, I do&Car', 'Yes, I do', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How many siblings do you have?', 'A1', 'Скільки у тебе братів і сестер?', 'Red&I have one brother and two sisters&Monday', 'I have one brother and two sisters', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s this?', 'A1', 'Що це?', 'Green&It''s a book&Apple', 'It''s a book', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Are you a student?', 'A1', 'Ти студент?', 'No, I''m not&Yes, I''m&Bike', 'Yes, I''m', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How do you spell \"cat\"?', 'A1', 'Як ти вимовиш \"кіт\"?', 'C-A-R&C-A-T&C-A-P', 'C-A-T', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How many days are in a week?', 'A1', 'Скільки днів у тижні?', 'Five&Seven&Ten', 'Seven', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What color is the sky?', 'A1', 'Який колір неба?', 'Fish&The sky is blue&No color', 'The sky is blue', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Where do you work?', 'A1', 'Де ти працюєш?', 'I like pizza&I work in an office&Sun', 'I work in an office', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your favorite animal?', 'A1', 'Яка твоя улюблена тварина?', 'Elephant&I like dogs&Chair', 'I like dogs', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Do you have any pets?', 'A1', 'У тебе є домашні тварини?', 'No, I don''t&Yes, I have a cat&Orange', 'Yes, I have a cat', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What you do on weekends', 'A1', 'Що ти робиш на вихідних?', 'I like ice cream&I usually go hiking&Book', 'I usually go hiking', 1)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Can you swim?', 'A1', 'Ти вмієш плавати?', 'No, I can''t&Yes, I can swim&Shoe', 'Yes, I can swim', 1)")


            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What did you do yesterday?', 'A2', 'Що ти робив вчора?', 'I watched a movie&I''m eating lunch&It''s sunny', 'I watched a movie', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Where is the nearest post office?', 'A2', 'Де найближча пошта?', 'I like pizza&Turn right at the corner&The cat is sleeping', 'Turn right at the corner', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How often do you exercise?', 'A2', 'Як часто ти займаєшся фізичними вправами?', 'The weather is nice today&I go to the gym twice a week&The book is on the table', 'I go to the gym twice a week', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Can you cook spaghetti?', 'A2', 'Ти можешь готувати спагеті?', 'I have a red car&Yes, I can cook spaghetti&The keys are in my bag', 'Yes, I can cook spaghetti', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What are you going to do this weekend?', 'A2', 'Що ти плануєш робити на цих вихідних?', 'The flowers are in the garden&I''m going to visit my grandparents&I like to read books', 'I''m going to visit my grandparents', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Why do you like that movie?', 'A2', 'Чому тобі подобається цей фільм?', 'I don''t like rainy days&Because it''s funny and exciting&The dog is barking', 'Because it''s funny and exciting', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How far is the train station from here?', 'A2', 'Як далеко відсюди залізничний вокзал?', 'I prefer to walk&It''s about a 10-minute walk&The music is too loud', 'It''s about a 10-minute walk', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Do you have any siblings?', 'A2', 'У тебе є брати або сестри?', 'I like to play the guitar&Yes, I have one sister&The sun is shining', 'Yes, I have one sister', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What kind of music do you enjoy listening to?', 'A2', 'Яку музику ти любиш слухати?', 'I can speak Spanish&I enjoy rock and pop music&The cat is climbing a tree', 'I enjoy rock and pop music', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Have you ever traveled abroad?', 'A2', 'Ти коли-небудь подорожував за кордоном?', 'I have a blue backpack&Yes, I have been to France&The book is on the shelf', 'Yes, I have been to France', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What do you like to do in your free time?', 'A2', 'Що тобі подобається робити у вільний час?', 'I don''t have any money&I enjoy reading and playing sports&The dog is running in the park', 'I enjoy reading and playing sports', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How do you usually celebrate your birthday?', 'A2', 'Як ти зазвичай святкуєш свій день народження?', 'I live in a small town&I invite friends and have a party&The weather is cold today', 'I invite friends and have a party', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Can you recommend a good restaurant?', 'A2', 'Ти можеш порекомендувати хороший ресторан?', 'I need to buy a new phone&Yes, there''s a great Italian restaurant downtown&The keys are on the table', 'Yes, there''s a great Italian restaurant downtown', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your favorite season?', 'A2', 'Яка твоя улюблена пора року?', 'I don''t have a car&I love the autumn season&Cats are cute', 'I love the autumn season', 2.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Do you enjoy cooking?', 'A2', 'Ти любиш готувати?', 'I''m going to the beach&Yes, I find it relaxing and fun&The weather is good', 'Yes, I find it relaxing and fun', 2.5)")


            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your favorite childhood memory?', 'B1', 'Яке твоє улюблене дитинство спогад?', 'I don''t remember much from my childhood&One of my favorite memories is building sandcastles at the beach&I have a blue bicycle', 'One of my favorite memories is building sandcastles at the beach', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How has technology changed your life?', 'B1', 'Як технології змінили твоє життя?', 'I don''t use technology much&Technology has made communication easier and more convenient&I need to buy a new computer', 'Technology has made communication easier and more convenient', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What do you think are the biggest challenges in the world today?', 'B1', 'Які, на твою думку, найбільші виклики у сучасному світі?', 'I don''t think about global challenges&Climate change and inequality are among the biggest challenges&I have a red phone', 'Climate change and inequality are among the biggest challenges', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How do you deal with stress?', 'B1', 'Як ти впораєшся зі стресом?', 'I get stressed easily&I practice relaxation techniques and exercise to manage stress&The book is on the shelf', 'I practice relaxation techniques and exercise to manage stress', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Do you think it''s important to learn a second language?', 'B1', 'Ти вважаєш важливим вивчати другу мову?', 'I don''t see the importance of learning another language&Yes, learning a second language opens up new opportunities and perspectives&The cat is sleeping on the couch', 'Yes, learning a second language opens up new opportunities and perspectives', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s the most adventurous thing you''ve ever done?', 'B1', 'Яке найбільш відважне, що ти коли-небудь робив?', 'I''m not a very adventurous person&I went skydiving once and it was thrilling&The weather is cold today', 'I went skydiving once, and it was thrilling', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What do you enjoy most about your job?', 'B1', 'Що тобі подобається найбільше у своїй роботі?', 'I don''t really like my job&I enjoy the opportunity to solve challenging problems&I have a green laptop', 'I enjoy the opportunity to solve challenging problems', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How do you stay motivated to achieve your goals?', 'B1', 'Як ти зберігаєш мотивацію до досягнення своїх цілей?', 'I struggle with motivation&Setting clear goals and tracking progress keeps me motivated&The music is too loud', 'Setting clear goals and tracking progress keeps me motivated', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your favorite way to relax and unwind?', 'B1', 'Яким способом ти найкраще відпочиваєш і розслабляєшся?', 'I don''t have much time to relax&I like to read a good book or take a long walk&I need to buy a new camera', 'I like to read a good book or take a long walk', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('Have you ever had to overcome a major obstacle in your life?', 'B1', 'Чи доводилось тобі подолати серйозну перешкоду у своєму житті?', 'I''ve faced some challenges but nothing major&Yes, I had to overcome a serious illness&The keys are on the table', 'Yes, I had to overcome a serious illness', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your favorite book or movie and why?', 'B1', 'Яка твоя улюблена книга або фільм і чому?', 'I''m not much of a reader or movie buff&My favorite book is \"To Kill a Mockingbird\" because of its powerful themes&The dog is running in the park', 'My favorite book is \"To Kill a Mockingbird\" because of its powerful themes', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your approach to making important decisions?', 'B1', 'Як ти підходиш до прийняття важливих рішень?', 'I usually rely on others to make decisions for me&I gather information and weigh the pros and cons and make an informed choice&The weather is nice today', 'I gather information, weigh the pros and cons, and make an informed choice', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What do you value most in your friendships?', 'B1', 'Що для тебе найцінніше у дружбі?', 'I haven''t thought about it much&Trust and loyalty are essential in my friendships&The book is on the shelf', 'Trust and loyalty are essential in my friendships', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How do you like to spend your holidays?', 'B1', 'Як ти любиш проводити свої канікули?', 'I don''t take many vacations&I enjoy traveling and exploring new places&The cat is sleeping on the couch', 'I enjoy traveling and exploring new places', 4.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your opinion on social media?', 'B1', 'Яка твоя думка щодо соціальних медіа?', 'I''m not active on social media&I think it''s a useful tool for staying connected but should be used mindfully&The music is too loud', 'I think it''s a useful tool for staying connected but should be used mindfully', 4.5)")


            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What are the implications of artificial intelligence on the job market?', 'B2', 'Які наслідки штучного інтелекту на ринок праці?', 'I haven''t thought much about it&AI could lead to job displacement but also create new roles&I have a blue car', 'AI could lead to job displacement but also create new roles', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How would you define success in life?', 'B2', 'Як би ти визначив успіх у житті?', 'Success means different things to different people&To me success is achieving personal goals and finding fulfillment&The keys are on the table', 'To me, success is achieving personal goals and finding fulfillment', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What impact do global events have on your daily life?', 'B2', 'Як впливають глобальні події на твоє повсякденне життя?', 'I try to stay informed but don''t see a direct impact&Global events can influence my job and travel plans and more&The weather is nice today', 'Global events can influence my job, travel plans, and more', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your perspective on the role of government in society?', 'B2', 'Яка твоя точка зору на роль уряду в суспільстві?', 'I''m not very interested in politics&Government plays a crucial role in providing services and regulations&The cat is sleeping on the couch', 'Government plays a crucial role in providing services and regulations', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What ethical considerations should be taken into account in scientific research?', 'B2', 'Які етичні аспекти слід враховувати в наукових дослідженнях?', 'I haven''t studied ethics in science&Ethical research includes informed consent and minimizing harm&The book is on the shelf', 'Ethical research includes informed consent and minimizing harm', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('In your opinion, what are the keys to effective communication?', 'B2', 'На твою думку, які ключові аспекти ефективного спілкування?', 'Effective communication involves active listening and clarity&I don''t think much about communication&The weather is cold today', 'Effective communication involves active listening and clarity', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What are the advantages and disadvantages of globalization?', 'B2', 'Які переваги і недоліки глобалізації?', 'Globalization has economic benefits but can lead to cultural homogenization&I''m not sure about globalization&The music is too loud', 'Globalization has economic benefits but can lead to cultural homogenization', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How do you see the future of renewable energy?', 'B2', 'Як ти бачиш майбутнє відновлювальних джерел енергії?', 'I''m not well-informed about renewable energy&Renewable energy will likely play a major role in reducing environmental impact&I have a green laptop', 'Renewable energy will likely play a major role in reducing environmental impact', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What motivates you to continue learning and growing?', 'B2', 'Що тебе мотивує продовжувати навчатися і розвиватися?', 'I don''t have a strong motivation to learn&Continuous learning helps me adapt and achieve personal goals&The dog is running in the park', 'Continuous learning helps me adapt and achieve personal goals', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How do you think advancements in technology will shape the future of work?', 'B2', 'Як ти думаєш, як розвиток технологій вплине на майбутню роботу?', 'I''m not sure about the future of work&Technology will create new job opportunities but also require new skills&The weather is nice today', 'Technology will create new job opportunities but also require new skills', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your approach to balancing work and personal life?', 'B2', 'Як ти підходиш до балансу між роботою і особистим життям?', 'I prioritize work over personal life&I strive to maintain a healthy work-life balance&The cat is sleeping on the couch', 'I strive to maintain a healthy work-life balance', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What role does creativity play in problem-solving?', 'B2', 'Яку роль вирішенні проблем відіграє творчість?', 'I don''t think creativity is necessary for problem-solving&Creativity can lead to innovative solutions and fresh perspectives&I need to buy a new camera', 'Creativity can lead to innovative solutions and fresh perspectives', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your opinion on the impact of social media on society?', 'B2', 'Яка твоя думка про вплив соціальних медіа на суспільство?', 'I don''t use social media so I don''t have an opinion&Social media has both positive and negative effects on society&The book is on the shelf', 'Social media has both positive and negative effects on society', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What strategies do you use for personal financial management?', 'B2', 'Які стратегії використовуєш для особистого фінансового управління?', 'I don''t pay much attention to my finances&I budget and save and invest to secure my financial future&The music is too loud', 'I budget, save, and invest to secure my financial future', 5.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your perspective on the importance of lifelong learning?', 'B2', 'Яка твоя точка зору на важливість вивчення на протязі всього життя?', 'I don''t think learning is important beyond formal education&Lifelong learning is essential for personal growth and adaptation&The dog is running in the park', 'Lifelong learning is essential for personal growth and adaptation', 5.5)")

            
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What are the ethical dilemmas in advanced medical technology?', 'C1', 'Які етичні дилеми в інноваційних медичних технологіях?', 'I''m not familiar with medical ethics&Ethical dilemmas may arise in areas like genetic engineering and organ transplantation&I have a blue car', 'Ethical dilemmas may arise in areas like genetic engineering and organ transplantation', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your perspective on the impact of literature on society?', 'C1', 'Яка твоя думка про вплив літератури на суспільство?', 'I don''t read much literature&Literature can shape culture and provoke thought and foster empathy&The keys are on the table', 'Literature can shape culture, provoke thought, and foster empathy', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How does the concept of beauty vary across cultures?', 'C1', 'Як змінюється концепція краси у різних культурах?', 'I haven''t explored cross-cultural perspectives on beauty&Beauty standards differ widely and are culturally influenced&The weather is nice today', 'Beauty standards differ widely and are culturally influenced', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('In your opinion, What''s the role of art in contemporary society?', 'C1', 'На твою думку, яка роль мистецтва в сучасному суспільстві?', 'I don''t pay much attention to art&Art can challenge norms and provoke discussion and inspire change&I need to buy a new camera', 'Art can challenge norms, provoke discussion, and inspire change', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How do you assess the impact of technology on education?', 'C1', 'Як ти оцінюєш вплив технологій на освіту?', 'I''m not well-informed about educational technology&Technology can enhance learning but also present challenges&The music is too loud', 'Technology can enhance learning but also present challenges', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your perspective on the role of media in shaping public opinion?', 'C1', 'Яка твоя точка зору на роль ЗМІ у формуванні громадської думки?', 'I don''t think media has much influence&Media can shape public opinion and should provide balanced information&The dog is running in the park', 'Media can shape public opinion and should provide balanced information', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How do you see the future of renewable energy?', 'C1', 'Як ти бачиш майбутнє відновлювальних джерел енергії?', 'I''m not well-versed in energy trends&Renewable energy is crucial for a sustainable future and will continue to grow&The weather is cold today', 'Renewable energy is crucial for a sustainable future and will continue to grow', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What strategies can organizations use to promote diversity and inclusion?', 'C1', 'Які стратегії можуть використовувати організації для сприяння різноманітності та інклюзії?', 'I haven''t thought much about diversity in organizations&Strategies include inclusive policies and training and diverse hiring practices&I have a green laptop', 'Strategies include inclusive policies, training, and diverse hiring practices', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What challenges do emerging technologies pose to privacy?', 'C1', 'Які виклики ставлять перед приватністю нові технології?', 'I haven''t considered the privacy implications of emerging tech&Emerging tech can lead to data breaches and surveillance concerns&The cat is sleeping on the couch', 'Emerging tech can lead to data breaches and surveillance concerns', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('In your opinion, how should governments address climate change?', 'C1', 'На твою думку, як уряди повинні вирішувати проблему зміни клімату?', 'I''m not well-informed on climate policy&Governments should take bold actions and invest in renewables and set emission targets&The weather is nice today', 'Governments should take bold actions, invest in renewables, and set emission targets', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How do you see the future of work in a post-pandemic world?', 'C1', 'Як ти бачиш майбутнє роботи в світі після пандемії?', 'I''m not sure about the future of work&Remote work and digital skills and and flexibility will shape the post-pandemic workplace&The weather is nice today', 'Remote work, digital skills, and flexibility will shape the post-pandemic workplace', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What''s your perspective on the impact of social media on politics?', 'C1', 'Яка твоя думка про вплив соціальних медіа на політику?', 'I don''t follow politics on social media&Social media can amplify political movements but also spread misinformation&The music is too loud', 'Social media can amplify political movements but also spread misinformation', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('What strategies can individuals use to combat climate change?', 'C1', 'Які стратегії можуть використовувати особи для боротьби зі зміною клімату?', 'I haven''t taken personal action on climate change&Individuals can reduce their carbon footprint and support clean energy and advocate for policies&The book is on the shelf', 'Individuals can reduce their carbon footprint, support clean energy, and advocate for policies', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('How can individuals foster innovation in their personal and professional lives?', 'C1', 'Як можуть особи сприяти інноваціям у своєму особистому та професійному житті?', 'I haven''t thought much about fostering innovation&Fostering innovation involves curiosity and risk-taking and collaboration&The music is too loud', 'Fostering innovation involves curiosity, risk-taking, and collaboration', 6.5)")
            cr.execute("INSERT INTO question(question, level, question_translation, answers, right_answer, points) VALUES ('In your opinion, What''s the significance of lifelong learning?', 'C1', 'На твою думку, яка значущість навчання на протязі всього життя?', 'I don''t see the value of lifelong learning&Lifelong learning fosters personal growth and adaptability and innovation&The dog is running in the park', 'Lifelong learning fosters personal growth, adaptability, and innovation', 6.5)")

        self.conn.commit()

    def create_column_english_level(self):
        self.cursor.execute('''ALTER TABLE students ADD english_level VARCHAR(255);''')
        self.conn.commit()

    def update_english_level(self, level, user_id):
        self.cursor.execute("PRAGMA table_info('students')")
        column_exists = any(column[1] == 'english_level' for column in self.cursor.fetchall())
        if column_exists:
            pass
        else:
            self.create_column_english_level()
        self.cursor.execute("UPDATE students SET english_level = ? WHERE id = ?", (level, user_id))
        self.conn.commit()

    def user_in_db(self, user_id):
        self.cursor.execute(f"""
        SELECT id
        FROM students
        WHERE id = {user_id}
        """)
        # return self.cursor.fetchone()
        is_user_in_db = self.cursor.fetchone()
        return bool(is_user_in_db)

        # is_user_exists = self.cursor.fetchone()[0]
        # return bool(is_user_exists)