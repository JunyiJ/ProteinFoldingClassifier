from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
from sklearn.metrics import average_precision_score

def draw_precision_recall(classifier, test_X, test_Y, figname):	
	y_score = classifier.decision_function(test_X)
	precision, recall, _ = precision_recall_curve(test_Y, y_score)
	average_precision = average_precision_score(test_Y, y_score)
	print(average_precision)
	fig = plt.gcf()
	plt.step(recall, precision, color='K', alpha=0.2, where='post')
	plt.fill_between(recall, precision, step='post', alpha=0.2, color='b')
	plt.xlabel('Recall')
	plt.ylabel('Precision')
	plt.ylim([0.0, 1.05])
	plt.xlim([0.0, 1.0])
	title = figname.split("\\")[-1]
	plt.title(title + ' Precision_Recall: average_precision = %f' %(average_precision))
	plt.show()
	fig.savefig(figname)	