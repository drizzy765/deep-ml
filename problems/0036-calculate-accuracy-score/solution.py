import numpy as np


def accuracy_score(y_true, y_pred):
	# Your code here
	correct = np.sum(y_true == y_pred)
	return correct/len(y_true)