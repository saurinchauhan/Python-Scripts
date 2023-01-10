import pandas as pd

df = pd.read_csv('datafile.csv')

for area,group in df.groupby(['Area']):
    print(area)
    group.to_csv(f'datafile_{area}.csv')

for state,group in df.groupby(['State/UT']):
    group.to_csv(f'data_file_{state}.csv')