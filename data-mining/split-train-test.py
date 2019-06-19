from sklearn.model_selection import train_test_split
train_img_X,test_img_X, train_extra_X, test_extra_X, train_label,  test_label, = train_test_split(
                                     img_feature,
                                    extra_feature,
                                     labels,
                                   test_size = 0.3, 
                                   random_state = 2018,
                                   stratify = df['level']
                                    )
