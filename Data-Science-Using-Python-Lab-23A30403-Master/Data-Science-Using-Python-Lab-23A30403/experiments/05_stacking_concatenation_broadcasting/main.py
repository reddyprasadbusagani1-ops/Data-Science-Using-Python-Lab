"""
Experiment 5: Stacking, Concatenation, and Broadcasting
Course Code: 23A30403 - Data Science Using Python Lab
"""
import numpy as np

def main():
    print("=== Experiment 5: Stacking, Concatenation, and Broadcasting ===")
    
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    
    # a. Vertical and Horizontal Stacking
    print("a. Stacking:")
    print(f"Vertical Stack (vstack):\n{np.vstack((a, b))}")
    print(f"Horizontal Stack (hstack): {np.hstack((a, b))}")
    
    # b. Array Concatenation
    m1 = np.array([[1, 2], [3, 4]])
    m2 = np.array([[5, 6], [7, 8]])
    print(f"\nb. Concatenation along axis 0:\n{np.concatenate((m1, m2), axis=0)}")
    print(f"   Concatenation along axis 1:\n{np.concatenate((m1, m2), axis=1)}")
    
    # c. Broadcasting
    matrix = np.array([[10, 20, 30], [40, 50, 60]])
    scalar = 5
    vector = np.array([1, 2, 3])
    
    print(f"\nc. Broadcasting Matrix + Scalar (5):\n{matrix + scalar}")
    print(f"   Broadcasting Matrix (2x3) + Vector (1x3):\n{matrix + vector}")

if __name__ == "__main__":
    main()
