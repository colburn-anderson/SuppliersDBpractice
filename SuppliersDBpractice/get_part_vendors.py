import psycopg2


def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def get_part_vendors():
    """Query part and vendor data from multiple tables"""
    conn = None

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="abcd123"
        )

        cur = conn.cursor()

        cur.execute("""
            SELECT part_name, vendor_name
            FROM parts
            INNER JOIN vendor_parts 
                ON vendor_parts.part_id = parts.part_id
            INNER JOIN vendors 
                ON vendors.vendor_id = vendor_parts.vendor_id
            ORDER BY part_name;
        """)

        for row in iter_row(cur, 10):
            print(row)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_part_vendors()
