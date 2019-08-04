'''
>>> import search_engine
>>> search_engine.initialize_from_scratch() # first time
>>> search_engine.add_product(3,'maggi masala') # duplicate entries are allowed
>>> search_engine.search('maggi')
'''

import sqlite3
conn = sqlite3.connect('search_index.db')

def add_product(product_id,description):
    conn.execute('''INSERT into products VALUES(?,?)''',(product_id,description))

def search(text):
    text = ' OR '.join(i for i in text.split())
    return conn.execute(f'''SELECT pid FROM products WHERE description MATCH '{text}' ORDER BY RANK''').fetchall()

def initialize_from_scratch():
    conn.execute('''DROP TABLE IF EXISTS products''')
    conn.execute('''CREATE VIRTUAL TABLE IF NOT EXISTS products USING FTS5(pid,description)''')

def clear_all():
    conn.execute('''DROP TABLE IF EXISTS products''')

def testing():
    conn.execute('''CREATE VIRTUAL TABLE IF NOT EXISTS products USING FTS5(pid,description)''')

    add_product(1,'maggi masala')
    add_product(2,'chai masala')
    add_product(3,'masala chai')
    add_product(4,'chai chai 31')
    add_product(5,'2 minute maggi')
    add_product(6,'chai maggi masala')


    print(search('maggi'))

if __name__ == '__main__':
    clear_all()
    testing()
