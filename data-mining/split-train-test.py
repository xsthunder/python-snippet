y_column_name = '0,1~5'
SKLEAN_RAMDOM_SEED=20190619
from sklearn.model_selection import train_test_split
df = df_all.copy()
train_df, test_df = train_test_split(
                                    df,
                                   test_size = 0.3, 
                                   random_state = SKLEAN_RAMDOM_SEED,
                                   stratify = df[y_column_name]
                                    )
