multi_disease_model = MultiDiseaseModel() # return model
multi_disease_model.load_weights(MULTIDISEASEMODEL_WEIGHT_PATH) # load weight
p_extra_input = Input(shape=(11,))
p_concate = concatenate([multi_disease_model.layers[1].output, p_extra_input])
p_dense_1 = Dense(512, activation=LAST_ACTIVATION)(p_concate)
p_dense_2 = Dense(*LABEL_SHAPE, activation=LAST_ACTIVATION)(p_dense_1)
p_model = Model(inputs=[multi_disease_model.input, p_extra_input], outputs=p_dense_2)
p_model.summary()
