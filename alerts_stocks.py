from tabulate import tabulate
from db_Connector import get_connection

def low_stock_alert(category=None):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = "SELECT item_id, name, quantity, low_stock_min FROM items WHERE quantity <= low_stock_min"
        values = []

        if category:
            sql += " AND category = %s"
            values.append(category)

        cursor.execute(sql, tuple(values))
        rows = cursor.fetchall()

        if not rows:
            print(" No low-stock alerts!")
            return

        headers = ["ID", "Name", "Qty", "LowStockMin"]
        print("⚠️ Low Stock Alerts:")
        print(tabulate(rows, headers=headers, tablefmt="pretty"))

    except Exception as e:
        print("Failed to fetch low-stock alerts:", e)
    finally:
        cursor.close()
        conn.close()
