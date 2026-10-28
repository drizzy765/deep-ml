import numpy as np

def make_diagonal(x):
	# write a python function to convert a 1d numpy array into a diagonal matrix 
	diag_matrix = np.diag(x)

	return diag_matrix.tolist()