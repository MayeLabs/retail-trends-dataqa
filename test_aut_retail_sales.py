import pytest
import pandas as pd

sales_automated = pd.read_csv("retail_sales_for_automated.csv", index_col=0)

print(sales_automated)

# QC001
def test_missing_values():
    assert sales_automated['product_id'].notnull().all(), f"Null Values: product_id"
    assert sales_automated['date'].notnull().all(), f"Null Values: sales_automated"
    assert sales_automated['sales_revenue_usd'].notnull().all(), f"Null Values: sales_revenue_usd"


# QC002 - QC003 - QC005 
@pytest.mark.parametrize("column", ['units_sold', 'sales_revenue_usd', 'marketing_spend_usd'])
def test_non_negative(column):
    assert (sales_automated[column] >= 0).all(), f"Exist values < 0 in {column}"

# QC004
@pytest.mark.parametrize("column", ['discount_percentage'])
def test_range_percentage():
    assert(sales_automated[column] >= 0 and sales_automated[column] <= 100).all(), f"Percentage Invalid in {column}"