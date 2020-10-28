import os
import sqlite3

if os.getcwd() != 'C:\\Users\\Utilisateur\\Google Drive\\Python\\BaseDeDonnees':
    os.chdir(r"Google Drive\Python\BaseDeDonnees")

conn = sqlite3.connect('ma_base.db')


cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     duree INTEGER,
     vignette TEXT,
     path TEXT
     Note INTEGER
)
""")
conn.commit()

cursor.execute("""INSERT INTO users(name, duree) VALUES(?, ?)""", ("olivier", 30))
conn.close()