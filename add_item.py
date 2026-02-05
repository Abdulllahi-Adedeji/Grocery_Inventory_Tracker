from db_Connector import get_connection

def add_item(name, quantity, price, category=None, expiry_date=None, low_stock_min=5):
    conn = get_connection()
    cursor = conn.cursor()
    
    sql = """
    INSERT INTO items (name, quantity, price, category, expiry_date, low_stock_min)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (name, quantity, price, category, expiry_date, low_stock_min))
    conn.commit()
    
    # Low stock check
    if quantity <= low_stock_min:
        print(f" {name} is low on stock!")
    
    cursor.close()
    conn.close()