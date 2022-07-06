import sqlite3

from sqlite3 import Error

def sql_connection():

    try:
        ## make the connection to db:
        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:

        print(Error)

def sql_table(con):

    ## make the connection to db:
    cursorObj = con.cursor()

    ## CREATE creates db:
    # cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

    ## INSERT put values 1st way:
    # cursorObj.execute("INSERT INTO employees VALUES(2, 'John', 700, 'HR', 'Manager', '2017-01-04')")

    ## INSERT put values 2nd way:
    # entities = (4, 'Adam', 800, 'IT', 'Tech', '2022-02-06')
    # cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)

    ## UPDATE values name (Rogers) with id=2
    # cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')

    ## SELECT part of table
    cursorObj.execute("SELECT id, name FROM employees")

    # commit - publish
    con.commit()

con = sql_connection()

sql_table(con)