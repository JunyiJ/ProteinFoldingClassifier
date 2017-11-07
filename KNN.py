#Using KNN to do classification
#Using cross validation to choose a k value
import matplotlib.pyplot as plt
from sklearn import datasets, metrics, preprocessing
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import scipy.io as sio
import sys, os
from sklearn.metrics import roc_curve, auc
from scipy import interp
from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold
from multiprocessing import Pool
from os.path import abspath,dirname,join
from data_process import data_process
from roc import draw_ROC


def cross_validation_k(train_X, train_Y, neighbors, figname):
	#find the best k value from neighbors using cross validation
	
	cv_scores=[]
	for neighbor in neighbors:
		classifier = KNeighborsClassifier(n_neighbors=neighbor)
		scores = cross_val_score(classifier, train_X, train_Y, cv=6, scoring='recall')
		cv_scores.append(scores.mean())
	print (neighbors)
	print (cv_scores)
	# plot neighbor~recall
	fig=plt.gcf()
	plt.plot(neighbors, cv_scores)
	plt.xlabel('Number of Neighbors K')
	plt.ylabel('Recall')
	plt.show()
	fig.savefig(figname)
	# find top k value for classifier
	maxscore,goodneighbor = 0, 1
	for i in range(len(neighbors)):
		if cv_scores[i] > maxscore:
			maxscore = cv_scores[i]
			goodneighbor = neighbors[i]
	return goodneighbor
	
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
		#Using cross validation to get a good k value
		neighbors = [x for x in range(1,15,2)]
		goodneighbor = cross_validation_k(train_X, train_Y, neighbors, join(data_path, "CV_KNN_k"))
		
		#train the model with selected K value
		KNN = KNeighborsClassifier(n_neighbors=goodneighbor)
		KNN.fit(train_X, train_Y)	
		predicted=KNN.predict(test_X)
		print "predicted result using neighbor=%d:\n" %(goodneighbor),predicted
		print "expected results\n",test_Y.flatten("C")
		print("Classification report for classifier %s:\n%s\n" % (KNN, metrics.classification_report(test_Y, predicted)))
		draw_ROC(train_X, train_Y, KNN, join(data_path, "ROC_KNN"))


