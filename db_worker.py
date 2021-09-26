import sqlite3


class Worker:
    def __init__(self):
        self.conn = sqlite3.connect('data.sqlite3')
        self.cur = self.conn.cursor()
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            chat_id TEXT NOT NULL,
            captcha TEXT NOT NULL,
            full_name TEXT NOT NULL
            );
            """
        )
        self.conn.commit()

    def get_users(self):
        self.cur.execute("SELECT * FROM users;")
        db_users = self.cur.fetchall()

        return db_users

    def save_user(self, user_id, chat_id, captcha, full_name):
        self.cur.execute(f"""INSERT INTO users(user_id, chat_id, captcha, full_name)
                           VALUES('{user_id}', '{chat_id}', '{captcha}', '{full_name}');""")
        self.conn.commit()

    def delete_users(self, user_id, chat_id):
        self.cur.execute(f"""DELETE FROM users                                       
                                WHERE user_id = '{user_id}' AND chat_id = '{chat_id}'
                        """)
        self.conn.commit()
