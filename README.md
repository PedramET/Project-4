# Healthcare Data Cleaning and Analysis Project

## Project Overview
This project focuses on cleaning, analyzing, and visualizing a messy healthcare dataset using Python.  
The goal is to demonstrate real-world data cleaning techniques, exploratory data analysis, and basic data science methods such as anomaly detection.

---

## Dataset Description
The dataset is a downloaded healthcare CSV file containing patient-related information such as:
- Visit Date
- Age
- Gender
- Phone Number
- Email
- Cholesterol Levels

The dataset contains missing values, inconsistent formats, duplicates, and invalid entries, making it suitable for data cleaning and analysis.

---

## Data Cleaning Steps
The following cleaning steps were applied:

1. **Duplicate Removal**
   - Duplicate rows were removed to avoid repeated records.

2. **Visit Date Cleaning**
   - Converted mixed-format visit dates into a standardized datetime format.
   - Invalid or unreadable dates were coerced to missing values.

3. **Age Cleaning**
   - Converted age values to numeric format.
   - Ages less than 0 or greater than 120 were considered unrealistic and replaced with missing values.

4. **Gender Normalization**
   - Trimmed whitespace and converted text to lowercase.
   - Standardized values such as `m` and `f` to `male` and `female`.
   - Invalid gender entries were replaced with missing values.

5. **Phone Number Cleaning**
   - Removed non-numeric characters using regular expressions.
   - Phone numbers with invalid lengths were replaced with missing values.

6. **Email Validation**
   - Email addresses without the `@` symbol were considered invalid and replaced with missing values.

7. **Cholesterol Cleaning**
   - Converted cholesterol values to numeric format.
   - Medically impossible values (below 50 or above 400) were removed.
   - Missing cholesterol values were filled using the median cholesterol level.

---

## Data Analysis
The analysis includes:
- Summary statistics (mean, median, minimum, maximum)
- Quartile analysis
- Distribution analysis using histograms
- Box-and-whisker plots to identify outliers
- Trend analysis over time
- Relationship analysis between age and cholesterol

---

## Anomaly Detection
Anomaly detection was performed on cholesterol levels using the Z-score method.  
Data points with a Z-score greater than 3 were flagged as anomalies.

---

## Visualization Tools
- **Matplotlib** for base plotting
- **Seaborn** for enhanced statistical visualizations

---

## Example Visualizations

<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/00348a0b-dce6-4318-82cd-89870dab4257" /> <img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/5b8fe140-4e22-4f9d-b8cb-b5dabdf4801d" />
<img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/cbabac69-0049-4af4-a770-472bc1f238c5" /> <img width="400" height="300" alt="image" src="https://github.com/user-attachments/assets/e00e0015-6d31-4827-b1d7-40bb026c8a03" />

---

## Libraries Used
- pandas
- numpy
- matplotlib
- seaborn
- scipy

---

## How to Run the Project
1. Place the dataset file (`healthcare_messy_data.csv`) in the project directory.
2. Run the Python script:
   ```bash
   python main.py
