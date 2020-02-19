
import os
import sqlite3
import pandas as pd

DB_FILEPATH = "rpg_db.sqlite3"

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

table = input("Table : ")
print(table)
df = pd.read_sql('SELECT * FROM charactercreator_character', connection)
print(df.head);