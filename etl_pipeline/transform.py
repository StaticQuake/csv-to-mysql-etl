import pandas as pd
def transform_csv(df,save_path):
    # 1. Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )

    # 2. Convert date
    df['transaction_date'] = pd.to_datetime(
        df['transaction_date'], errors='coerce'
    )

    # 3. Handle discount_applied
    df['discount_applied'] = df['discount_applied'].fillna('False')
    df['discount_applied'] = df['discount_applied'].astype(bool)

    # 4. Drop rows with missing item
    df = df.dropna(subset=['item']).copy()

    # 5. Enforce numeric types
    df['price_per_unit'] = pd.to_numeric(
        df['price_per_unit'], errors='coerce'
    )
    df['quantity'] = pd.to_numeric(
        df['quantity'], errors='coerce'
    )

    # 6. Derived column
    df['total_spent'] = df['price_per_unit'] * df['quantity']

    df.to_csv(save_path,index=False)
    return df