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

    def grammar_text(self, level):
        self.cursor.execute("""
            SELECT theme, text
            FROM grammar
            WHERE level = ?
        """, (level, ))
        theme, text = self.cursor.fetchone()
        return f'{theme} {text}'
       
