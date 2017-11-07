# Table of Contents
1. [Prerequisites](README.md#Prerequisites)
2. [Aim](README.md#Aim)
3. [How to use](README.md#How-to-use)
4. [Implementation details](README.md#Implementation-details)
5. [Directory structure](README.md#directory-structure)


## Prerequisites

Python 2 and the following packages: numpy, scipy, sklearn, matplotlab

## Aim

Function of proteins greatly depend on their dynamic structural changes, also known as folding process. 
The dynamic protein folding process can be studied using single-molecule force spectrometry. Basically,
this single-molecule method allows us to hold two ends of a single protein molecule. We can apply force 
to unfold the protein by pulling two ends and allow protein to spontaneouly refold by relax two ends. We 
record **force** and **extension** in this process, which tells us the stability and folding status of the protein.
When protein is structured, the distance (**extension**) between two pulling ends are smaller compared to 
unstructured protein.
<img src=https://github.com/JunyiJ/ProteinFoldingClassifier/blob/master/other/Optical_tweezer_figure.png width="32">

In single-molecule force spectrometry study, noise to signal ratio can be very high. In other words, only 30%~50% collected
signals are from protein folding and the rest signals are non-specific signals. Manually going through the signals can be
time consuming. Here I present a machine-learning based approach to identify protein folding signals from non-signals.

The following figure shows the difference of protein folding signals from nonspecific signals: 

<img src=https://github.com/JunyiJ/ProteinFoldingClassifier/blob/master/other/SNARE_sig_nosig_10ms.png >


I implemented and evaluated several different classifiers, including logistic regression, k-nearest neighbors and SVM,
based on recall of test and ROC curves. SVM usually has the best performance under different conditions. 
This may result from the high-dimension feature space of my input data.

## How to use

1. To use logistic regression, use command `python logistic_regression.py \path\to\data\`
2. To use k nearest neighbors classifier , use command `python KNN.py \path\to\data\`
3. To use k nearest neighbors classifier with principle component analysis (PCA), use command `python PCA_KNN.py \path\to\data`
4. To use SVM classifer, use the command `python SVM.py \path\to\data`
5. Two matlab scripts were used to extract features from the raw matlab data files.



## Implementation details

Cross validation were used to select key paremeters or hyper paremeters. For example k in KNN and C in SVM. 
Usually a ROC curve was generated using cross validation to give you a sense of your classifier.
The programs will also print out the predicted results for your test cases. 


The following figures shows a ROC example of using SVM to classify protein folding signals.

<img src=https://github.com/JunyiJ/ProteinFoldingClassifier/blob/master/other/ROC_SVM.png>



## Directory-structure
Put your training_positive data in path: `data/training_sig`
Put your training_neg data in path: `data/training_nonsig`
Put your test_positive data in path: `data/test_sig`
Put your test_neg data in path: `data/test_nonsig`

The directory structure should look like this:

    ├── README.md 
    ├── KNN.py
    ├── logistic_regression.py
    ├── PCA_KNN.py
    ├── SVM.py
    ├── data_process.py
    ├── roc.py
    ├── get_region.m
	├── process.m
    ├── data
    |   └── training_nonsig
	|		└── your_own_training_data_neg
    |   └── training_sig
	|		└── your_own_training_data_pos
    |   └── test_nonsig
	|		└── your_own_test_data_neg
    |   └── test_nonsig
	|		└── your_own_test_data_pos
	├── others

	