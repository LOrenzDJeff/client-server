import sqlite3

def cratedatabase():
    con = sqlite3.connect('example.db')
    cursor = con.cursor()

    try:
        # Создаем таблицу
        cursor.execute('''CREATE TABLE numbers
                        (id INTEGER PRIMARY KEY, 
                        value INTEGER)''')
        #cursor.execute('''INSERT INTO numbers (id, value) VALUES (0, 0)''')
        con.commit()

    except sqlite3.OperationalError:
        print("Таблица уже создана")
        
    con.close()

def newcell(id):
    con = sqlite3.connect('example.db')
    cursor = con.cursor()
    cursor.execute("SELECT value FROM numbers WHERE id = (?)", (id,))
    flag  = str(cursor.fetchone())
    if flag == "None":
        cursor.execute("INSERT INTO numbers (value) VALUES (0)")
        con.commit()
    else:
        print("Данный id уже есть")
    con.close()

def databaseset(num, id):
    # Создаем таблицу
    con = sqlite3.connect('example.db')
    cursor = con.cursor()
    cursor.execute("SELECT value FROM numbers WHERE id = (?)", (id,))
    numstr = cursor.fetchone()
    numfin = ""
    for i in numstr:
        if i == "(" or i == ")" or i == ",":
            continue
        numfin += str(i)
    numfin = int(numfin) + int(num)
    cursor.execute("UPDATE numbers SET value = (?) WHERE id = (?)", (numfin, id,))
    con.commit()
    con.close()