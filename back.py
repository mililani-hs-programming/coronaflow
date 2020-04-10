import numpy as np
import pandas as pd

data = {'Dates': [1,2,3,4]}
a = pd.DataFrame(data=data)

def df_date_to_unix(df, column_name='Dates'):
    assert type(df) == type(pd.DataFrame())
    str_dates = df[column_name]
    print(str_dates)
    
df_date_to_unix(a)
