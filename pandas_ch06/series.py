import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}
pd.Series(data=my_data)
pd.Series(data=my_data, index=labels)
pd.Series(d)
ser1 = pd.Series([1,2,3,4], [
    'USA',
    'Germany',
    'USSR',
    'Japan',
])

ser2 = pd.Series([1,2,5,4], [
    'USA',
    'Germany',
    'Italy',
    'Japan',
])
