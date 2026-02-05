from db_Connector import get_connection

def total_inventory_value(category=None):
  
    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = "SELECT SUM(quantity * price) FROM items"
        values = []

        if category:
            sql += " WHERE category = %s"
            values.append(category)

        cursor.execute(sql, tuple(values))
        result = cursor.fetchone()
        total_value = result[0] if result[0] else 0

        if category:
            print(f"Total value of {category} inventory: €{total_value:.2f}")
        else:
            print(f" Total value of all inventory: €{total_value:.2f}")

    except Exception as e:
        print("Failed to calculate total inventory value:", e)

    finally:
        cursor.close()
        conn.close()