import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	T = np.array(T)
	A = np.array(A)
	S = np.array(S)
	# FIND T-1AS
	if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
		return -1
    # find the inverse of T
	inv_T = np.linalg.inv(T)

	#DOT PRODUCT
	dot_product_of_invT_and_A = np.dot(inv_T, A)

	# FINAL SOLUTION T-1AS
	final = np.dot(dot_product_of_invT_and_A, S)

    return final.tolist()


	    