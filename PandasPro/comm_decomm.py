# compressing data - reducing the size of a dataset while preserving its essential information
# decompressing data - restoring the original dataset from its compressed form

import pandas as pd

import os

df = pd.read_csv("./ecommerce_orders.csv")

# 1. writing compressed files

df.to_csv("ecommerce_orders_csv.gz", index=False, compression="gzip")
df.to_csv("ecommerce_orders_csv.zip", index=False, compression="zip")

original_size = os.path.getsize("./ecommerce_orders.csv")
print(original_size)
gzip_size = os.path.getsize("./ecommerce_orders_csv.gz")
print(gzip_size)
zip_size = os.path.getsize("./ecommerce_orders_csv.zip")
print(zip_size)


# 2. reading compressed files back

df_from_gzip = pd.read_csv("./ecommerce_orders_csv.gz")
print("Loaded back from .gz file")

df_from_zip = pd.read_csv("./ecommerce_orders_csv.zip")
print("Loaded back from .zip file")


## Parquet file --> column bases binary file format --> large dataset

try: 
    df.to_parquet("ecommerce_orders.parquet", index=False)
    parquet_size = os.path.getsize("./ecommerce_orders.parquet")

    print(f"Parquet file size: {parquet_size} bytes ({parquet_size/original_size*100:.1f} % of original size)")

    df_from_parquet = pd.read_parquet("./ecommerce_orders.parquet")
    print("Loaded back from .parquet file- shape: ", df_from_parquet.shape)

    print(df_from_parquet.dtypes.head(16))

except ImportError:
    print("Parquet support not available. Please install pyarrow or fastparquet.")
