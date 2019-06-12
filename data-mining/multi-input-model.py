# https://www.kaggle.com/kmader/train-simple-xray-cnn/notebook#Create-a-simple-model
# you must maintain the original model architecture to load pretrain network
from keras.applications.mobilenet import MobileNet
from keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from keras.models import Sequential
def MultiDiseaseModel(): # do NOT change this, 
    base_mobilenet_model = MobileNet(
        
        input_shape = (128, 128, 1), # IMG_SIZE=(128,128), color_mode='gray' #t_x.shape[1:], 
#         input_shape =  INPUT_SHAPE,
        
         include_top = False, weights = None)
    multi_disease_model = Sequential()
    multi_disease_model.add(base_mobilenet_model)
    multi_disease_model.add(GlobalAveragePooling2D())
    multi_disease_model.add(Dropout(0.1))
    multi_disease_model.add(Dense(512))
    multi_disease_model.add(Dropout(0.1))
    multi_disease_model.add(Dense(
        
#         LABEL_SHAPE[0], 
        13, #len(all_labels), # use the pretrained model's output dimenseion in order to load the weight, we won't use this layer
        
        activation = LAST_ACTIVATION))
    # no need to compile
    return multi_disease_model


multi_disease_model = MultiDiseaseModel() # can be any model, including Sequential(). In this case a img decoder.
multi_disease_model.load_weights(MULTIDISEASEMODEL_WEIGHT_PATH) # load weight
p_extra_input = Input(shape=(11,))
p_concate = concatenate([multi_disease_model.layers[1].output, p_extra_input]) # take conv base only, leave out dense layers.
p_dense_1 = Dense(512, activation=LAST_ACTIVATION)(p_concate)
p_dense_2 = Dense(*LABEL_SHAPE, activation=LAST_ACTIVATION)(p_dense_1)
p_model = Model(inputs=[multi_disease_model.input, p_extra_input], outputs=p_dense_2)
p_model.summary()

