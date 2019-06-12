from keras.utils import multi_gpu_model


#
pretrain_filepath = "regession-pretrain-{epoch:02d}-{val_loss:.2f}.hdf5"
from keras.callbacks import Callback
class mutiGPUSaver(Callback):
    def __init__(self, model):
        self.model_to_save = model
    def on_epoch_end(self,epoch,logs=None):
        self.model_to_save.save('pretrain_%s.hdf5'%epoch)

    
pretrain_filepath = "regession-pretrain-{epoch:02d}-{val_loss:.2f}.hdf5"
from keras.callbacks import Callback
class mutiGPUSaver(Callback): # need to have your OWN saver
    def __init__(self, model):
        self.model_to_save = model
    def on_epoch_end(self,epoch,logs=None):
        self.model_to_save.save('pretrain_%s.hdf5'%epoch)
        
pretrain_checkpoint = mutiGPUSaver(p_model)

p_parallel_model = multi_gpu_model(p_model, gpus=2) # do NOT specify gpu in global keras setting
p_parallel_model.summary()

# 预训练
p_parallel_model.layers[0].trainable=False
p_parallel_model.compile(optimizer = OPTIMIZER, loss = LOSS_FUNC_NAME ,metrics = METRICS)
p_parallel_model_history = p_parallel_model.fit(
[train_img_X, train_extra_X],
 train_label,
validation_data=[[test_img_X, test_extra_X], test_label],
epochs=10,
batch_size=len(train_extra_X),
)

p_parallel_model.layers[0].trainable=True
p_parallel_model.compile(optimizer = OPTIMIZER, loss = LOSS_FUNC_NAME ,metrics = METRICS)
p_parallel_model_history = p_parallel_model.fit(
[train_img_X, train_extra_X],
 train_label,
validation_data=[[test_img_X, test_extra_X], test_label],
epochs=40,
batch_size=len(train_extra_X),
    callbacks=[pretrain_checkpoint]
)
