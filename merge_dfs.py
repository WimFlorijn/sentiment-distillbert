import pandas as pd

df_names = [
    'ALL-DATA-OUTS-0.csv',
    'ALL-DATA-OUTS-1.csv',
    'ALL-DATA-OUTS-2.csv',
    'ALL-DATA-OUTS-3.csv',
    'ALL-DATA-OUTS-4.csv',
]

dfs = list(map(lambda x: pd.read_csv('processed/' + x, delimiter='\t'), df_names))
df_concat = pd.concat(dfs, ignore_index=True)

df_concat.to_csv('ALL-DATA-PROCESSED.csv', sep='\t', index=False)
