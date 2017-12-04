import pandas as pd 
import numpy as np
import matplotlib as plt

s = pd.Series([1,3,5,np.nan,6,8])

print s

dates = pd.date_range('20130101', periods=6)

print dates

p = pd.Series(['A', 'B', 'C', 'AaBb', 'Baca', np.nan, 'CABA', 'dog', 'cat'])

p.str.lower()

print p

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()

print ts.plot()
