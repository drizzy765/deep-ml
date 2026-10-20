import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

              A = np.array(a)
              B = np.array(b)
              # the rule for matrix addition, not multiplication. For a dot product, the number of columns in the first matrix must equal the number of rows in the second matrix
              if A.shape[1] != B.shape[0]:
                return -1
              c = np.dot(A,B)
              # convert array back to list
	          return c.tolist()