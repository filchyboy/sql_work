
import os
import sqlite3
import pandas as pd
# construct a path to wherever your database exists
DB_FILEPATH = "rpg_db.sqlite3"

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

def question():
    query = 'SELECT AVG(weapons.count) FROM ( \
                SELECT COUNT(*) as count \
                FROM charactercreator_character_inventory AS cci, \
                     armory_weapon AS aw \
                WHERE cci.item_id = aw.item_ptr_id \
                GROUP BY character_id) as weapons'
    result = cursor.execute(query).fetchone()
    print('\nOn average, how many weapons does each character have?',
          result[0])
    print(pd.read_sql(query, connection).T.rename(columns={0: 'Count'}))
question()

