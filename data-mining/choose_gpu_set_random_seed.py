GPU_ID = "1" # start from 0
TF_SEED_NUMBER = 1000
NP_SEED_NUMBER = TF_SEED_NUMBER # performance may still changes
GPU_MEMORY_FRACTION = 0.3 #进行配置，使用30%的GPU

import os
import random

import numpy as np
from numpy.random import seed
seed(NP_SEED_NUMBER)
from tensorflow.random import set_random_seed
set_random_seed(TF_SEED_NUMBER)

import keras
import keras.backend as K
import tensorflow as tf
import keras.backend.tensorflow_backend as KTF

os.environ["CUDA_VISIBLE_DEVICES"] = GPU_ID
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction =  GPU_MEMORY_FRACTION
session = tf.Session(config=config)

# 设置session
KTF.set_session(session )
