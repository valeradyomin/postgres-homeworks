import json

import psycopg2

from config import config


def main():
    script_file = 'fill_db.sql'
    json_file = 'suppliers.json'
    db_name = 'homework5'

    params = config()
    conn = None

    create_database(params, db_name)
    print(f"БД {db_name} успешно создана")

    params.update({'dbname': db_name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                execute_sql_script(cur, script_file)
                print(f"БД {db_name} успешно заполнена")

                create_suppliers_table(cur)
                print("Таблица suppliers успешно создана")

                suppliers = get_suppliers_data(json_file)
                insert_suppliers_data(cur, suppliers)
                print("Данные в suppliers успешно добавлены")

                add_foreign_keys(cur, json_file)
                print(f"FOREIGN KEY успешно добавлены")

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def create_database(params, db_name) -> None:
    """Создает новую базу данных."""
    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute("SELECT datname FROM pg_catalog.pg_database WHERE datname = %s", (db_name,))
    exist = cur.fetchone()

    if exist:
        cur.execute(f"DROP DATABASE {db_name}")

    cur.execute(f"CREATE DATABASE {db_name}")
    conn.close()


def execute_sql_script(cur, script_file) -> None:
    """Выполняет скрипт из файла для заполнения БД данными."""
    with open(script_file, 'r', encoding='UTF-8') as file:
        sql_file = file.read()
        cur.execute(sql_file)
        # cur.close()


def create_suppliers_table(cur) -> None:
    """Создает таблицу suppliers."""
    with cur:
        cur.execute("CREATE TABLE IF NOT EXISTS suppliers ("
                    "supplier_id SERIAL PRIMARY KEY,"
                    "company_name VARCHAR(100),"
                    "contact VARCHAR(100),"
                    "address VARCHAR(100),"
                    "phone VARCHAR(30),"
                    "fax VARCHAR(30),"
                    "homepage VARCHAR(50),"
                    "products TEXT"
                    ");")
        cur.close()


def get_suppliers_data(json_file: str) -> list[dict]:
    """Извлекает данные о поставщиках из JSON-файла и возвращает список словарей с соответствующей информацией."""
    with open(json_file, "rt", encoding="UTF-8") as file:
        data_json = json.load(file)
        return data_json


def insert_suppliers_data(cur, suppliers: list[dict]) -> None:
    """Добавляет данные из suppliers в таблицу suppliers."""
    pass


def add_foreign_keys(cur, json_file) -> None:
    """Добавляет foreign key со ссылкой на supplier_id в таблицу products."""
    pass


if __name__ == '__main__':
    main()
