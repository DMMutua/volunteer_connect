import psycopg2

#Connection Object to DB
conn = psycopg2.connect(
    database="postgress",
    user="postgress",
    password="",
    host="127.0.0.1",
    port="5432"
)