import pandas as pd

# read csv
df = pd.read_csv('datafile.csv')

# group data by 'Area' and loop the data
for area,group in df.groupby(['Area']):
    print(area)
    # create new csv based on grouped data
    group.to_csv(f'datafile_{area}.csv')

for state,group in df.groupby(['State/UT']):
    group.to_csv(f'data_file_{state}.csv')