"""
Experiment 3: Expanding, Squeezing, and Sorting
Course Code: 23A30403 - Data Science Using Python Lab
"""
import numpy as np

def main():
    print("=== Experiment 3: Expanding, Squeezing, and Sorting ===")
    
    # Sample 1D array
    arr = np.array([12, 5, 2, 8, 30, 1])
    print(f"Original 1D Array: {arr}, Shape: {arr.shape}")
    
    # a. Expanding an array using expand_dims()
    expanded_row = np.expand_dims(arr, axis=0)
    print(f"\na. Expanded dims (axis=0) shape: {expanded_row.shape}")
    expanded_col = np.expand_dims(arr, axis=1)
    print(f"   Expanded dims (axis=1) shape: {expanded_col.shape}")
    
    # b. Squeezing using squeeze()
    squeezed = np.squeeze(expanded_col)
    print(f"\nb. Squeezed shape back from {expanded_col.shape} -> {squeezed.shape}")
    
    # c. Sorting NumPy arrays using sort()
    sorted_arr = np.sort(arr)
    print(f"\nc. Sorted Array (Ascending): {sorted_arr}")
    
    # Sorting a 2D array along axes
    matrix = np.array([[9, 2, 7], [4, 1, 8]])
    print(f"\nOriginal 2D Matrix:\n{matrix}")
    print(f"Sorted along columns (axis=0):\n{np.sort(matrix, axis=0)}")
    print(f"Sorted along rows (axis=1):\n{np.sort(matrix, axis=1)}")

if __name__ == "__main__":
    main()
