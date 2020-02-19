
import os
import sqlite3

DB_FILEPATH = "rpg_db.sqlite3"
connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()
query = """
SELECT
    *
FROM
    (SELECT COUNT(DISTINCT character_ptr_id) as clerics FROM charactercreator_cleric)
    ,(SELECT COUNT(DISTINCT character_ptr_id) as fighters FROM charactercreator_fighter)
    ,(SELECT COUNT(DISTINCT character_ptr_id) as mages FROM charactercreator_mage)
    ,(SELECT COUNT(DISTINCT mage_ptr_id) as necromancers FROM charactercreator_necromancer)
    ,(SELECT COUNT(DISTINCT character_ptr_id) as thieves FROM charactercreator_thief)
"""

result = cursor.execute(query).fetchall()

for row in result:
    cleric = row["clerics"]
    print("Clerics:",cleric)
    fighter = row["fighters"]
    print("Fighters:",fighter)  
    mages = row["mages"]
    print("Mages:",mages)    
    necromancers = row["necromancers"]
    print("Necromancers:",necromancers)    
    thieves = row["thieves"]
    print("Thieves:",thieves)       
  
 