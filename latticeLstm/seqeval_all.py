import sys
import os
import json
import pandas as pd
import seqeval
from seqeval.metrics import recall_score
from seqeval.metrics import classification_report
from seqeval.metrics import f1_score
from seqeval.metrics import precision_score

# TODO 
# check argv length

filename = sys.argv[1]

def run(filename):
	print('------------------       %s      ---------------'%filename)
	with open(filename, 'r') as f:
	    obj = json.load(f)


	y_true=obj['gold_results']
	y_pred=obj['pred_results']

	pre = precision_score(y_true, y_pred)
	rec = recall_score(y_true, y_pred)
	f1 = f1_score(y_true, y_pred)

	df = pd.DataFrame({'percision':[pre], 'recall':[rec], 'f1':[f1]})
	print(df)

	report = classification_report(y_true, y_pred)
	print(report)


run(filename)
