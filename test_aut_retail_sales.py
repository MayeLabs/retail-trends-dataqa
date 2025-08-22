import pytest
import pandas as pd

sales_automated = pd.read_csv("retail_sales_for_automated.csv", index_col=0)

print(sales_automated)

# QC001
def test_missing_values():
    assert sales_automated['product_id'].notnull().all(), f"Null Values: product_id"
    assert sales_automated['date'].notnull().all(), f"Null Values: sales_automated"
    assert sales_automated['sales_revenue_usd'].notnull().all(), f"Null Values: sales_revenue_usd"
