import psycopg2


def get_vendors():
    """Query data from the vendors table"""
    conn = None

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="abcd123"
        )

        cur = conn.cursor()
        cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name")

        print("The number of tuples:", cur.rowcount)

        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    get_vendors()
