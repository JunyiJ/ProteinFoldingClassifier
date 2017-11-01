#Using SVM to do classification
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
import numpy as np
import scipy.io as sio
import os
from sklearn import preprocessing
from sklearn.metrics import roc_curve, auc
from scipy import interp
from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold
from os.path import abspath, dirname, join
from data_process import data_process
from roc import draw_ROC
import sys

def cross_validation_C(train_X, train_Y, C, figname):
	#find the best k value from neighbors using cross validation	
	cv_scores = []
	for c in C:
		classifier = svm.SVC(C=c, cache_size=400)
		scores = cross_val_score(classifier, train_X, train_Y, cv=6, scoring='recall')
		cv_scores.append(scores.mean())
	print (C)
	print (cv_scores)
	# plot neighbor~recall
	fig = plt.gcf()
	plt.plot(C, cv_scores)
	plt.xlabel('Hyperpar C')
	plt.ylabel('Recall')
	plt.show()
	fig.savefig(figname)
	# find top C value for classifier
	maxscore,goodC = 0, 1
	for i in range(len(C)):
		if cv_scores[i] > maxscore+0.01:
			maxscore = cv_scores[i]
			goodC = C[i]
	return goodC
	
def cross_validation_gamma(train_X, train_Y, goodC, gamma_powerange, figname):
	#find the best k value from neighbors using cross validation	
	gamma = [ pow(0.1, i) for i in gamma_powerange ]
	cv_scores = []
	for g in gamma:
		classifier = svm.SVC(C=goodC, gamma=g, cache_size=400)
		scores = cross_val_score(classifier, train_X, train_Y, cv=6, scoring='recall')
		cv_scores.append(scores.mean())
	print (gamma)
	print (cv_scores)
	# plot neighbor~recall
	fig = plt.gcf()
	plt.plot(gamma_powerange, cv_scores)
	plt.xlabel('gamma_power')
	plt.ylabel('Recall')
	plt.show()
	fig.savefig(figname)
	# find top C value for classifier
	maxscore,goodgamma = 0, 0.000001
	for i in range(len(gamma)):
		if cv_scores[i] > maxscore+0.01:
			maxscore = cv_scores[i]
			goodgamma = gamma[i]
	return goodgamma
	

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

		train_X,train_Y = data_process([train_neg,train_pos])
		test_X,test_Y = data_process([test_neg,test_pos])

		 
		C = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0, 8.0]
		goodC = cross_validation_C(train_X, train_Y, C, join(data_path, "CV_SVM_C.png"))
		#print goodC
		gamma_powerange = [x for x in range(2,12)]		
		goodgamma = cross_validation_gamma(train_X, train_Y, goodC, gamma_powerange, join(data_path, "CV_SVM_gamma.png"))

		classifier = svm.SVC(C=goodC, gamma=goodgamma, cache_size=400)
		classifier.fit(train_X, train_Y)
		predicted = classifier.predict(test_X)
		print predicted
		print test_Y
		print("Classification report for classifier %s:\n%s\n" % (classifier, metrics.classification_report(test_Y, predicted)))
		classifier = svm.SVC(probability=True, cache_size=400, C=goodC, gamma=goodgamma)
		draw_ROC(train_X, train_Y, classifier, join(data_path,"ROC_SVM.png"))


