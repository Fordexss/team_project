from utils.db_api.db import BasicInterface

class LearnInfo(BasicInterface):
    def grammar_text(self, theme, text, level):
        self.cursor.execute("""
            SELECT theme, text
            FROM grammar
            WHERE level = ?
        """, (level))
        grammar = self.cursor.fetchone()
        if text:
            result = ""
            for theme, text in grammar:
                result = f"{theme, text}"
            return result
        else:
            return "Щоб продовжити вам потрібно зареєструватись"



    def close(self):
        if hasattr(self, 'conn'):
            self.conn.close()