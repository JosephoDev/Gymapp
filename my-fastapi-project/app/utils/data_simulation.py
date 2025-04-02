import numpy as np

def simulate_data(num_points=100, noise_level=0.1):
    np.random.seed(42)  # For reproducibility
    X = np.random.rand(num_points, 1) * 10  # Random X values between 0 and 10
    true_slope = 2.0
    true_intercept = 1.0
    y = true_slope * X + true_intercept + np.random.normal(0, noise_level, X.shape)  # Linear relation with noise
    return X, y

def generate_dataset(num_samples=100, noise=0.1):
    X, y = simulate_data(num_points=num_samples, noise_level=noise)
    return X, y