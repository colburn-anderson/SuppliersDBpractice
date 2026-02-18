import psycopg2


def get_parts():
    """Query parts from the parts table"""
    conn = None

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="abcd123"
        )

        cur = conn.cursor()
        cur.execute("SELECT part_id, part_name FROM parts ORDER BY part_name")

        rows = cur.fetchall()

        print("The number of parts:", cur.rowcount)

        for row in rows:
            print(row)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_parts()
