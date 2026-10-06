import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	temp = [1, -np.trace(matrix), np.linalg.det(matrix)];
	eigenvalues = np.roots(temp);
	return eigenvalues