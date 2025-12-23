CREATE TABLE retail_sales_store (
    transaction_id VARCHAR(30) PRIMARY KEY, 
    customer_id VARCHAR(30), 
    category VARCHAR(30), 
    item VARCHAR(30), 
    price_per_unit DECIMAL(10,2),
    quantity DECIMAL(10,2),
    total_spent DECIMAL(10,2),
    payment_method VARCHAR(30),
    location VARCHAR(30),
    transaction_date DATE,
    discount_applied TINYINT(1)
);