import os 
import sqlite3 as lite 
import sys 

# simple script to create a db 

db_filename = 'sensorsData.db' 

conn = lite.connect(db_filename)

conn.close()

