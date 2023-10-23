from utils.db_api.db import BasicInterface

class LearnInfo(BasicInterface):
    def user_level(self, user_id):
        self.cursor.execute("""SELECT english_level
        FROM students
        WHERE id = ?
        """, (user_id, ))
        level = self.cursor.fetchone()
        if level:
            return level[0]
        else:
            return "Щоб продовжити вам потрібно зареєструватись"

    def grammar(self, level):
        self.cursor.execute("""
            SELECT theme, text
            FROM grammar
            WHERE level = ?
        """, (level, ))
        text = self.cursor.fetchall()
        return text
    
    def video(self, level):
        self.cursor.execute("""
            SELECT theme, video
            FROM grammar
            WHERE level = ?
        """, (level, ))
        fetch = self.cursor.fetchall()
        return fetch
    
    def lexic(self, level):
        self.cursor.execute("""
            SELECT word, translate
            FROM lexic
            WHERE level = ?
        """, (level, ))
        word = self.cursor.fetchall()
        return word
    
    def insert_grammar(self, themes, id):
        self.cursor.execute("""
            INSERT INTO score(themes_grammar, id)
            VALUES(?, ?)
    """, (themes, id))
        self.conn.commit()

    def score_grammar(self, themes, id):
        self.cursor.execute("""
            UPDATE score
            SET themes_grammar = ?
            WHERE id = ?
    """, (themes, id))
        self.conn.commit()

    def gram_quantity(self, id):
        self.cursor.execute("""
            SELECT themes_grammar
            FROM score
            WHERE id = ?
    """, (id, ))
        themes = self.cursor.fetchone()
        return themes

    def insert_video(self, video, user_id):
        self.cursor.execute("""
            INSERT INTO score(watched_video, id)
            VALUES(?, ?)
    """, (video, user_id))
        self.conn.commit()

    def score_videos(self, video, id):
        self.cursor.execute("""
            UPDATE score
            SET watched_video = ?
            WHERE id = ?
    """, video, id)
        self.conn.commit()

    def video_quantity(self, id):
        self.cursor.execute("""
            SELECT watched_video
            FROM score
            WHERE id = ?
    """, (id, ))
        themes = self.cursor.fetchone()
        return themes

    def insert_words(self, words, id):
        self.cursor.execute("""
            INSERT INTO score(learned_words, id)
            VALUES(?, ?)
    """, (words, id))
        self.conn.commit()

    def score_words(self, word, id):
        self.cursor.execute("""
            UPDATE score
            SET learned_words = ?
            WHERE id = ?
    """, word, id)
        self.conn.commit()

    def words_quntity(self, id):
        self.cursor.execute("""
            SELECT learned_words
            FROM score
            WHERE id = ?
    """, (id, ))
        themes = self.cursor.fetchone()
        return themes

    def user_score(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS score(
                id INTEGER PRIMARY KEY,
                themes_grammar INTEGER,
                learned_words INTEGER, 
                watched_video INTEGER
            );
    """)

    
        
       
