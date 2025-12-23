import pandas as pd
def load_to_mysql(df,connection):
    df = df.where(pd.notnull(df), None)

    cursor = connection.cursor()

    insert_query = """
        INSERT IGNORE INTO retail_sales_store (transaction_id, customer_id, category, item, price_per_unit,
        quantity, total_spent, payment_method, location,
        transaction_date, discount_applied
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    data = [
        (
            row['transaction_id'], row['customer_id'], row['category'], row['item'], row['price_per_unit'],
            row['quantity'], row['total_spent'], row['payment_method'], row['location'],
            row['transaction_date'].date() if row['transaction_date'] else None, row['discount_applied']
            )
        for _, row in df.iterrows()
    ]

    cursor.executemany(insert_query,data)
    connection.commit()
    cursor.close()