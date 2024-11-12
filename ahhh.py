import pandas as pd
import tables

df = pd.read_hdf('data.h5')
print(df)