'''
https://leetcode.com/problems/sales-analysis-iii/
'''

import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales = sales.groupby('product_id').agg(
        min = ('sale_date', 'min'),
        max = ('sale_date', 'max')).reset_index()
    sales = sales[(sales['min'] >= '2019-01-01') & (sales['max'] <= '2019-03-31')]
    return sales.merge(product, on='product_id')[['product_id','product_name']]