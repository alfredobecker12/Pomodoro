import psycopg2 as ps


conn = ps.connect(
    dbname='pomodoro',
    user='postgres',
    password='root',
    host='localhost',
    port='5432')

