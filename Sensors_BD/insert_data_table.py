import sqlite3 as lite 
import sys 

#conecting with bd 

conn= lite.connect('sensorsData.db') 


#def cursor (cursor é um interador que permite navegar e manipular os registros do bd) 

cursor = conn.cursor() 

cur = cursor

#criando função add_data para adicionar dados a tabela DHT_data 

def add_data (temp, hum): 
	 # chamamos o cursor para executar o comando em sql que insere valores a tabela DHT_data 
	 # os valores são (dados de data e hora e valores em aberto para a temperatura e humidade)
	
	 cur.execute("INSERT INTO DHT_data values(datetime('now'), (?), (?))", (temp, hum))
	 conn.commit()
	 
	 #chamamos a funcão add_data e passamos os parametros de (temperatura, humidade) 
add_data (25.5, 32)
add_data (28.8, 42)
add_data (35.3, 59) 
	 
# usamos a função print para escrever uma entrada para os dados 	 
print ("\nTodos os conteudos da tabela DHT_data:\n") 

# definimos uma iteração com o loop for para caminhar por todas as linhas da tabela e escrevemos cada linha

for row in cur.execute('SELECT * FROM DHT_data'): 
	print(row) 
	
#desconectando do banco de dados

conn.close() 	
