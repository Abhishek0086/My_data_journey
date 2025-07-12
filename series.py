import pandas as pd

s = pd.Series([10,20,30], index = ['a','b','c'])

print(s)

df = pd.DataFrame(s,columns = ['values'])

print(df)