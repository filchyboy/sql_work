
import os
import sqlite3
import pandas as pd
# construct a path to wherever your database exists
DB_FILEPATH = "rpg_db.sqlite3"
#DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "rpg_db.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()
query = """
SELECT COUNT(DISTINCT character_id) AS CHARACTERS FROM charactercreator_character;"""

result = cursor.execute(query).fetchall()


for row in result:
    characters = row["CHARACTERS"]
    print("Characters:",characters)          
 
#df = pd.read_sql_query('SELECT * FROM table', conectionn)

def question2():
    query = 'SELECT(SELECT COUNT(*) \
             FROM charactercreator_cleric) AS cleric_count, \
            (SELECT COUNT(*) \
            FROM charactercreator_mage) AS mage_count, \
            (SELECT COUNT(*) \
            FROM charactercreator_necromancer) AS necro_count, \
            (SELECT COUNT(*) \
            FROM charactercreator_fighter) AS fighter_count, \
            (SELECT COUNT(*) \
            FROM charactercreator_thief) AS thief_count;'
#    print('\nHow many of each specific subclass?')
    print(pd.read_sql(query, connection).T.rename(columns={0: 'Count'}))
#df = pd.read_sql(query, connection).T.rename(columns={0: 'Count'})
question2()