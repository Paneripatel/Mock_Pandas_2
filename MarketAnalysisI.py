'''
https://leetcode.com/problems/market-analysis-i/description/
'''

import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders = orders[(orders['order_date']>= '2019-01-01') & (orders['order_date']<'2020-01-01')][['order_id', 'buyer_id']]
    orders = orders.groupby('buyer_id').count().reset_index()

    df = users.merge(orders, how='left', left_on='user_id', right_on='buyer_id').rename(columns={'order_id':'orders_in_2019'})
    df = df[['user_id', 'join_date', 'orders_in_2019']].rename(columns={'user_id':'buyer_id'})
    return df.fillna(0)

