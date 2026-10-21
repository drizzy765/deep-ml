import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# convert x to numpy array
	x = np.array(vectors)
    # number of observation per feature
	shape = x.shape[1]
    # find mean across columns
	means = np.mean(x, axis=1, keepdims=True)
    # find the deviation of mean
	deviation = x - means
    # formula for covariance search the internet i aint typing it
	cov = np.dot(deviation, deviation.T) / (shape - 1)


	return cov.tolist()