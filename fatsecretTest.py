from fatsecret import Fatsecret
import psycopg2
clientID = 'c1ffa8c2349d498b878ddc82422bbe2d'
clientSecret = '58ba7b4983ac4b0187fd0c68999e1d50'

fs = Fatsecret(clientID, clientSecret)

auth_url = fs.get_authorize_url()

print("Browse to the following URL in your browser to authorize access:\n{}".format(auth_url))

pin = input("Enter the PIN provided by FatSecret: ")
session_token = fs.authenticate(pin)
date_time_str='11/08/20'
foods=fs.foods_search('Pineapple')

SERVER = '176.15.105.107'
DATABASE = 'stavteamdb'
UID = 'stavteamdb'
PWD = '111111'
cnxn = psycopg2.connect(dbname=DATABASE, user=UID,
                        password=PWD, host=SERVER)
cursor = cnxn.cursor()
for food in foods:
    cursor.execute("INSERT INTO public.fatsecretfoods "+
                    "(name, fatsecretid) "+
                    "VALUES('"+food['food_name'].replace("'","''")+"', "+str(food['food_id'])+"); ")
    cnxn.commit()
cnxn.close()
print(len(foods))