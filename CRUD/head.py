# import the sqlite module
import sqlite3

# initialize a conection the databse or create a new on if it does not exist
conection = sqlite3.connect('salesNov.db')

# Initialize a method to create a cursor
pointer = conection.cursor()
