import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	A = np.array(A)
	B = np.array(b)

	# extract the diagonal values and create the remainder matrix
	diagonal = np.diag(A)
    R = A - np.diagflat(diagonal)

	# Initialize the solution vector x to all zeros
    x = np.zeros(len(b))
    
    # Perform the Jacobi iterations exactly n times
    for _ in range(n):
        x = (B - np.dot(R, x)) / diagonal
        
    # Round only the final result to 4 decimal places and convert to a list
    return np.round(x, 4).tolist()

	return x