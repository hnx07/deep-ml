import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a = matrix[0][0];
	b = matrix[0][1];
	c = matrix[1][0];
	d = matrix[1][1];
	temp = [1, -a - d, a*d - c*b];
	eigenvalues = np.roots(temp);
	return eigenvalues