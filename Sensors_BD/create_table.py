import sqlite3	

#conecting with bd 

conn= sqlite3.connect('sensorsData.db')

#def cursor (cursor é um interador que permite navegar e manipular os registros do bd) 

cursor = conn.cursor() 

cur = cursor

#creating table (DHT_data) to save sensors data 

cur.execute("DROP TABLE IF EXISTS DHT_data")

cur.execute("CREATE TABLE DHT_data(timestamp DATETIME, temp NUMERIC, hum NUMERIC)")

print('tabela criada com sucesso.')

#desconectando do banco
conn.close() 

