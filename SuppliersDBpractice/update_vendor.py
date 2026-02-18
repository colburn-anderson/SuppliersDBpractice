import psycopg2


def update_vendor(vendor_id, vendor_name):
    """Update vendor name based on the vendor id"""
    sql = """
        UPDATE vendors
        SET vendor_name = %s
        WHERE vendor_id = %s
    """

    conn = None
    updated_rows = 0

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="suppliers",
            user="postgres",
            password="abcd123",
            port="5432"
        )

        cur = conn.cursor()

        # Execute the UPDATE statement
        cur.execute(sql, (vendor_name, vendor_id))

        # Get number of updated rows
        updated_rows = cur.rowcount
        print("Updated rows:", updated_rows)

        # Commit changes
        conn.commit()

        # Close cursor
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)

    finally:
        if conn is not None:
            conn.close()

    return updated_rows


if __name__ == '__main__':
    # Update vendor id 1
    update_vendor(1, "3M Corp")
