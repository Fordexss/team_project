from utils.db_api.db import BasicInterface


class DbUserInterface(BasicInterface):
    def save_user_data(self, data, user_id):
        self.cursor.execute("INSERT INTO students (name, last_name, phone_number, id) VALUES (?, ?, ?, ?)",
                            (data['name'], data['last_name'], data['phone_number'], user_id))
        self.conn.commit()

    def user_exists(self, user_id):
        self.cursor.execute("""
        SELECT COUNT(*)
        FROM students
        WHERE id = ?
        """, (user_id,))
        is_user_exists = self.cursor.fetchone()[0]
        return bool(is_user_exists)

    def create_default_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name VARCHAR(255),
                last_name VARCHAR(255),
                phone_number VARCHAR(255)
            );
        """)
        return self.conn.commit()
