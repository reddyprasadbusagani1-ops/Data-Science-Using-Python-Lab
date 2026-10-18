"""
Experiment 11: Loan Prediction Dataset Preprocessing
Course Code: 23A30403 - Data Science Using Python Lab
Note: Synthetic educational data used.
"""
import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

def main():
    print("=== Experiment 11: Loan Data Preprocessing ===")
    
    csv_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'loan_prediction.csv')
    df = pd.read_csv(csv_path)
    print("Original Dataset Sample:")
    print(df[['ApplicantIncome', 'LoanAmount', 'Education', 'Property_Area']].head())
    
    # a. Feature Scaling using MinMaxScaler
    min_max_scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[['ApplicantIncome_MinMax', 'LoanAmount_MinMax']] = min_max_scaler.fit_transform(
        df_scaled[['ApplicantIncome', 'LoanAmount']]
    )
    print("\na. MinMaxScaler Results:")
    print(df_scaled[['ApplicantIncome_MinMax', 'LoanAmount_MinMax']].head())
    
    # b. Feature Standardization using StandardScaler
    std_scaler = StandardScaler()
    df_scaled[['ApplicantIncome_Std', 'LoanAmount_Std']] = std_scaler.fit_transform(
        df_scaled[['ApplicantIncome', 'LoanAmount']]
    )
    print("\nb. StandardScaler Results:")
    print(df_scaled[['ApplicantIncome_Std', 'LoanAmount_Std']].head())
    
    # c. Label Encoding
    le = LabelEncoder()
    df_scaled['Education_Encoded'] = le.fit_transform(df_scaled['Education'])
    print("\nc. LabelEncoder Results for 'Education':")
    print(df_scaled[['Education', 'Education_Encoded']].head())
    
    # d. One-Hot Encoding using pandas.get_dummies()
    one_hot_df = pd.get_dummies(df_scaled[['Property_Area']], prefix='Area')
    print("\nd. One-Hot Encoding Results for 'Property_Area':")
    print(one_hot_df.head())

if __name__ == "__main__":
    main()
