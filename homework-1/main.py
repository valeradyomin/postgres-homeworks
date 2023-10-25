"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
mypass = os.getenv("PSQL_PSW")


def load_from_csv(filename):
    path_to_csv = os.path.join("..", "homework-1", "north_data", filename)
    try:
        with open(path_to_csv, newline="", encoding="UTF-8") as csvfile:
            reader = csv.DictReader(csvfile)
            return [tuple(row.values()) for row in reader]
    except FileNotFoundError:
        print(f"Отсутствует файл {filename}")
