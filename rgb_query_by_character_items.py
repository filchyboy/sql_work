
import os
import sqlite3
import pandas as pd
# construct a path to wherever your database exists
DB_FILEPATH = "rpg_db.sqlite3"

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

def question():
    query = '''
    SELECT AVG(items.count) FROM ( 
                SELECT COUNT(*) as count, character_id 
                FROM charactercreator_character_inventory 
                GROUP BY character_id) AS items;
    '''
    result = cursor.execute(query).fetchone()
    print('\nOn average, how many items does each character have?', result[0])

    print(pd.read_sql(query, connection).T.rename(columns={0: 'Count'}))
question()

