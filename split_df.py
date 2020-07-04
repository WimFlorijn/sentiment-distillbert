import pandas as pd


review_df = pd.read_csv('ALL-DATA-OUT.csv', delimiter='\t')

i = 0
b_size = 500 * 1000
count = len(review_df)

start = i * b_size
stop = start + b_size

while start < count:
    batch = review_df.iloc[start:stop]
    batch.to_csv('batches/ALL-DATA-OUT-{i}.csv'.format(i=i), sep='\t', index=False)

    i += 1
    start = i * b_size
    stop = start + b_size
