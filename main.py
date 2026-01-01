
import pandas as pd              # Import pandas for working with tables (DataFrames)
import numpy as np               # Import numpy for numerical operations
import seaborn as sns            # Import seaborn for statistical visualizations
import matplotlib.pyplot as plt  # Import matplotlib for displaying plots
from scipy import stats          # Import scipy stats for statistical calculations (Z-score)


# -------------------------------
# 1. Load the dataset
# -------------------------------
def load_data(file_path):
    """Load CSV file into a pandas DataFrame."""

    df = pd.read_csv(file_path)

    print("Data loaded successfully!")
    print(df.head(15))
    print(df.info())

    return df


# -------------------------------
# 2. Clean the dataset
# -------------------------------
def clean_data(df):
    """Clean messy healthcare data."""

    df = df.drop_duplicates()

    # -------------------------------
    # Visit Date cleaning
    # -------------------------------
    if "Visit Date" in df.columns:  
        df["Visit Date"] = pd.to_datetime(df["Visit Date"], format="mixed", dayfirst=True, errors="coerce")

    # -------------------------------
    # Age cleaning
    # -------------------------------
    if "Age" in df.columns: 
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

        # Replace unrealistic ages with NaN
        df.loc[(df["Age"] < 0) | (df["Age"] > 120), "Age"] = pd.NA # .loc[rows, columns]

    # -------------------------------
    # Gender cleaning
    # -------------------------------
    if "Gender" in df.columns: 
        df["Gender"] = (df["Gender"].astype(str).str.strip().str.lower())

        df["Gender"] = df["Gender"].replace({
            "m": "male",           
            "f": "female"
        })

        # Replace invalid gender values with NaN, ~ Means NOT
        df.loc[~df["Gender"].isin(["male", "female"]), "Gender"] = pd.NA # .isin(...) Checks each value in the "Gender" column, True if the value is "male" or "female", false otherwise

    # -------------------------------
    # Phone Number cleaning
    # -------------------------------
    if "Phone Number" in df.columns: 
        df["Phone Number"] = (df["Phone Number"].astype(str).str.replace(r"\D", "", regex=True))

        # Replace phone numbers with invalid length
        df.loc[~df["Phone Number"].str.len().between(7, 15), "Phone Number"] = pd.NA

    # -------------------------------
    # Email cleaning
    # -------------------------------
    if "Email" in df.columns:  
        df.loc[~df["Email"].astype(str).str.contains("@", na=False), "Email"] = pd.NA

    # -------------------------------
    # Cholesterol cleaning
    # -------------------------------
    if "Cholesterol" in df.columns:  
        df["Cholesterol"] = pd.to_numeric(df["Cholesterol"], errors="coerce")

        # Remove medically impossible cholesterol values
        df.loc[(df["Cholesterol"] < 50) | (df["Cholesterol"] > 400), "Cholesterol"] = pd.NA

        # Fill missing cholesterol values with the median
        df["Cholesterol"] = df["Cholesterol"].fillna(df["Cholesterol"].median())

    # -------------------------------
    # Blood Pressure cleaning
    # -------------------------------
    if "Blood Pressure" in df.columns:  
        bp_split = (df["Blood Pressure"].astype(str).str.split("/", expand=True))

    # -------------------------------
    # Drop rows missing critical values
    # -------------------------------

    # df = df.dropna(subset=["Visit Date", "Cholesterol"])  # Keep essential data

    print("Data cleaning complete!")  
    print(df.head(15))

    return df


# -------------------------------
# 3. Visualization
# -------------------------------
def visualize_data(df):
    """Create Seaborn visualizations."""
        # Histogram Plot
    if "Cholesterol" in df.columns:  
        sns.histplot(df["Cholesterol"], kde=True)
        plt.title("Distribution of Cholesterol Levels")
        plt.xlabel("Cholesterol")
        plt.ylabel("Frequency")
        plt.show()

        # Box Plot
    if "Cholesterol" in df.columns and "Gender" in df.columns:
        sns.boxplot(x="Gender", y="Cholesterol", data=df)  
        plt.title("Cholesterol Levels by Gender")
        plt.show()

        # Line Plot
    if "Visit Date" in df.columns and "Cholesterol" in df.columns:
        sns.lineplot(x="Visit Date", y="Cholesterol", data=df)  
        plt.title("Cholesterol Over Time")
        plt.xlabel("Visit Date")
        plt.ylabel("Cholesterol")
        plt.show()

        # Scatter Plot
    if "Age" in df.columns and "Cholesterol" in df.columns:
        sns.scatterplot(x="Age", y="Cholesterol", data=df)
        plt.title("Age vs Cholesterol") 
        plt.xlabel("Age")
        plt.ylabel("Cholesterol")
        plt.show()


# -------------------------------
# 4. Anomaly Detection
# -------------------------------
def detect_anomalies(df, column):
    """Detect anomalies using Z-score."""
    
    if column not in df.columns:  
        print(f"No column '{column}' for anomaly detection.")
        return pd.DataFrame()

    values = pd.to_numeric(df[column], errors="coerce").dropna()

    z_scores = np.abs(stats.zscore(values))  

    anomalies = df.loc[values.index[z_scores > 3]]  

    print(f"Anomalies detected in '{column}':")
    print(anomalies)

    return anomalies


# -------------------------------
# 5. Summary Statistics
# -------------------------------
def summary_statistics(df):
    """Print summary statistics for numeric columns."""

    numeric_cols = df.select_dtypes(include=np.number).columns  # select_dtypes: selects columns based on data type

    for col in numeric_cols:  
        print(f"\nSummary Statistics for '{col}':")
        print(f"Mean: {df[col].mean()}")
        print(f"Median: {df[col].median()}")     
        print(f"Min: {df[col].min()}, Max: {df[col].max()}")  
        print("Quartiles:")
        print(df[col].quantile([0.25, 0.5, 0.75]))  


# -------------------------------
# 6. Main function
# -------------------------------
def main():
    df = load_data("healthcare_messy_data.csv")  
    df = clean_data(df)
    visualize_data(df)
    detect_anomalies(df, "Cholesterol")
    summary_statistics(df)


# Run the program
if __name__ == "__main__":  
    main()
