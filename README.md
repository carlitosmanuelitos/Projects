Final Project
The climax of this course is its final project. The final project is your opportunity to take your newfound savvy with programming out for a spin and develop your very own piece of software. So long as your project draws upon this course’s lessons, the nature of your project is entirely up to you. You may implement your project in any language(s). You are welcome to utilize infrastructure other than the CS50 Codespace. All that we ask is that you build something of interest to you, that you solve an actual problem, that you impact your community, or that you change the world. Strive to create something that outlives this course.

Inasmuch as software development is rarely a one-person effort, you are allowed an opportunity to collaborate with one or two classmates for this final project. Needless to say, it is expected that every student in any such group contribute equally to the design and implementation of that group’s project. Moreover, it is expected that the scope of a two- or three-person group’s project be, respectively, twice or thrice that of a typical one-person project. A one-person project, mind you, should entail more time and effort than is required by each of the course’s problem sets.

Note that CS50’s staff audits submissions to CS50x including this final project. Students found to be in violation of the Academic Honesty policy will be removed from the course and deemed ineligible for a certificate. Students who have already completed CS50x, if found to be in violation, will have their CS50 Certificate (and edX Certificate, if applicable) revoked.

Ideas
a web-based application using JavaScript, Python, and SQL
an iOS app using Swift
a game using Lua with LÖVE
an Android app using Java
a Chrome extension using JavaScript
a command-line program using C
a hardware-based application for which you program some device
…
Getting Started
Creating an entire project may seem daunting. Here are some questions that you should think about as you start:

What will your software do? What features will it have? How will it be executed?
What new skills will you need to acquire? What topics will you need to research?
If working with one or two classmates, who will do what?
In the world of software, most everything takes longer to implement than you expect. And so it’s not uncommon to accomplish less in a fixed amount of time than you hope. What might you consider to be a good outcome for your project? A better outcome? The best outcome?
Consider making goal milestones to keep you on track.

If using the CS50 Codespace, create a directory called project to store your project source code and other files. You are welcome to develop your project outside of the CS50 Codespace.





































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





import pandas as pd
import numpy as np
from datetime import datetime

def clean_marketing_data(df):
    """
    Complete data cleaning pipeline for marketing campaign dataset
    """
    print("Starting data cleaning process...")
    print(f"Initial shape: {df.shape}")
    
    # 1. Handle missing values
    df_cleaned = handle_missing_values(df)
    print(f"Shape after handling missing values: {df_cleaned.shape}")
    
    # 2. Fix data types
    df_cleaned = fix_data_types(df_cleaned)
    
    # 3. Handle outliers
    df_cleaned = handle_outliers(df_cleaned)
    print(f"Shape after handling outliers: {df_cleaned.shape}")
    
    # 4. Feature cleaning
    df_cleaned = clean_features(df_cleaned)
    
    # 5. Feature engineering
    df_cleaned = engineer_features(df_cleaned)
    
    print(f"Final shape: {df_cleaned.shape}")
    return df_cleaned

def handle_missing_values(df):
    """
    Handle missing values in the dataset
    """
    df_clean = df.copy()
    
    # 1. Drop rows where Income is missing (can't be reliably imputed)
    df_clean = df_clean.dropna(subset=['Income'])
    
    # 2. Check for any remaining missing values
    missing_summary = df_clean.isnull().sum()
    print("\nMissing values summary:")
    print(missing_summary[missing_summary > 0])
    
    return df_clean

def fix_data_types(df):
    """
    Fix data types of columns
    """
    df_clean = df.copy()
    
    # 1. Convert Dt_Customer to datetime
    df_clean['Dt_Customer'] = pd.to_datetime(df_clean['Dt_Customer'], format='%d-%m-%Y')
    
    # 2. Ensure numeric columns are properly typed
    numeric_columns = ['Income', 'Kidhome', 'Teenhome', 'Recency', 
                      'MntWines', 'MntFruits', 'MntMeatProducts', 
                      'MntFishProducts', 'MntSweetProducts', 'MntGoldProds',
                      'NumDealsPurchases', 'NumWebPurchases', 
                      'NumCatalogPurchases', 'NumStorePurchases', 
                      'NumWebVisitsMonth']
    
    for col in numeric_columns:
        if col in df_clean.columns:
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    
    print("\nUpdated data types:")
    print(df_clean.dtypes)
    
    return df_clean

def handle_outliers(df):
    """
    Handle outliers using IQR method for relevant numerical columns
    """
    df_clean = df.copy()
    
    # Columns to check for outliers
    columns_to_check = ['Income', 'MntWines', 'MntFruits', 'MntMeatProducts', 
                       'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    
    outlier_summary = []
    
    for column in columns_to_check:
        # Calculate IQR
        Q1 = df_clean[column].quantile(0.25)
        Q3 = df_clean[column].quantile(0.75)
        IQR = Q3 - Q1
        
        # Define bounds
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Count outliers
        outliers = df_clean[(df_clean[column] < lower_bound) | 
                           (df_clean[column] > upper_bound)][column]
        
        outlier_summary.append({
            'Column': column,
            'Outliers_Count': len(outliers),
            'Percentage': (len(outliers) / len(df_clean)) * 100
        })
        
        # Cap outliers instead of removing them
        df_clean[column] = df_clean[column].clip(lower=lower_bound, upper=upper_bound)
    
    print("\nOutlier Summary:")
    print(pd.DataFrame(outlier_summary))
    
    return df_clean

def clean_features(df):
    """
    Clean specific features
    """
    df_clean = df.copy()
    
    # 1. Clean Education column
    df_clean['Education'] = df_clean['Education'].replace('2n Cycle', '2nd Cycle')
    df_clean['Education'] = df_clean['Education'].str.capitalize()
    
    # 2. Clean Marital_Status column
    # Remove unusual categories and standardize names
    valid_marital_status = ['Single', 'Married', 'Divorced', 'Widow', 'Together']
    df_clean = df_clean[df_clean['Marital_Status'].isin(valid_marital_status)]
    
    # 3. Remove any negative values from numeric columns
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df_clean[col] = df_clean[col].clip(lower=0)
    
    # 4. Remove unrealistic birth years
    df_clean = df_clean[df_clean['Year_Birth'] > 1900]
    
    # Print summary of cleaning
    print("\nUnique values in cleaned categorical columns:")
    print("Education:", df_clean['Education'].unique())
    print("Marital_Status:", df_clean['Marital_Status'].unique())
    
    return df_clean

def engineer_features(df):
    """
    Create new features and transform existing ones
    """
    df_clean = df.copy()
    
    # 1. Age feature
    df_clean['Age'] = 2024 - df_clean['Year_Birth']
    
    # 2. Total children
    df_clean['Total_Children'] = df_clean['Kidhome'] + df_clean['Teenhome']
    
    # 3. Total spending
    spending_cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 
                    'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
    df_clean['Total_Spending'] = df_clean[spending_cols].sum(axis=1)
    
    # 4. Total purchases
    purchase_cols = ['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']
    df_clean['Total_Purchases'] = df_clean[purchase_cols].sum(axis=1)
    
    # 5. Average spending per purchase
    df_clean['Avg_Spending_Per_Purchase'] = df_clean['Total_Spending'] / df_clean['Total_Purchases']
    
    # 6. Campaign response rate
    campaign_cols = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 
                    'AcceptedCmp4', 'AcceptedCmp5']
    df_clean['Campaign_Response_Rate'] = df_clean[campaign_cols].mean(axis=1)
    
    # 7. Customer tenure
    df_clean['Customer_Tenure_Days'] = (pd.to_datetime('today') - 
                                      df_clean['Dt_Customer']).dt.days
    
    print("\nNew features added:")
    print(list(set(df_clean.columns) - set(df.columns)))
    
    return df_clean

# Example usage
def main():
    # Load the data
    df = pd.read_csv("marketing_campaign.csv", sep="\t")
    
    # Clean the data
    cleaned_df = clean_marketing_data(df)
    
    # Save cleaned dataset
    cleaned_df.to_csv('cleaned_marketing_campaign.csv', index=False)
    
    # Print summary statistics of cleaned dataset
    print("\nCleaned dataset summary:")
    print(cleaned_df.describe())
    
    return cleaned_df

if __name__ == "__main__":
    cleaned_df = main()






import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

def select_and_preprocess_features(df):
    """
    Main function for feature selection and preprocessing
    """
    print("Starting feature selection and preprocessing...")
    
    # 1. Select relevant features
    features_df = select_features(df)
    
    # 2. Remove high correlations
    features_df = handle_correlations(features_df)
    
    # 3. Scale the features
    scaled_features, scaler = scale_features(features_df)
    
    return scaled_features, features_df.columns, scaler

def select_features(df):
    """
    Select relevant features for clustering
    """
    # Numerical features to consider
    numerical_features = [
        'Age',
        'Income',
        'Total_Children',
        'Total_Spending',
        'Total_Purchases',
        'Avg_Spending_Per_Purchase',
        'Customer_Tenure_Days',
        'Campaign_Response_Rate',
        'NumWebVisitsMonth'
    ]
    
    # Verify features exist in dataframe
    available_features = [col for col in numerical_features if col in df.columns]
    
    print("\nSelected features:")
    print(available_features)
    
    return df[available_features]

def handle_correlations(df, threshold=0.8):
    """
    Remove highly correlated features
    """
    # Calculate correlation matrix
    correlation_matrix = df.corr()
    
    # Plot correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Feature Correlation Matrix')
    plt.tight_layout()
    plt.show()
    
    # Find highly correlated features
    high_corr_features = np.where(np.abs(correlation_matrix) > threshold)
    high_corr_features = [(correlation_matrix.index[x], correlation_matrix.columns[y], correlation_matrix.iloc[x, y]) 
                         for x, y in zip(*high_corr_features) if x != y and x < y]
    
    if high_corr_features:
        print("\nHighly correlated feature pairs (correlation > {}):".format(threshold))
        for feat1, feat2, corr in high_corr_features:
            print(f"{feat1} - {feat2}: {corr:.2f}")
            
        # Remove one feature from each highly correlated pair
        features_to_drop = set()
        for feat1, feat2, _ in high_corr_features:
            # Keep the first feature, drop the second
            features_to_drop.add(feat2)
        
        print("\nDropping features due to high correlation:", list(features_to_drop))
        df = df.drop(columns=list(features_to_drop))
    
    return df

def scale_features(df):
    """
    Scale features using StandardScaler
    """
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df)
    
    # Compare original and scaled distributions
    plot_scaling_comparison(df, scaled_features, df.columns)
    
    return scaled_features, scaler

def plot_scaling_comparison(original_df, scaled_features, feature_names):
    """
    Plot distribution comparison of original and scaled features
    """
    scaled_df = pd.DataFrame(scaled_features, columns=feature_names)
    
    n_features = len(feature_names)
    n_cols = 3
    n_rows = (n_features + n_cols - 1) // n_cols
    
    plt.figure(figsize=(15, 5*n_rows))
    
    for idx, feature in enumerate(feature_names):
        plt.subplot(n_rows, n_cols, idx + 1)
        
        # Plot original distribution
        sns.kdeplot(original_df[feature], label='Original', color='blue', alpha=0.5)
        
        # Plot scaled distribution
        sns.kdeplot(scaled_df[feature], label='Scaled', color='red', alpha=0.5)
        
        plt.title(f'Distribution of {feature}')
        plt.legend()
    
    plt.tight_layout()
    plt.show()

def evaluate_feature_importance(scaled_features, feature_names):
    """
    Use PCA to evaluate feature importance
    """
    # Apply PCA
    pca = PCA()
    pca_result = pca.fit_transform(scaled_features)
    
    # Calculate explained variance ratio
    explained_variance_ratio = pca.explained_variance_ratio_
    
    # Plot explained variance ratio
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(explained_variance_ratio) + 1), 
             np.cumsum(explained_variance_ratio), 'bo-')
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance Ratio')
    plt.title('Explained Variance Ratio by PCA Components')
    plt.show()
    
    # Feature importance based on first principal component
    feature_importance = pd.DataFrame(
        abs(pca.components_[0]),
        index=feature_names,
        columns=['Importance']
    ).sort_values('Importance', ascending=False)
    
    print("\nFeature importance based on first principal component:")
    print(feature_importance)
    
    return pca, feature_importance

# Example usage
def main():
    # Assuming we have our cleaned dataset
    df = pd.read_csv('cleaned_marketing_campaign.csv')
    
    # Perform feature selection and preprocessing
    scaled_features, feature_names, scaler = select_and_preprocess_features(df)
    
    # Evaluate feature importance
    pca, feature_importance = evaluate_feature_importance(scaled_features, feature_names)
    
    return scaled_features, feature_names, scaler, pca, feature_importance

if __name__ == "__main__":
    scaled_features, feature_names, scaler, pca, feature_importance = main()








import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
import hdbscan
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from scipy.cluster.hierarchy import dendrogram, linkage
from kneed import KneeLocator
import warnings
warnings.filterwarnings('ignore')

class AdvancedClustering:
    def __init__(self, scaled_features, feature_names):
        self.scaled_features = scaled_features
        self.feature_names = feature_names
        self.results = {}
        
    def run_all_clustering(self):
        """
        Run all clustering algorithms and compare results
        """
        print("Starting comprehensive clustering analysis...")
        
        # 1. K-means clustering
        self.run_kmeans()
        
        # 2. Hierarchical clustering
        self.run_hierarchical()
        
        # 3. DBSCAN
        self.run_dbscan()
        
        # 4. HDBSCAN (state-of-the-art)
        self.run_hdbscan()
        
        # Compare results
        self.compare_clustering_results()
        
        return self.results
    
    def run_kmeans(self):
        """
        Perform K-means clustering with optimal k
        """
        print("\nPerforming K-means clustering...")
        
        # Find optimal k
        k_range = range(2, 11)
        inertias = []
        silhouette_scores = []
        
        for k in k_range:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(self.scaled_features)
            inertias.append(kmeans.inertia_)
            silhouette_scores.append(silhouette_score(self.scaled_features, kmeans.labels_))
        
        # Plot evaluation metrics
        plt.figure(figsize=(15, 5))
        
        # Elbow curve
        plt.subplot(1, 2, 1)
        plt.plot(k_range, inertias, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Inertia')
        plt.title('Elbow Method for K-means')
        
        # Silhouette scores
        plt.subplot(1, 2, 2)
        plt.plot(k_range, silhouette_scores, 'rx-')
        plt.xlabel('k')
        plt.ylabel('Silhouette Score')
        plt.title('Silhouette Scores for K-means')
        
        plt.tight_layout()
        plt.show()
        
        # Select optimal k
        optimal_k = k_range[np.argmax(silhouette_scores)]
        
        # Final K-means clustering
        kmeans = KMeans(n_clusters=optimal_k, random_state=42)
        labels = kmeans.fit_predict(self.scaled_features)
        
        self.results['kmeans'] = {
            'labels': labels,
            'model': kmeans,
            'silhouette': silhouette_scores[optimal_k-2]
        }
        
    def run_hierarchical(self):
        """
        Perform hierarchical clustering
        """
        print("\nPerforming Hierarchical clustering...")
        
        # Create linkage matrix
        linkage_matrix = linkage(self.scaled_features, method='ward')
        
        # Plot dendrogram
        plt.figure(figsize=(10, 7))
        dendrogram(linkage_matrix)
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('Sample Index')
        plt.ylabel('Distance')
        plt.show()
        
        # Try different numbers of clusters
        silhouette_scores = []
        n_clusters_range = range(2, 11)
        
        for n_clusters in n_clusters_range:
            hierarchical = AgglomerativeClustering(n_clusters=n_clusters)
            labels = hierarchical.fit_predict(self.scaled_features)
            silhouette_scores.append(silhouette_score(self.scaled_features, labels))
        
        # Plot silhouette scores
        plt.figure(figsize=(8, 5))
        plt.plot(n_clusters_range, silhouette_scores, 'bo-')
        plt.xlabel('Number of Clusters')
        plt.ylabel('Silhouette Score')
        plt.title('Silhouette Scores for Hierarchical Clustering')
        plt.show()
        
        # Select optimal number of clusters
        optimal_n = n_clusters_range[np.argmax(silhouette_scores)]
        
        # Final hierarchical clustering
        hierarchical = AgglomerativeClustering(n_clusters=optimal_n)
        labels = hierarchical.fit_predict(self.scaled_features)
        
        self.results['hierarchical'] = {
            'labels': labels,
            'model': hierarchical,
            'silhouette': max(silhouette_scores)
        }
        
    def run_dbscan(self):
        """
        Perform DBSCAN clustering
        """
        print("\nPerforming DBSCAN clustering...")
        
        # Find optimal epsilon using nearest neighbors
        from sklearn.neighbors import NearestNeighbors
        
        neighbors = NearestNeighbors(n_neighbors=2)
        neighbors_fit = neighbors.fit(self.scaled_features)
        distances, indices = neighbors_fit.kneighbors(self.scaled_features)
        distances = np.sort(distances[:, 1])
        
        # Plot k-distance graph
        plt.figure(figsize=(8, 5))
        plt.plot(distances)
        plt.xlabel('Points')
        plt.ylabel('k-distance')
        plt.title('k-distance Graph for DBSCAN')
        plt.show()
        
        # Estimate epsilon using knee point
        knee = KneeLocator(range(len(distances)), distances, 
                          curve='convex', direction='increasing')
        epsilon = distances[knee.knee]
        
        # Try different min_samples values
        min_samples_range = [3, 5, 10, 15, 20]
        best_silhouette = -1
        best_labels = None
        best_min_samples = None
        
        for min_samples in min_samples_range:
            dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
            labels = dbscan.fit_predict(self.scaled_features)
            
            # Only calculate silhouette score if more than one cluster
            if len(np.unique(labels)) > 1:
                current_silhouette = silhouette_score(self.scaled_features, labels)
                if current_silhouette > best_silhouette:
                    best_silhouette = current_silhouette
                    best_labels = labels
                    best_min_samples = min_samples
        
        self.results['dbscan'] = {
            'labels': best_labels,
            'parameters': {'eps': epsilon, 'min_samples': best_min_samples},
            'silhouette': best_silhouette
        }
        
    def run_hdbscan(self):
        """
        Perform HDBSCAN clustering (state-of-the-art)
        """
        print("\nPerforming HDBSCAN clustering...")
        
        # Try different min_cluster_sizes
        min_cluster_sizes = [5, 10, 15, 20, 30]
        best_score = -1
        best_labels = None
        best_model = None
        
        for min_cluster_size in min_cluster_sizes:
            clusterer = hdbscan.HDBSCAN(
                min_cluster_size=min_cluster_size,
                min_samples=None,
                cluster_selection_method='eom'  # Excess of Mass
            )
            
            labels = clusterer.fit_predict(self.scaled_features)
            
            # Use DBCV score (specific to HDBSCAN) for evaluation
            if len(np.unique(labels)) > 1:
                score = clusterer.relative_validity_
                if score > best_score:
                    best_score = score
                    best_labels = labels
                    best_model = clusterer
        
        self.results['hdbscan'] = {
            'labels': best_labels,
            'model': best_model,
            'dbcv_score': best_score
        }
        
    def compare_clustering_results(self):
        """
        Compare results from different clustering methods
        """
        print("\nComparing clustering results...")
        
        # Create comparison metrics
        comparison = {}
        for method, result in self.results.items():
            labels = result['labels']
            n_clusters = len(np.unique(labels[labels >= 0]))  # Account for noise points (-1)
            
            comparison[method] = {
                'n_clusters': n_clusters,
                'n_noise': np.sum(labels == -1) if -1 in labels else 0,
                'silhouette': silhouette_score(self.scaled_features, labels) if n_clusters > 1 else np.nan,
                'calinski': calinski_harabasz_score(self.scaled_features, labels) if n_clusters > 1 else np.nan
            }
        
        comparison_df = pd.DataFrame(comparison).round(3)
        print("\nClustering Comparison:")
        print(comparison_df)
        
        # Visualize cluster assignments
        self.plot_cluster_comparisons()
        
    def plot_cluster_comparisons(self):
        """
        Visualize clustering results from different methods
        """
        n_methods = len(self.results)
        fig, axes = plt.subplots(1, n_methods, figsize=(5*n_methods, 5))
        
        for ax, (method, result) in zip(axes, self.results.items()):
            # Use first two features for visualization
            scatter = ax.scatter(self.scaled_features[:, 0], self.scaled_features[:, 1],
                               c=result['labels'], cmap='viridis')
            ax.set_title(f'{method.upper()} Clustering')
            plt.colorbar(scatter, ax=ax)
        
        plt.tight_layout()
        plt.show()

# Example usage
def main():
    # Assuming we have scaled_features and feature_names from previous preprocessing
    scaled_features = np.load('scaled_features.npy')
    feature_names = pd.read_csv('feature_names.csv')['Feature'].tolist()
    
    # Initialize and run clustering analysis
    clustering = AdvancedClustering(scaled_features, feature_names)
    results = clustering.run_all_clustering()
    
    return clustering, results

if __name__ == "__main__":
    clustering, results = main()
    





class ComprehensiveClustering:
    def __init__(self, scaled_features, feature_names, original_df):
        self.scaled_features = scaled_features
        self.feature_names = feature_names
        self.original_df = original_df
        self.results = {}
        
    def analyze_optimal_clusters(self, max_k=10):
        """
        Determine optimal number of clusters using multiple methods
        """
        k_range = range(2, max_k + 1)
        metrics = {
            'inertias': [],
            'silhouette_scores': [],
            'calinski_scores': []
        }
        
        for k in k_range:
            kmeans = KMeans(n_clusters=k, random_state=42)
            labels = kmeans.fit_predict(self.scaled_features)
            
            metrics['inertias'].append(kmeans.inertia_)
            metrics['silhouette_scores'].append(silhouette_score(self.scaled_features, labels))
            metrics['calinski_scores'].append(calinski_harabasz_score(self.scaled_features, labels))
        
        # Plot all metrics
        plt.figure(figsize=(15, 5))
        
        # Elbow plot
        plt.subplot(131)
        plt.plot(k_range, metrics['inertias'], 'bo-')
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Inertia')
        plt.title('Elbow Method')
        
        # Find elbow point
        kl = KneeLocator(k_range, metrics['inertias'], curve='convex', direction='decreasing')
        if kl.elbow:
            plt.axvline(x=kl.elbow, color='r', linestyle='--')
        
        # Silhouette score plot
        plt.subplot(132)
        plt.plot(k_range, metrics['silhouette_scores'], 'go-')
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Silhouette Score')
        plt.title('Silhouette Analysis')
        
        # Calinski-Harabasz score plot
        plt.subplot(133)
        plt.plot(k_range, metrics['calinski_scores'], 'mo-')
        plt.xlabel('Number of Clusters (k)')
        plt.ylabel('Calinski-Harabasz Score')
        plt.title('Calinski-Harabasz Analysis')
        
        plt.tight_layout()
        plt.show()
        
        return metrics
    
    def analyze_cluster_profiles(self, labels, method_name):
        """
        Analyze and visualize cluster profiles
        """
        # Create DataFrame with features and labels
        cluster_df = pd.DataFrame(self.scaled_features, columns=self.feature_names)
        cluster_df['Cluster'] = labels
        
        # 1. Cluster size distribution
        plt.figure(figsize=(10, 5))
        sizes = cluster_df['Cluster'].value_counts()
        sizes.plot(kind='bar')
        plt.title(f'Cluster Size Distribution - {method_name}')
        plt.xlabel('Cluster')
        plt.ylabel('Number of Samples')
        plt.show()
        
        # 2. Cluster profiles heatmap
        cluster_means = cluster_df.groupby('Cluster').mean()
        plt.figure(figsize=(12, 8))
        sns.heatmap(cluster_means, annot=True, cmap='RdYlBu', center=0)
        plt.title(f'Cluster Profiles Heatmap - {method_name}')
        plt.show()
        
        # 3. Feature distributions by cluster
        self.plot_feature_distributions(cluster_df, method_name)
        
        return cluster_means
    
    def plot_feature_distributions(self, cluster_df, method_name):
        """
        Plot distribution of each feature by cluster
        """
        n_features = len(self.feature_names)
        n_cols = 3
        n_rows = (n_features + n_cols - 1) // n_cols
        
        plt.figure(figsize=(15, 5 * n_rows))
        
        for idx, feature in enumerate(self.feature_names):
            plt.subplot(n_rows, n_cols, idx + 1)
            
            for cluster in sorted(cluster_df['Cluster'].unique()):
                cluster_data = cluster_df[cluster_df['Cluster'] == cluster][feature]
                sns.kdeplot(data=cluster_data, label=f'Cluster {cluster}')
            
            plt.title(f'{feature} Distribution by Cluster')
            plt.legend()
        
        plt.suptitle(f'Feature Distributions by Cluster - {method_name}')
        plt.tight_layout()
        plt.show()
    
    def visualize_clusters_2d(self, labels, method_name):
        """
        Create 2D visualization of clusters using different techniques
        """
        # 1. PCA visualization
        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(self.scaled_features)
        
        # 2. t-SNE visualization
        tsne = TSNE(n_components=2, random_state=42)
        tsne_result = tsne.fit_transform(self.scaled_features)
        
        # Create visualizations
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # PCA plot
        scatter1 = axes[0].scatter(pca_result[:, 0], pca_result[:, 1], 
                                 c=labels, cmap='viridis')
        axes[0].set_title(f'PCA Visualization - {method_name}')
        plt.colorbar(scatter1, ax=axes[0])
        
        # t-SNE plot
        scatter2 = axes[1].scatter(tsne_result[:, 0], tsne_result[:, 1], 
                                 c=labels, cmap='viridis')
        axes[1].set_title(f't-SNE Visualization - {method_name}')
        plt.colorbar(scatter2, ax=axes[1])
        
        plt.tight_layout()
        plt.show()
    
    def analyze_cluster_characteristics(self, labels, method_name):
        """
        Analyze detailed characteristics of each cluster
        """
        # Combine scaled features with original data
        analysis_df = self.original_df.copy()
        analysis_df['Cluster'] = labels
        
        cluster_profiles = {}
        
        for cluster in sorted(np.unique(labels)):
            cluster_data = analysis_df[analysis_df['Cluster'] == cluster]
            
            # Calculate key metrics
            profile = {
                'Size': len(cluster_data),
                'Size_Percentage': len(cluster_data) / len(analysis_df) * 100,
                'Age_Mean': cluster_data['Age'].mean(),
                'Income_Mean': cluster_data['Income'].mean(),
                'Total_Spending_Mean': cluster_data['Total_Spending'].mean(),
                'Campaign_Response_Rate': cluster_data['Campaign_Response_Rate'].mean(),
                'Web_Purchase_Ratio': cluster_data['Web_Purchase_Ratio'].mean()
            }
            
            cluster_profiles[f'Cluster_{cluster}'] = profile
        
        # Create profile summary DataFrame
        profile_df = pd.DataFrame(cluster_profiles).round(2)
        
        print(f"\nCluster Profiles Summary - {method_name}")
        print(profile_df)
        
        # Visualize key characteristics
        self.plot_cluster_characteristics(profile_df, method_name)
        
        return profile_df
    
    def plot_cluster_characteristics(self, profile_df, method_name):
        """
        Create visualizations for cluster characteristics
        """
        # 1. Cluster sizes
        plt.figure(figsize=(15, 5))
        
        plt.subplot(131)
        profile_df.loc['Size'].plot(kind='bar')
        plt.title('Cluster Sizes')
        plt.xticks(rotation=45)
        
        # 2. Key metrics comparison
        plt.subplot(132)
        metrics = ['Age_Mean', 'Income_Mean', 'Total_Spending_Mean']
        profile_df.loc[metrics].plot(kind='bar')
        plt.title('Key Metrics by Cluster')
        plt.xticks(rotation=45)
        
        # 3. Response rates
        plt.subplot(133)
        metrics = ['Campaign_Response_Rate', 'Web_Purchase_Ratio']
        profile_df.loc[metrics].plot(kind='bar')
        plt.title('Response Rates by Cluster')
        plt.xticks(rotation=45)
        
        plt.suptitle(f'Cluster Characteristics - {method_name}')
        plt.tight_layout()
        plt.show()
    
    def run_complete_analysis(self):
        """
        Run complete clustering analysis with all visualizations and profiles
        """
        # 1. Analyze optimal number of clusters
        metrics = self.analyze_optimal_clusters()
        
        # 2. Run all clustering methods
        clustering_methods = {
            'kmeans': self.run_kmeans,
            'hierarchical': self.run_hierarchical,
            'dbscan': self.run_dbscan,
            'hdbscan': self.run_hdbscan
        }
        
        for method_name, clustering_func in clustering_methods.items():
            print(f"\nRunning {method_name} clustering...")
            
            # Run clustering
            labels = clustering_func()
            
            # Analyze cluster profiles
            cluster_profiles = self.analyze_cluster_profiles(labels, method_name)
            
            # Visualize clusters
            self.visualize_clusters_2d(labels, method_name)
            
            # Analyze cluster characteristics
            cluster_characteristics = self.analyze_cluster_characteristics(labels, method_name)
            
            # Store results
            self.results[method_name] = {
                'labels': labels,
                'profiles': cluster_profiles,
                'characteristics': cluster_characteristics
            }
        
        # Compare results across methods
        self.compare_clustering_results()
        
        return self.results

# Example usage
def main():
    # Load data and preprocessing results
    scaled_features = np.load('scaled_features.npy')
    feature_names = pd.read_csv('feature_names.csv')['Feature'].tolist()
    original_df = pd.read_csv('cleaned_marketing_campaign.csv')
    
    # Initialize and run analysis
    clustering = ComprehensiveClustering(scaled_features, feature_names, original_df)
    results = clustering.run_complete_analysis()
    
    return clustering, results

if __name__ == "__main__":
    clustering, results = main()
