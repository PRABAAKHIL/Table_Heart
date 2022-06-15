import pandas as pd

df1=pd.read_csv('heart_2020_cleaned.csv')
df1.head()

chunk_size=79949

batch_no=1



for chunk in pd.read_csv('heart_2020_cleaned.csv',chunksize=chunk_size):

  chunk.to_csv('heart_2020_cleaned.csv' + str(batch_no) + '.csv', index=False)

  batch_no +=1