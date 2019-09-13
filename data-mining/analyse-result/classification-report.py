from sklearn.metrics import classification_report

# scores, output of models
# y_true

y_pred = scores >= best_threshold

print(metrics.classification_report(y_true=y_true, y_pred=y_pred))

"""
outputs are
              precision    recall  f1-score   support

       False       0.59      0.75      0.66       116
        True       0.91      0.82      0.86       338

   micro avg       0.80      0.80      0.80       454
   macro avg       0.75      0.78      0.76       454
weighted avg       0.82      0.80      0.81       454
"""
