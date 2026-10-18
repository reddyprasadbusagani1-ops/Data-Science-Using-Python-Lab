"""
Experiment 4: Indexing and Slicing
Course Code: 23A30403 - Data Science Using Python Lab
"""
import numpy as np

def main():
    print("=== Experiment 4: Indexing and Slicing ===")
    
    # a. Slicing 1D array
    arr_1d = np.array([10, 20, 30, 40, 50, 60, 70, 80])
    print(f"1D Array: {arr_1d}")
    print(f"Slice [2:6]: {arr_1d[2:6]}")
    
    # b. Slicing 2D array
    arr_2d = np.array([
        [10, 11, 12, 13],
        [20, 21, 22, 23],
        [30, 31, 32, 33]
    ])
    print(f"\n2D Array:\n{arr_2d}")
    print(f"Sub-matrix (Rows 0-1, Cols 1-2):\n{arr_2d[0:2, 1:3]}")
    
    # c. Slicing 3D array
    arr_3d = np.arange(1, 13).reshape(2, 2, 3)
    print(f"\n3D Array:\n{arr_3d}")
    print(f"Slice First Block:\n{arr_3d[0, :, :]}")
    
    # d. Negative slicing & reverse
    print(f"\nd. Negative slicing on 1D (Last 3 elements): {arr_1d[-3:]}")
    print(f"   Reversed 1D Array: {arr_1d[::-1]}")

if __name__ == "__main__":
    main()
