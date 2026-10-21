import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	# normal equation finds the optimal coefficient of a linear regression in a simple step (a closed form solution) formula 0 = (x-t*x)-1 x-t*y 1. x-t transpose of x, (x-t*x)-1 inverse of transpose of x * x, y = target vector
	
	x = np.array(X)
	y = np.array(y)

	transpose_of_x = np.transpose(x)

    transpose_of_x_multipliedby_x = np.dot(transpose_of_x, x)

	inverse_of_transpose_of_x_multipliedby_x = np.linalg.inv(transpose_of_x_multipliedby_x)

	multiply_transpose_of_x_and_y = np.dot(transpose_of_x, y)

	normal_regression = np.dot(inverse_of_transpose_of_x_multipliedby_x, multiply_transpose_of_x_and_y)

	normal_regression_rounded = np.round(normal_regression, 4)


	return normal_regression_rounded




