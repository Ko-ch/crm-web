import sqlite3


def init_db():
    """データベースの初期化を行う関数"""
    conn = sqlite3.connect("crm.sqlite")
    cursor = conn.cursor()

    with open("schema.sql", encoding="utf-8") as f:
        sql = f.read()

    cursor.executescript(sql)

    conn.commit()

    conn.close()


def db():
    conn = sqlite3.connect("crm.sqlite")
    cursor = conn.cursor()

    sql = """SELECT * FROM customers"""

    results = cursor.execute(sql)

    allname = results.fetchall()

    conn.commit()

    conn.close()

    return allname


def addcustomer(name, age):
    conn = sqlite3.connect("crm.sqlite")
    cursor = conn.cursor()

    sql = f"""INSERT INTO customers VALUES ("{name}", {age})"""

    cursor.execute(sql)

    conn.commit()

    conn.close()


if __name__ == "__main__":
    init_db()
