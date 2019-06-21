# use an image decoder
datagen = ImageDataGenerator(
#     rescale=1./255
    preprocessing_function=keras.applications.vgg16.preprocess_input
)
# combine label from vgg16 conv_base
def extract_feature(directory):
    # different class in respective folder
    sub_dir = map(lambda d:join(directory, d), listdir(directory))
    sample_count = reduce(lambda x,y: x + y, map(lambda d:len(listdir(d)), sub_dir))
    features = np.zeros(shape=(sample_count, 4,4,512))
    labels = np.zeros(shape=sample_count)
    batch_size = 20
    datagenerator = datagen.flow_from_directory(
        directory,
        target_size=(150,150),
        batch_size=batch_size, # 一张一张读入?
        class_mode='binary'
    )
    i = 0
    for inputs_batch, labels_batch in datagenerator:
        features_batch = conv_base.predict(inputs_batch) # wherever your model
        features[i * batch_size:((i+1)*batch_size)] = features_batch
        labels[i * batch_size:((i+1)*batch_size)] = labels_batch
        i += 1
        if i * batch_size >=sample_count:break
    return features, labels
train_features, train_labels = extract_feature(train_dir)
validation_features, validation_labels = extract_feature(validation_dir)
test_features, test_labels = extract_feature(test_dir)
