import sqlite3
import json


class Register:
    def __init__(self):
        self.conn = sqlite3.connect('transactions.db', check_same_thread=False)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    account_no INTEGER,
                    date TEXT,
                    type TEXT,
                    amount REAL
                )
            ''')
            #self.conn.execute('CREATE INDEX IF NOT EXISTS idx_account_no ON transactions (account_no);')

    def add_Transaction(self, account_no, date, type, amount):
        with self.conn:
            self.conn.execute('''
                INSERT INTO transactions (account_no, date, type, amount)
                VALUES (?, ?, ?, ?)
            ''', (account_no, date, type, amount))
        new_transaction = {
            "Account_no": account_no,
            "Date": date,
            "Type": type,
            "Amount": amount
        }
        return json.dumps(new_transaction)


    def get_Transaction(self, account_no):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT account_no, date, type, amount FROM 'transactions' WHERE account_no = ?
        ''', (account_no,))
        return cursor.fetchall()
    
    def get_Sum(self, account_no):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT SUM(CASE 
                            WHEN type = 'deposit' THEN amount 
                            WHEN type = 'withdraw' THEN -amount 
                            ELSE 0 
                        END) 
                FROM transactions WHERE account_no = ?
            ''', (account_no,))
            return cursor.fetchone()[0] or 0
        except Exception as e:
            print(f"Error occurred while fetching sum for account_no {account_no}: {e}")
            raise e

