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
def test_range_percentage(column):
    assert sales_automated[column].between(0,100).all(), f"Percentage Invalid in {column}"

# QC006
def test_valid_day_week():
    valid_day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    assert sales_automated['day_of_week'].str.lower().isin(valid_day).all(), "Day of week invalid"
# QC007
def test_valid_holiday_boolean():
    assert sales_automated['holiday_effect'].isin([True, False]).all(), "Invalid holiday_effect"

# QC008
def test_unique_combination():
    subset_col =  ['store_id', 'product_id', 'date']
    assert sales_automated.reset_index().duplicated(subset=subset_col).sum() == 0, f"Existe rows duplicated in {subset_col}"

# QC009
def test_notnull_notempty():
    invalid = sales_automated['store_location'].isnull() | (sales_automated['store_location'].str.strip() == '')
    assert not invalid.any(), "There is null or empty"