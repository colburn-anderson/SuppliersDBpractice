import psycopg2


def insert_vendor(vendor_name):
    """Insert a new vendor into the vendors table"""
    sql = """INSERT INTO vendors(vendor_name) 
             VALUES(%s) RETURNING vendor_id;"""
    conn = None
    vendor_id = None

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="abcd123"
        )

        cur = conn.cursor()
        cur.execute(sql, (vendor_name,))  # Execute INSERT
        vendor_id = cur.fetchone()[0]    # Get generated ID
        print("Inserted vendor ID:", vendor_id)

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

    finally:
        if conn is not None:
            conn.close()

    return vendor_id


def insert_vendor_list(vendor_list):
    """Insert multiple vendors into the vendors table"""
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="abcd123"
        )

        cur = conn.cursor()
        cur.executemany(sql, vendor_list)

        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    # Insert one vendor
    insert_vendor("3M Co.")

    # Insert multiple vendors
    insert_vendor_list([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])
