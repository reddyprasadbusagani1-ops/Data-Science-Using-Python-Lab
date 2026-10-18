"""
Experiment 9: Pickle, Images, Glob, and Databases
Course Code: 23A30403 - Data Science Using Python Lab
"""
import os
import pickle
import glob
import sqlite3
from PIL import Image

def main():
    print("=== Experiment 9: Pickle, Images, Glob, and Databases ===")
    
    data_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
    
    # a. Reading and Writing Pickle File
    # WARNING: Unpickle only files from trusted sources as unpickling arbitrary data can execute malicious code.
    print("\na. Pickle Demonstration (Trusted File Serialization):")
    sample_data = {"course": "Data Science Lab", "code": "23A30403", "students": 60}
    pickle_path = os.path.join(data_dir, "temp_data.pkl")
    
    with open(pickle_path, "wb") as f:
        pickle.dump(sample_data, f)
    print(f"Saved object to pickle: {pickle_path}")
    
    with open(pickle_path, "rb") as f:
        loaded_data = pickle.load(f)
    print(f"Loaded object from pickle: {loaded_data}")
    
    if os.path.exists(pickle_path):
        os.remove(pickle_path)
        
    # b. Opening & Inspecting Image with PIL
    img_path = os.path.join(data_dir, "sample.png")
    print(f"\nb. Inspecting Image with Pillow ({img_path}):")
    if os.path.exists(img_path):
        img = Image.open(img_path)
        print(f"Image Format: {img.format}, Size: {img.size}, Mode: {img.mode}")
    else:
        print("Sample image not found.")
        
    # c. Glob module usage
    print(f"\nc. Finding files in data directory using Glob:")
    files = glob.glob(os.path.join(data_dir, "*.*"))
    for file in files:
        print(f" - {os.path.basename(file)}")
        
    # d. SQLite Database interaction
    db_path = os.path.join(data_dir, "sample_database.db")
    print(f"\nd. Querying SQLite Database ({db_path}):")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(f" ID: {row[0]}, Name: {row[1]}, Role: {row[2]}, Salary: ${row[3]}")
    conn.close()

if __name__ == "__main__":
    main()
