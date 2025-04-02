import numpy as np

class LinearRegression:
    def __init__(self):
        self.coefficients = None

    def fit(self, X, y):
        X_b = self._add_bias(X)
        self.coefficients = self._calculate_coefficients(X_b, y)

    def predict(self, X):
        X = np.array(X).reshape(-1, 1)  # Ensure X is a 2D array
        X_b = self._add_bias(X)
        return X_b.dot(self.coefficients)

    def _add_bias(self, X):
        return np.c_[np.ones((X.shape[0], 1)), X]

    def _calculate_coefficients(self, X, y):
        return np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)