def draw_3_img(img_arr, name_arr=None, level_arr=None, patientID=None):
    fig, m_axs = plt.subplots(1, 3, figsize = (10, 3)) # nrow, ncolumn, @see https://www.kaggle.com/kmader/train-simple-xray-cnn/notebook#Show-a-few-images-and-associated-predictions
    if name_arr == None:
        name_arr = [None for i in range(3)]
    if level_arr == None:
        level_arr = [None for i in range(3)]
    for _img, _title, level, _ax in zip(img_arr, name_arr, level_arr,m_axs.flatten()):
        _ax.imshow(_img)
        _ax.axis('off')
        _ax.set_title('(%s, %s, %s)'%(str(patientID), str(_title), str(level)))
