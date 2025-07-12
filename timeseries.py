import numpy as np
import pandas as pd

data_rng =pd.date_range(start='2024-01-01',periods=10,freq='D')

df = pd.DataFrame(data_rng, columns=['Date'])

df['data'] = np.random.randint(0,100,size=(10))

df.set_index('date',inplace=True)

resampled = df.resample('3D').mean()
print("\nResampled Data:\n",resampled)

df['rolling_mean'] = df['data'].rolling(window=3).mean()
print("\n Data with ROlling Mean:\n",df)