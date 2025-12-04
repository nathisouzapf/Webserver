from db import connect_db

def insert_data(value):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO data (value) VALUES (?)',
        (value,)
    )

    conn.commit()
    conn.close()


def get_all_data():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM data')
    rows = cursor.fetchall()

    conn.close()

    return [{"id": row[0], "data": row[1]} for row in rows]