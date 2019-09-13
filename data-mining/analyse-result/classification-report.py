from sklearn.metrics import classification_report

# scores, output of models
# y_true

y_pred = scores >= best_threshold # roc_curve is using threshold with greater or equal to

print(metrics.classification_report(y_true=y_true, y_pred=y_pred))

"""
outputs are
              precision    recall  f1-score   support

       False       0.59      0.75      0.66       116
        True       0.91      0.82      0.86       338

   micro avg       0.80      0.80      0.80       454
   macro avg       0.75      0.78      0.76       454
weighted avg       0.82      0.80      0.81       454

              precision    recall  f1-score   support

       False       查准      查全      0.66       116
        True       查准      查全      0.86       338

   micro avg       0.80      0.80      0.80       454
   macro avg       0.75      0.78      0.76       454
weighted avg       0.82      0.80      0.81       454

sensitivity = 正类的查率率
specifity = 负类的查全率
"""
