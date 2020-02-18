-- Count numbers of each class
SELECT
	*
FROM (
	SELECT
		COUNT(DISTINCT character_ptr_id) AS clerics
	FROM
		charactercreator_cleric),
	(
		SELECT
			COUNT(DISTINCT character_ptr_id) AS fighters
		FROM
			charactercreator_fighter),
		(
			SELECT
				COUNT(DISTINCT character_ptr_id) AS mages
			FROM
				charactercreator_mage),
			(
				SELECT
					COUNT(DISTINCT mage_ptr_id) AS necromancers
				FROM
					charactercreator_necromancer),
				(
					SELECT
						COUNT(DISTINCT character_ptr_id) AS thieves
					FROM
						charactercreator_thief)

-- Count numbers of characters
SELECT COUNT(DISTINCT character_id) AS CHARACTERS FROM charactercreator_character;

-- Average Number of Weapons

query = """
   SELECT AVG(total_weapons)
   FROM (
    SELECT cc.name, COUNT(aw.power) as total_weapons
    FROM charactercreator_character cc
        LEFT JOIN charactercreator_character_inventory cci
            ON cc.character_id=cci.character_id
        LEFT JOIN armory_item ai ON cci.item_id=ai.item_id
        LEFT JOIN armory_weapon aw ON ai.item_id=aw.item_ptr_id
    GROUP BY cc.name)
    """
result = cursor.execute(query).fetchall()
print(f'On average, each character has {result[0][0]:.2f} weapons')

-- On average, how many Items does each Character have?
-- row per character, two columns 1 char name, 2 item count
-- for each character, how many items do they have
-- any characters that don't have any items? 
-- should we include them in our counts?
-- row per char (302 rows)
-- select *
-- from charactercreator_character
-- 898 rows (row per character per item)
-- how many characters in the inventory table??????
-- select count(distinct character_id) as char_count
-- from charactercreator_character_inventory
SELECT AVG(item_count) as avg_item_per_char -- 2.973
FROM (
    -- row per character
    SELECT 
     character_id
     ,count(distinct item_id) as item_count
    FROM charactercreator_character_inventory
    GROUP BY character_id
) subq
-- select 898.0 / 302
SELECT 
  count(id) as row_count
  ,count(distinct character_id) as char_count
  ,count(id) / cast(count(distinct character_id) as float) as avg_item_per_char
FROM charactercreator_character_inventory