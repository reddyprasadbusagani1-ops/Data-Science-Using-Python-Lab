"""
Experiment 1: Creating a NumPy Array
Course Code: 23A30403 - Data Science Using Python Lab
"""
import numpy as np

def main():
    print("=== Experiment 1: Creating a NumPy Array ===")
    
    # a. Basic ndarray
    arr_basic = np.array([10, 20, 30, 40, 50])
    print("\na. Basic ndarray:")
    print(arr_basic)
    
    # b. Array of zeros
    arr_zeros = np.zeros((3, 3))
    print("\nb. Array of zeros (3x3):")
    print(arr_zeros)
    
    # c. Array of ones
    arr_ones = np.ones((2, 4))
    print("\nc. Array of ones (2x4):")
    print(arr_ones)
    
    # d. Random numbers in ndarray
    arr_random = np.random.rand(3, 2)
    print("\nd. Random numbers (3x2):")
    print(arr_random)
    
    # e. An array of your choice
    arr_custom = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("\ne. Custom 3x3 matrix:")
    print(arr_custom)
    
    # f. Identity matrix (I-matrix)
    arr_identity = np.eye(4)
    print("\nf. Identity matrix (4x4):")
    print(arr_identity)
    
    # g. Evenly spaced ndarray
    arr_spaced = np.arange(10, 50, 5)
    print("\ng. Evenly spaced array (10 to 50, step 5):")
    print(arr_spaced)

if __name__ == "__main__":
    main()
