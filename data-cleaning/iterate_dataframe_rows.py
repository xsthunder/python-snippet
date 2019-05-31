for index, row in merged_df.iterrows():
    # index, int
    # row, pandas.Series
    level = row.get('level') # dict-lick behavior
    
