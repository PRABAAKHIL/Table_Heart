import pandas as pd

csv_file=r'/content/heart_2020_cleaned.csv4.csv'
viki_df=pd.read_csv(csv_file)

jason_output = r'/content/viki_loc.json'
output = viki_df.to_json(jason_output, indent = 1,orient='records' )