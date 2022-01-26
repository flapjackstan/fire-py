import json
import pandas as pd

from src.CRUD import db

with open('data/json/santa-ana-cafe-1.json',encoding='utf8') as json_data:
        sb = json.load(json_data)
    
sb = sb['results']
sb = pd.json_normalize(sb)
sb = sb[['place_id', 'name', 'formatted_address', 'geometry.location.lat', 'geometry.location.lng', 'types', 'rating', 'user_ratings_total']]
sb.rename(columns={"geometry.location.lat": "lat", "geometry.location.lng": "lng"}, inplace=True)

filt = ['restaurant']
mask = sb['types'].apply(lambda s: len(set(s) & set(filt)) > 0)

sb = sb[~mask]
del(mask,filt)

test = db('/fire-py-1ce4b/', 'https://fire-py-1ce4b.firebaseio.com/')
    
#This creates a table if none exists, else it adds a row to the table
table = 'santa-ana'
test.create_table(table,sb)

# uid = '-MFLXSC6jYRI-90YlqEC'
# attribute = 'Name'
# change = 'Ricky'
# test.update(table,uid,attribute,change)


## selects all
# table = 'Test'
# query = ''
# json = test.read(table,query)
# df = pd.DataFrame.from_dict(json, orient='index')
# print(df.head())

#test.delete(table,uid)