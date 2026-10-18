"""
Experiment 7: Missing Values, Sorting, and Grouping
Course Code: 23A30403 - Data Science Using Python Lab
"""
import pandas as pd
import numpy as np

def main():
    print("=== Experiment 7: Missing Values, Sorting, and Grouping ===")
    
    # Sample DataFrame with missing values
    data = {
        'StudentID': [101, 102, 103, 104, 105, 106],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
        'Department': ['CSE', 'ECE', 'CSE', 'ECE', 'CSE', 'EEE'],
        'Marks': [85, np.nan, 92, 64, np.nan, 55],
        'City': ['Hyderabad', 'Bangalore', np.nan, 'Hyderabad', 'Chennai', 'Bangalore']
    }
    df = pd.DataFrame(data)
    print("Original DataFrame with Missing Values:")
    print(df)
    
    # a. Filling NaN values
    df_filled = df.copy()
    df_filled['Marks'] = df_filled['Marks'].fillna(df_filled['Marks'].mean())
    df_filled['City'] = df_filled['City'].fillna("Unknown")
    print("\na. DataFrame after Filling Missing Values:")
    print(df_filled)
    
    # b. Sorting by column values
    sorted_df = df_filled.sort_values(by='Marks', ascending=False)
    print("\nb. DataFrame Sorted by Marks (Descending):")
    print(sorted_df)
    
    # c. Grouping with groupby()
    grouped = df_filled.groupby('Department')['Marks'].agg(['count', 'mean', 'max'])
    print("\nc. Department-wise Summary using groupby():")
    print(grouped)

if __name__ == "__main__":
    main()
