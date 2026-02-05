from db_Connector import get_connection
from tabulate import tabulate

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

        headers = ["ID", "Name", "Qty", "Price", "Category", "Expiry", "LowStockMin"]

        print(tabulate(rows, headers=headers, tablefmt="pretty"))

    except Exception as e:
        print(" Failed to fetch items:", e)

    finally:
        cursor.close()
        conn.close()
