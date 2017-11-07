import os
from os.path import abspath, dirname, join
import numpy as np
import scipy.io as sio
from sklearn import preprocessing

def data_process(paths):
	#Read and preprocess data from paths=[path1,path2]
	#path1: path storing class0 data (non-protein data)
	#path2: path storing class1 data (protein folding data)
	train_X = np.array([], dtype=np.float32, order='C')
	train_Y = []
	train_size = 0
	sig_start = 0
	# Read from 
	for i in range(2):
		for file in os.listdir(paths[i]):
			if file.endswith(".mat"):
				train_size += 1
				file = join(paths[i], file)
				matdata = sio.loadmat(file)
				n = matdata['EXT_FORCE'].size
				flatten_matdata = matdata['EXT_FORCE'].reshape((-1,n))
				train_Y.append(i)
				if not sig_start:
					train_X = flatten_matdata					
					sig_start = 1
				else:
					train_X = np.append(train_X,flatten_matdata,axis=0)
	#normalize the data
	train_X = preprocessing.scale(train_X)
	#reshape train_Y
	train_Y = np.asarray(train_Y, dtype=np.float64, order='C').reshape((train_size,-1))
	train_Y = train_Y.reshape(train_size,)
	return train_X, train_Y