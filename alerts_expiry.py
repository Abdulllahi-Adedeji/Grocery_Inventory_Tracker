from datetime import datetime, timedelta
from tabulate import tabulate
from db_Connector import get_connection
def expiry_alert(days=7, category=None):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        today = datetime.today()
        alert_date = today + timedelta(days=days)

        sql = "SELECT item_id, name, expiry_date, quantity FROM items WHERE expiry_date <= %s"
        values = [alert_date]

        if category:
            sql += " AND category = %s"
            values.append(category)

        cursor.execute(sql, tuple(values))
        rows = cursor.fetchall()

        if not rows:
            print(f" No items expiring within {days} days!")
            return

        headers = ["ID", "Name", "Expiry Date", "Quantity"]
        print(f"Expiry Alerts (next {days} days):")
        print(tabulate(rows, headers=headers, tablefmt="pretty"))

    except Exception as e:
        print(" Failed to fetch expiry alerts:", e)
    finally:
        cursor.close()
        conn.close()
