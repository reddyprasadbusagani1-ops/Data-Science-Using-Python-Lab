# Data Science Using Python Lab (Course Code: 23A30403)
**Regulations:** JNTUA R23  
**Target OS:** Windows 11 / Linux / macOS  

---

## 📌 Project Overview
This repository contains the complete master laboratory solution for the **Data Science Using Python Lab** syllabus under **JNTUA R23** regulations. It features 15 modular, fully runnable experiments along with sample datasets, tools, and batch runners.

---

## 📂 Laboratory Syllabus Index

1. **01_numpy_array_creation**: Basic arrays, zeros, ones, random, identity, evenly spaced arrays.
2. **02_shape_and_reshaping**: Dimensions, shape, size, reshaping, flattening, and transposing.
3. **03_expand_squeeze_sort**: Dimension expansion, squeezing, and array sorting.
4. **04_indexing_slicing**: 1D, 2D, 3D array slicing and negative indexing.
5. **05_stacking_concatenation_broadcasting**: Stacking, concatenation, and scalar broadcasting.
6. **06_pandas_dataframe_operations**: DataFrame creation, concatenation, filtering, and column creation.
7. **07_pandas_missing_sort_groupby**: Handling missing values (`NaN`), sorting, and `groupby()`.
8. **08_read_file_formats**: Reading TXT, CSV, Excel (`.xlsx`), and JSON files.
9. **09_pickle_images_glob_database**: Object pickling, Pillow image inspection, Glob matching, and SQLite database operations.
10. **10_web_scraping**: Webpage scraping using `requests` and `BeautifulSoup` with error handling.
11. **11_loan_data_preprocessing**: Min-Max scaling, Standard scaling, Label encoding, One-Hot encoding.
12. **12_matplotlib_visualizations**: Bar chart, Pie chart, Box plot, Histogram, Line plot, Scatter plot.
13. **13_getting_started_nltk**: NLTK library setup, version check, and text tokenization.
14. **14_scikit_learn_and_nltk**: Sentiment classification using Scikit-Learn vectorizers and classifiers.
15. **15_nltk_scipy_pynlpl**: Word statistics using SciPy and optional PyNLPl inspection.

---

## 🚀 Setup Instructions (Windows 11)

1. **Open Command Prompt** in the project folder.
2. **Create Virtual Environment:**
   ```cmd
   py -m venv .venv
   .venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```cmd
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## 🏃 Execution Commands

Run any experiment individually from the project root:
```cmd
python experiments\01_numpy_array_creation\main.py
python experiments\06_pandas_dataframe_operations\main.py
python experiments\12_matplotlib_visualizations\main.py
```

Run all experiments sequentially:
```cmd
python run_all.py
```

---

## 📤 GitHub Upload Guide

```cmd
git init
git add .
git commit -m "Add all 15 Data Science Python lab experiments"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```
