from keras.preprocessing import image
import cv2
import matplotlib.pyplot as plt

# see https://github.com/fchollet/deep-learning-with-python-notebooks/blob/master/5.4-visualizing-what-convnets-learn.ipynb

# keep the same loading image setting
# grayscale
# 1./255

# img_path = '../../../../input-image-dmsa2vur/0/2017--296_0_right.jpg'
# img_file_name='2018--296_0_left.jpg' # <>.jpg
# img_file_name='2018--296_3_right.jpg' # <>.jpg
# img_file_name='2017--296_2_left.jpg' # <>.jpg
img_file_name='2018--296_0_left.jpg' # <>.jpg
img_name=img_file_name.split('.')[0]
img = image.load_img(img_file_name, grayscale=True, target_size=INPUT_SHAPE[:2])
img

x = image.img_to_array(img)
x = x.reshape((1, *x.shape))
x *= 1./255
preds = good_naive.predict(x)
good_naive_output = good_naive.output[:,0]

last_conv_layer_name = 'conv2d_6' # name for the last conv layer. May change from time to time.
last_conv_layer = good_naive.get_layer(last_conv_layer_name)
import keras.backend as K
grads = K.gradients(good_naive_output, last_conv_layer.output)[0]

pooled_grads = K.mean(grads, axis=(0,1,2))
pooled_grads.shape[0].value


iterate = K.function([good_naive.input],
                    [pooled_grads, last_conv_layer.output[0]])
pooled_grads_value, conv_layer_output_value = iterate([x])
for i in range(pooled_grads.shape[0].value):
    conv_layer_output_value[:, :, i] *= pooled_grads_value[i]
heatmap = np.mean(conv_layer_output_value, axis = -1)
heatmap = np.maximum(heatmap, 0)
heatmap /= np.max(heatmap)
plt.matshow(heatmap) # CHECK the CAM heatmap

cv_img = cv2.imread(img_file_name)
heatmap = cv2.resize(heatmap, (cv_img.shape[1], cv_img.shape[0]))
heatmap = np.uint8(255 * heatmap)
heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
superimposed_img =heatmap * 0.1 + cv_img # CHANGE this factor to have maxiumn visual effect
cv2.imwrite('%s-cam.jpg'%img_name, superimposed_img)
