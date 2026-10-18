import pandas as pd
import os

def create_excel():
    data = {
        'StudentID': [101, 102, 103, 104, 105],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Department': ['CSE', 'ECE', 'CSE', 'EEE', 'CSE'],
        'Marks': [85, 78, 92, 64, 88],
        'Attendance': [92, 85, 95, 70, 90]
    }
    df = pd.DataFrame(data)
    target_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'students.xlsx')
    df.to_excel(target_path, index=False)
    print(f"Excel file created successfully at: {os.path.abspath(target_path)}")

if __name__ == "__main__":
    create_excel()
