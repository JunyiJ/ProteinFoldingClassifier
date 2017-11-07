#Using logistic regression to do classification
#Using cross validation to choose a k value
import matplotlib.pyplot as plt
from sklearn import datasets, metrics, preprocessing
import numpy as np
import scipy.io as sio
import sys, os
from sklearn.metrics import roc_curve, auc
from scipy import interp
from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold
from multiprocessing import Pool
from os.path import abspath,dirname,join
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from data_process import data_process
from roc import draw_ROC
from precision_recall import draw_precision_recall

	

if __name__=="__main__":	
	#preprocess data (multiprocess training data and test data)
	n = len(sys.argv)
	if n != 2:
		print n
		print "Not enough args, please input paths of train_neg,train_pos,test_neg,test_pos"
	else:
		root = dirname(abspath(__file__))
		data_path = join(root,sys.argv[1])
		print data_path
		train_pos = join(data_path,"trainning_sig/")
		train_neg = join(data_path,"trainning_nonsig/")
		test_pos = join(data_path,"test_sig/")
		test_neg = join(data_path,"test_nonsig/")
		train_X,train_Y = data_process([train_neg, train_pos])
		test_X,test_Y = data_process([test_neg, test_pos])
		#Using PCA to transform the data
		logistic = LogisticRegression(penalty='l1')		
		logistic.fit(train_X, train_Y)	
		predicted = logistic.predict(test_X)
		draw_precision_recall(logistic, test_X, test_Y, join(data_path, "PR_Logistic_l1"))
		print "predicted result",predicted
		print "expected results\n",test_Y.flatten("C")
		print("Classification report for classifier %s:\n%s\n" % (logistic, metrics.classification_report(test_Y, predicted)))
		draw_ROC(train_X, train_Y, logistic, join(data_path, "ROC_logistic_l1"))
		


