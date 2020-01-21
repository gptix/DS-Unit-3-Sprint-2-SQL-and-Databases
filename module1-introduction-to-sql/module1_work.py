# Start sqlite
import sqlite3
sqlite_conn = sqlite3.connect('rpg_db.sqlite3')

# get cursor
sqlite_cursor = sqlite_conn.cursor()



# How many characters are there?

characters = sqlite_cursor.execute("SELECT * FROM charactercreator_character;").fetchall()
print ("There are " + str(len(characters)) + " characters.")


# How many of each specific subclass?

subclasses = ['thief', 'cleric', 'fighter', 'mage', 'necromancer'];
print()
for sc in subclasses:
  print((sc, len(sqlite_cursor.execute("SELECT * FROM charactercreator_" + sc + ";").fetchall())))

# generaate code 
# for s in subclasses:
#     print(s + "_subclass_count = len(sqlite_cursor.execute(\"SELECT * FROM charactercreator_"  + s + ";\").fetchall())"

thief_subclass_count = len(sqlite_cursor.execute("SELECT * FROM charactercreator_thief;").fetchall())
cleric_subclass_count = len(sqlite_cursor.execute("SELECT * FROM charactercreator_cleric;").fetchall())
fighter_subclass_count = len(sqlite_cursor.execute("SELECT * FROM charactercreator_fighter;").fetchall())
mage_subclass_count = len(sqlite_cursor.execute("SELECT * FROM charactercreator_mage;").fetchall())
necromancer_subclass_count = len(sqlite_cursor.execute("SELECT * FROM charactercreator_necromancer;").fetchall())
          

# Looks like necromancers are also mages.  Don't count twice.
mage_not_necro_count = mage_subclass_count - necromancer_subclass_count
# mage_not_necro_count
print()
print('thief_subclass_count       = ' + str(thief_subclass_count))
print('cleric_subclass_count      = ' + str(cleric_subclass_count))
print('fighter_subclass_count     = ' + str(fighter_subclass_count))
print('mage_subclass_count        = ' + str(mage_subclass_count))
print('  mages that are also necromancer_subclass_count = ' + str(necromancer_subclass_count))
print('  mages that are NOT also necromancer_subclass_count = ' + str(mage_not_necro_count))


# How many total Items?
print()
armory_item_count = len(  sqlite_cursor.execute("SELECT * FROM armory_item;").fetchall()  )
print("Total Items: " + str(armory_item_count))

# How many of the Items are weapons? How many are not?
armory_weapon_count = len(  sqlite_cursor.execute("SELECT * FROM armory_weapon;").fetchall())
print()
print("Total Weapons: " + str(armory_weapon_count))
print()
non_weapon_count = armory_item_count - armory_weapon_count
print("Total Non-Weapons: " + str(non_weapon_count))
print("Worked.")


# How many Items does each character have? (Return first 20 rows)
item_per_char_count_select_statement_limit_20 = "\
    SELECT cc.name, COUNT(ai.item_id) \
    FROM charactercreator_character AS cc, \
        armory_item AS ai, \
        charactercreator_character_inventory as cci \
    WHERE cc.character_id = cci.character_id \
    AND ai.item_id = cci.item_id \
    GROUP BY cc.character_id \
    ORDER BY COUNT(ai.item_id) DESC\
    LIMIT 20;"
item_count_answer = sqlite_cursor.execute(item_per_char_count_select_statement_limit_20).fetchall()
print();
print("Top 20 Item Counts by Character:")
print();
print(item_count_answer)


# How many Weapons does each character have? (Return first 20 rows)
weapon_per_char_count_select_statement_limit_20 = "\
    SELECT cc.name, COUNT(aw.item_ptr_id) \
    FROM charactercreator_character AS cc, \
         armory_weapon AS aw, \
         charactercreator_character_inventory as cci \
    WHERE cc.character_id = cci.character_id \
    AND aw.item_ptr_id = cci.item_id \
    GROUP BY cc.character_id \
    ORDER BY COUNT(aw.item_ptr_id) DESC \
    LIMIT 20;"
print();
print("Top 20 Weapon Counts by Character:")
print();
weapon_count_limit_20_answer= sqlite_cursor.execute(weapon_per_char_count_select_statement_limit_20).fetchall()
print(weapon_count_limit_20_answer)

# On average, how many Items does each Character have?
char_count = sqlite_cursor.execute("SELECT COUNT(character_id) FROM charactercreator_character").fetchall()[0][0]
# char_count
item_count_answer_sql = "\
    SELECT COUNT(ai.item_id) \
    FROM charactercreator_character AS cc, \
         armory_item AS ai, \
         charactercreator_character_inventory as cci \
    WHERE cc.character_id = cci.character_id \
    AND ai.item_id = cci.item_id \
    GROUP BY cc.character_id \
    ORDER BY COUNT(ai.item_id) DESC;"

item_counts= sqlite_cursor.execute(item_count_answer_sql).fetchall()

items_total = 0
for item in item_counts:
    items_total += item[0]
    
# items_total    

average_items_per_char = items_total / char_count
print()
print("The average item count per character is: " + str(average_items_per_char))

# On average, how many Weapons does each character have?
weapon_count_answer_sql = "\
    SELECT COUNT(aw.item_ptr_id) \
    FROM charactercreator_character AS cc, \
         armory_weapon AS aw, \
         charactercreator_character_inventory as cci \
    WHERE cc.character_id = cci.character_id \
    AND aw.item_ptr_id = cci.item_id \
    GROUP BY cc.character_id \
    ORDER BY COUNT(aw.item_ptr_id) DESC;"

weapon_counts= sqlite_cursor.execute(weapon_count_answer_sql).fetchall()

weapons_total = 0
for w in weapon_counts:
    weapons_total += w[0]
    
# weapons_total    

average_weapons_per_char = weapons_total / char_count

print("The average weapon count per character is: " + str(average_weapons_per_char))
