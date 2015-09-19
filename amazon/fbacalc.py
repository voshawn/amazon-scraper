import pandas as pd
import numpy as np

df = pd.read_csv('test.csv', dtype=object)

df['dimensions']= df['dimensions'].astype(str)

i = 0
for x in df['dimensions']:
	df.x[i] = x.count("x")
	i = i + 1



print(df.x)

