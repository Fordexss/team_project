import sqlite3
from constant import DB_FILE

class BotDB:
    def __init__(self, db_file_name) -> None:
        self.db_file_name = db_file_name

    def open(self):
        self.conn = sqlite3.connect(self.db_file_name)
        self.cursor = self.conn.cursor()

    def close(self):
        if hasattr(self, 'conn'):
            self.conn.close()

class DbParsingInterface(BotDB):    
    def insert_into_grammar(self, level, theme, text, video, id):
        self.cursor.execute("""INSERT INTO grammar(level, theme, text, video, id) VALUES(?, ?, ?, ?, ?)""", (level, theme, text, video, id))
        self.conn.commit()
        
    def create_default_table_grammar(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS grammar(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            theme TEXT,
            text TEXT,
            video TEXT,
            level VARCHAR(12)
    )""")
        
    def create_default_table_lexic(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS lexic(
            word TEXT,
            translate TEXT,
            level VARCHAR(12)
    )""")
        
    def insert_into_lexic(self, word, translate, level):
        self.cursor.execute("""INSERT INTO lexic(word, translate, level) VALUES(?, ?, ?)""", (word, translate, level))
        self.conn.commit()