"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

# release connection to database
conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="1739")
try:
    with conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", ('ALFKI', 'Alfreds Futterkiste', 'Maria Anders'))
            cur.execute("SELECT * FROM customers")

            # print results
            rows = cur.fetchall()
            for row in rows:
                print(row)
finally:
    conn.close()
