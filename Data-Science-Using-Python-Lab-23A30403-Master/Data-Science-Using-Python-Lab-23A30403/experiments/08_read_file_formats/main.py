"""
Experiment 8: Reading Common File Formats
Course Code: 23A30403 - Data Science Using Python Lab
"""
import os
import pandas as pd
import json

def main():
    print("=== Experiment 8: Reading Common File Formats ===")
    
    base_data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
    
    # a. Reading a text file
    txt_path = os.path.join(base_data_path, 'sample.txt')
    print(f"\na. Reading Text File ({txt_path}):")
    with open(txt_path, 'r', encoding='utf-8') as f:
        print(f.read().strip())
        
    # b. Reading a CSV file
    csv_path = os.path.join(base_data_path, 'students.csv')
    print(f"\nb. Reading CSV File ({csv_path}):")
    df_csv = pd.read_csv(csv_path)
    print(df_csv.head())
    
    # c. Reading an Excel .xlsx file
    xlsx_path = os.path.join(base_data_path, 'students.xlsx')
    print(f"\nc. Reading Excel File ({xlsx_path}):")
    df_xlsx = pd.read_excel(xlsx_path)
    print(df_xlsx.head())
    
    # d. Reading a JSON file
    json_path = os.path.join(base_data_path, 'students.json')
    print(f"\nd. Reading JSON File ({json_path}):")
    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    print(json.dumps(json_data[:2], indent=2))

if __name__ == "__main__":
    main()
