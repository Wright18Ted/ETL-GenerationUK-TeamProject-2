def create_order_table():
    result = """
     CREATE TABLE IF NOT EXISTS orders (
            order_id UUID PRIMARY KEY,
            order_timestamp TIMESTAMP NOT NULL,
            location VARCHAR(50) NOT NULL,
            items_ordered TEXT NOT NULL,
            total_amount NUMERIC(10,2) NOT NULL,
            payment_method VARCHAR(10) NOT NULL
            CHECK (payment_method IN ('CARD', 'CASH'))
    """
    return result
