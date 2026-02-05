from db_Connector import get_connection

def update_item(item_id, quantity=None, price=None, category=None, expiry_date=None, low_stock_min=None):
    conn = get_connection()
    cursor = conn.cursor()

    try:
   
        cursor.execute("SELECT * FROM items WHERE item_id = %s", (item_id,))
        item = cursor.fetchone()
        if not item:
            print(f" Item with ID {item_id} not found. Cannot update.")
            return

        if quantity is not None and quantity < 0:
            print(" Quantity cannot be negative")
            return
        if price is not None and price < 0:
            print("Price cannot be negative")
            return
        if low_stock_min is not None and low_stock_min < 0:
            print(" Low stock minimum cannot be negative")
            return


        fields = []
        values = []

        if quantity is not None:
            fields.append("quantity = %s")
            values.append(quantity)
        if price is not None:
            fields.append("price = %s")
            values.append(price)
        if category is not None:
            fields.append("category = %s")
            values.append(category)
        if expiry_date is not None:
            fields.append("expiry_date = %s")
            values.append(expiry_date)
        if low_stock_min is not None:
            fields.append("low_stock_min = %s")
            values.append(low_stock_min)

        if not fields:
            print("No fields to update")
            return

        
        sql = f"UPDATE items SET {', '.join(fields)} WHERE item_id = %s"
        values.append(item_id) 

       
        cursor.execute(sql, tuple(values))
        conn.commit()
        print(f" Item ID {item_id} updated successfully")

    except Exception as e:
        print("Update failed:", e)

    finally:
        cursor.close()
        conn.close()
