"""
Experiment 6: Pandas DataFrame Operations
Course Code: 23A30403 - Data Science Using Python Lab
"""
import pandas as pd

def main():
    print("=== Experiment 6: Pandas DataFrame Operations ===")
    
    # a. Creating DataFrames
    df1 = pd.DataFrame({
        'StudentID': [101, 102, 103],
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Department': ['CSE', 'ECE', 'CSE'],
        'Marks': [85, 78, 92]
    })
    
    df2 = pd.DataFrame({
        'StudentID': [104, 105],
        'Name': ['David', 'Eva'],
        'Department': ['EEE', 'CSE'],
        'Marks': [64, 88]
    })
    
    print("Initial DataFrame 1:")
    print(df1)
    
    # b. concat()
    combined_df = pd.concat([df1, df2], ignore_index=True)
    print("\nb. Combined DataFrame using concat():")
    print(combined_df)
    
    # c. Filtering records using conditions
    high_scorers = combined_df[combined_df['Marks'] >= 80]
    print("\nc. Filtered Students with Marks >= 80:")
    print(high_scorers)
    
    # d. Adding a new column
    combined_df['Grade'] = ['A', 'B+', 'A+', 'C', 'A']
    print("\nd. DataFrame after adding 'Grade' column:")
    print(combined_df)

if __name__ == "__main__":
    main()
