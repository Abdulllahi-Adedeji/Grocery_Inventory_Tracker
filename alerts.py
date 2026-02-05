from db_Connector import get_connection
from tabulate import tabulate

def view_low_stock(category=None):
  
    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = "SELECT item_id, name, quantity, price, category, expiry_date, low_stock_min FROM items WHERE quantity <= low_stock_min"
        values = []

        if category:
            sql += " AND category = %s"
            values.append(category)

        sql += " ORDER BY name"

        cursor.execute(sql, tuple(values))
        rows = cursor.fetchall()

        if not rows:
            print("No low-stock items found.")
            return

        table_data = []
        for row in rows:
            item_id, name, quantity, price, category, expiry_date, low_stock_min = row
            table_data.append([
                item_id,
                name,
                quantity,
                price,
                category,
                expiry_date,
                low_stock_min,
                "YES" 
            ])

        headers = ["ID", "Name", "Qty", "Price", "Category", "Expiry", "LowStockMin", "Low Stock"]
        print(tabulate(table_data, headers=headers, tablefmt="pretty"))

    except Exception as e:
        print(" Failed to fetch low-stock items:", e)

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    view_low_stock() 