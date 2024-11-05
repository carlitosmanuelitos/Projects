# 1. Initial Data Inspection
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load data
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# Basic dataset information
def inspect_data(df):
    print("1. Dataset Shape:", df.shape)
    print("\n2. Column Names:")
    print(df.columns.tolist())
    print("\n3. Data Types:")
    print(df.dtypes)
    print("\n4. First few rows:")
    print(df.head())
    print("\n5. Basic statistics:")
    print(df.describe())

# 2. Missing Value Analysis
def analyze_missing_values(df):
    missing_vals = df.isnull().sum()
    missing_vals_percent = 100 * missing_vals / len(df)
    
    missing_val_table = pd.concat([missing_vals, missing_vals_percent], axis=1)
    missing_val_table.columns = ['Missing Values', 'Percentage']
    missing_val_table = missing_val_table[missing_val_table['Missing Values'] > 0].sort_values('Missing Values', ascending=False)
    
    print("\n6. Missing Value Analysis:")
    print(missing_val_table)
    
    if not missing_val_table.empty:
        plt.figure(figsize=(10, 6))
        plt.bar(missing_val_table.index, missing_val_table['Percentage'])
        plt.title('Percentage of Missing Values by Column')
        plt.xticks(rotation=45)
        plt.ylabel('Percentage')
        plt.tight_layout()
        plt.show()

# 3. Categorical Variable Analysis
def analyze_categorical_vars(df):
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    print("\n7. Categorical Variable Analysis:")
    for col in categorical_cols:
        print(f"\nUnique values in {col}:")
        value_counts = df[col].value_counts()
        print(value_counts)
        
        plt.figure(figsize=(10, 5))
        value_counts.plot(kind='bar')
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# 4. Numerical Variable Analysis
def analyze_numerical_vars(df):
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    print("\n8. Numerical Variable Analysis:")
    
    # Distribution plots
    for col in numerical_cols:
        plt.figure(figsize=(12, 4))
        
        # Histogram
        plt.subplot(121)
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f'Distribution of {col}')
        plt.xticks(rotation=45)
        
        # Box plot
        plt.subplot(122)
        sns.boxplot(y=df[col].dropna())
        plt.title(f'Box Plot of {col}')
        
        plt.tight_layout()
        plt.show()
        
        # Basic statistics
        print(f"\nStatistics for {col}:")
        print(df[col].describe())

# 5. Age Distribution Analysis
def analyze_age(df):
    df['Age'] = 2024 - df['Year_Birth']
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(121)
    sns.histplot(df['Age'], kde=True)
    plt.title('Age Distribution')
    
    plt.subplot(122)
    sns.boxplot(y=df['Age'])
    plt.title('Age Box Plot')
    
    plt.tight_layout()
    plt.show()
    
    print("\n9. Age Statistics:")
    print(df['Age'].describe())

# 6. Income vs Spending Analysis
def analyze_income_spending(df):
    # Calculate total spending
    spending_cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 
                    'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    df['Total_Spending'] = df[spending_cols].sum(axis=1)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Income'], df['Total_Spending'], alpha=0.5)
    plt.title('Income vs Total Spending')
    plt.xlabel('Income')
    plt.ylabel('Total Spending')
    plt.tight_layout()
    plt.show()
    
    # Correlation analysis
    correlation = df['Income'].corr(df['Total_Spending'])
    print(f"\n10. Correlation between Income and Total Spending: {correlation:.2f}")

# 7. Campaign Response Analysis
def analyze_campaigns(df):
    campaign_cols = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 
                    'AcceptedCmp4', 'AcceptedCmp5']
    
    # Calculate response rates
    response_rates = df[campaign_cols].mean() * 100
    
    plt.figure(figsize=(10, 5))
    response_rates.plot(kind='bar')
    plt.title('Campaign Response Rates')
    plt.xlabel('Campaign')
    plt.ylabel('Response Rate (%)')
    plt.tight_layout()
    plt.show()
    
    print("\n11. Campaign Response Rates:")
    print(response_rates)

# 8. Purchase Behavior Analysis
def analyze_purchases(df):
    purchase_cols = ['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']
    
    plt.figure(figsize=(12, 5))
    
    plt.subplot(121)
    df[purchase_cols].boxplot()
    plt.title('Purchase Distribution by Channel')
    plt.ylabel('Number of Purchases')
    
    plt.subplot(122)
    purchase_means = df[purchase_cols].mean()
    purchase_means.plot(kind='bar')
    plt.title('Average Purchases by Channel')
    plt.ylabel('Average Number of Purchases')
    
    plt.tight_layout()
    plt.show()
    
    print("\n12. Purchase Statistics by Channel:")
    print(df[purchase_cols].describe())

# Execute all EDA steps
def run_complete_eda(df):
    inspect_data(df)
    analyze_missing_values(df)
    analyze_categorical_vars(df)
    analyze_numerical_vars(df)
    analyze_age(df)
    analyze_income_spending(df)
    analyze_campaigns(df)
    analyze_purchases(df)

# Run the analysis
run_complete_eda(df)
