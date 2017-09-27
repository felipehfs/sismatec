import sqlite3
import datetime
from model.contact_model import Contact

class ContactDAO(object):
    """
    Data object Access of Contact
    """
    def __init__(self, con):
        self.con = con
        self.cursor = self.con.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS contacts(
    code INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birthday DATE,
    email TEXT
    )''')
        self.con.commit()
            
    def create(self, contact):
        self.cursor.execute('''INSERT INTO contacts (name,email, birthday) VALUES(?,?,?)''',
                     (contact.name, contact.email, contact.birthday))
        self.con.commit()

    def update(self, contact):
        self.cursor.execute('''UPDATE contacts SET name=?, email=?, birthday=? WHERE code=?''',
                            (contact.name, contact.email, contact.birthday, contact.code))
        self.con.commit()

    def find_by_id(self, code):
        self.cursor.execute("SELECT name, email, birthday, code FROM contacts WHERE code=?", (code,))
        row = self.cursor.fetchone()
        if row is None:
            return row
        return Contact(*row)
    
    def read(self):
        self.cursor.execute("SELECT name, email, birthday, code FROM contacts")
        contatos = []
        for row in self.cursor.fetchall():
            contatos.append(Contact(*row))
        return contatos

    def remove(self, code):
        self.cursor.execute("DELETE FROM contacts WHERE code=?", (code,))
        self.con.commit()
    
    def __del__(self):
        self.con.close()


