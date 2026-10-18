"""
Experiment 2: Shape and Reshaping of NumPy Arrays
Course Code: 23A30403 - Data Science Using Python Lab
"""
import numpy as np

def main():
    print("=== Experiment 2: Shape and Reshaping of NumPy Arrays ===")
    
    # Create sample array
    arr = np.arange(1, 13)
    print(f"Original Array:\n{arr}")
    
    # a. Dimensions using ndim
    print(f"\na. Dimensions (ndim): {arr.ndim}")
    
    # b. Shape using shape
    print(f"b. Shape (shape): {arr.shape}")
    
    # c. Size using size
    print(f"c. Total elements (size): {arr.size}")
    
    # d. Reshaping using reshape()
    reshaped_2d = arr.reshape(3, 4)
    print(f"\nd. Reshaped to 3x4 Matrix:\n{reshaped_2d}")
    print(f"   New Shape: {reshaped_2d.shape}, New ndim: {reshaped_2d.ndim}")
    
    # e. Flattening using flatten()
    flattened = reshaped_2d.flatten()
    print(f"\ne. Flattened Array:\n{flattened}")
    
    # f. Transpose using .T or transpose()
    transposed = reshaped_2d.T
    print(f"\nf. Transposed Matrix (4x3):\n{transposed}")

if __name__ == "__main__":
    main()
