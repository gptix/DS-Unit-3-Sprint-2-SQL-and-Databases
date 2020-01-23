# My Answer to the Discussion Question

## "How was working with MongoDB different from working with 
## PostgreSQL? What was easier, and what was harder?"

# I see a lot of value in both of them. NoSQL is neat because a data model can be changed 
# implicitly by receiving pairs with new keys. This means that special attention might be
# needed to remember to deal with records that did not have new keys.

# On the other hand, SQL dbs can be a hassle because records and tables can be orphaned, 
# e.g., when a parent record that has child records is deleted, if discipline is not 
# used, the child records can stick around in the data base forever.

# I look forward to seeing how NewSQL changes things.


import pymongo
import sqlite3

## Settings
password = "not-real"
path_to_sqlite_db = './'
## Connect to mongoDB.com


client_request_string = "mongodb://gptix:" + password + "@cluster0-shard-00-00-dxpn7.mongodb.net:27017,cluster0-shard-00-01-dxpn7.mongodb.net:27017,cluster0-shard-00-02-dxpn7.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority"
client = pymongo.MongoClient(client_request_string)
db = client.test

## Connect to sqlite database at path
sl_conn  = sqlite3.connect(path_to_sqlite_db + 'rpg_db.sqlite3')
sl_curs = sl_conn.cursor()


## get charactercreator_character rows
sl_char_rows_SQL = 'SELECT * FROM charactercreator_character'
sl_char_rows = sl_curs.execute(sl_char_rows_SQL).fetchall()


### Prepare data for insert into mongoDB
colnames = ['character_id', ' name', ' level', ' exp', ' hp', 
            ' strength', ' intelligence', ' dexterity', ' wisdom']


# len(sl_char_rows) # test
# sl_char_rows[:3]  # test

# one_row = sl_char_rows[0] 
# one_row

# dictionary = dict(zip(colnames, one_row))
# print(dictionary)


## Create list of dictionaries, each dict a character.
char_dicts = []
for row in sl_char_rows:
  char_dicts.append(dict(zip(colnames, row)))



# len(char_dicts)
db.test.insert_many(char_dicts)
