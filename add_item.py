from db_Connector import get_connection

def add_item(name, quantity, price, category=None, expiry_date=None, low_stock_min=5):
    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute("SELECT item_id, quantity FROM items WHERE name = %s", (name,))
        existing = cursor.fetchone()

        if existing:
    
            new_qty = existing[1] + quantity
            cursor.execute("UPDATE items SET quantity = %s WHERE item_id = %s", (new_qty, existing[0]))
            conn.commit()
            print(f" Updated quantity of {name} to {new_qty}")

 
            if new_qty <= low_stock_min:
                print(f"⚠️ {name} is low on stock!")
            return

        sql = """
        INSERT INTO items (name, quantity, price, category, expiry_date, low_stock_min)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (name, quantity, price, category, expiry_date, low_stock_min))
        conn.commit()


        if quantity <= low_stock_min:
            print(f"⚠️ {name} is low on stock!")

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        conn.close()