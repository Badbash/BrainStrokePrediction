import mysql.connector

def database():
    mydb = mysql.connector.connect(
        host='localhost', user='root', password='soumil123')
    cur = mydb.cursor()
    cur.execute('create database brainstorm;')
    print('Database Created')


database()