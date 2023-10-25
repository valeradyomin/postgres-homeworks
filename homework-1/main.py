"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
mypass = os.getenv("PSQL_PSW")


def load_from_csv(filename):
    """
    Загружает данные из CSV-файла в список кортежей.
    Args:
        filename (str): Имя CSV-файла.
    Returns:
        list: Список кортежей с данными из CSV-файла.
    """
    path_to_csv = os.path.join("..", "homework-1", "north_data", filename)
    try:
        with open(path_to_csv, newline="", encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return [tuple(row.values()) for row in reader]
    except FileNotFoundError:
        print(f"Отсутствует файл {filename}")


def main():
    """
    Заполняет таблицы в БД Postgres данными из CSV-файлов.
    """
    conn = psycopg2.connect(host="localhost", database="north", user="postgres", password=mypass)
    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", load_from_csv("customers_data.csv"))
                cur.execute("SELECT * FROM customers")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

                cur.executemany(
                    "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", load_from_csv("employees_data.csv"))
                cur.execute("SELECT * FROM employees")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

                cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", load_from_csv("orders_data.csv"))
                cur.execute("SELECT * FROM orders")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    finally:
        conn.close()


if __name__ == "__main__":
    main()
