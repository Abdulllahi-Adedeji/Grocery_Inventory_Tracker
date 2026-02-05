from db_Connector import get_connection

def view_items(category=None, low_stock_only=False):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = "SELECT item_id, name, quantity, price, category, expiry_date, low_stock_min FROM items"
        filters = []
        values = []

        if category:
            filters.append("category = %s")
            values.append(category)

        if low_stock_only:
            filters.append("quantity <= low_stock_min")

        if filters:
            sql += " WHERE " + " AND ".join(filters)

        sql += " ORDER BY name"  

        cursor.execute(sql, tuple(values))
        rows = cursor.fetchall()

        if not rows:
            print("No items found.")
            return

        print(f"{'ID':<5} {'Name':<20} {'Qty':<5} {'Price':<8} {'Category':<15} {'Expiry':<12} {'LowStockMin':<12}")
        print("-" * 80)
        for row in rows:
            item_id, name, quantity, price, category, expiry_date, low_stock_min = row
            print(f"{item_id:<5} {name:<20} {quantity:<5} {price:<8.2f} {str(category):<15} {str(expiry_date):<12} {low_stock_min:<12}")

    except Exception as e:
        print(" Failed to fetch items:", e)

    finally:
        cursor.close()
        conn.close()
