
import os
import sqlite3
import pandas as pd
# construct a path to wherever your database exists
DB_FILEPATH = "rpg_db.sqlite3"

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()


def question_characters():    
    query = 'SELECT COUNT(*) FROM charactercreator_character;'    
    result = cursor.execute(query).fetchone()       
    print('How many total characters are there?', result[0])

def question_weapons():
    query = '''
    SELECT AVG(weapons.count) FROM ( 
                SELECT COUNT(*) as count 
                FROM charactercreator_character_inventory AS cci, 
                     armory_weapon AS aw 
                WHERE cci.item_id = aw.item_ptr_id
                GROUP BY character_id) as weapons;
    '''
    result = cursor.execute(query).fetchone()
    print('On average, how many weapons does each character have?', result[0])
#    print(pd.read_sql(query, connection).T.rename(columns={0: 'Count'}))
    
def question_items():
    query = '''
    SELECT AVG(items.count) FROM ( 
                SELECT COUNT(*) as count, character_id 
                FROM charactercreator_character_inventory 
                GROUP BY character_id) AS items;
    '''
    result = cursor.execute(query).fetchone()
    print('On average, how many items does each character have?', result[0])
#    print(pd.read_sql(query, connection).T.rename(columns={0: 'Count'}))

def question_character_classes():
    query = '''
    SELECT(SELECT COUNT(*) 
             FROM charactercreator_cleric) AS ClericCount, 
            (SELECT COUNT(*) 
            FROM charactercreator_mage) AS MageCount, 
            (SELECT COUNT(*) 
            FROM charactercreator_necromancer) AS NecroCount, 
            (SELECT COUNT(*) 
            FROM charactercreator_fighter) AS FighterCount, 
            (SELECT COUNT(*) 
            FROM charactercreator_thief) AS ThiefCount;
    '''
    print('How many characters are there of each specific subclass?')
    print(pd.read_sql(query, connection).T.rename(columns={0: 'Count'}))
    
def question_which_weapons():    
    query = 'SELECT COUNT(*) FROM armory_weapon;'
    weapon_count = cursor.execute(query).fetchone()

    query = 'SELECT COUNT(*) FROM armory_item;'
    item_count = cursor.execute(query).fetchone()
    print('How many of items, in total, do these characters have?', item_count[0])
    print('How many of the items are not weapons?', item_count[0]-weapon_count[0])
    print('How many of the items are weapons?', weapon_count[0])

question_characters()
question_which_weapons()
question_weapons()    
question_items()
question_character_classes()

