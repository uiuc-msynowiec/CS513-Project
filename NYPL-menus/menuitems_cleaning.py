import pandas as pd
import numpy as np

data = pd.read_csv('MenuItem.csv', sep=',')

print(data.head())


data[data.price == np.nan].price = 0

data = data[data.price > 0]

data.to_csv('MenuItem_cleaned.csv', index=True)