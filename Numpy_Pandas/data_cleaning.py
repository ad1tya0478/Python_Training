import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Reliance Trends Fashion.csv')

# --------------------------
# 1. DATA CLEANING
# --------------------------

# Remove leading/trailing spaces in column names
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Remove commas and convert prices to numeric
df['Discount_Price_in_Rs.'] = df['Discount_Price_(in_Rs.)'].astype(str).str.replace(',', '').astype(float)
df['Original_Price_in_Rs.'] = df['Original_Price_(in_Rs.)'].astype(str).str.replace(',', '').astype(float)

# Drop old columns
df.drop(['Discount_Price_(in_Rs.)', 'Original_Price_(in_Rs.)'], axis=1, inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove rows with missing values
df.dropna(inplace=True)


""" 2. DATA ANALYSIS """

# Discount percentage
df['Discount_Percentage'] = ((df['Original_Price_in_Rs.'] - df['Discount_Price_in_Rs.']) / df['Original_Price_in_Rs.']) * 100

# Summary statistics
brand_counts = df['Brand'].value_counts()
category_counts = df['Category'].value_counts()
gender_counts = df['Category_by_gender'].value_counts()



"""  PLOTS """
# Brand Count Plot
plt.figure()
brand_counts.plot(kind='bar')
plt.xlabel('Brand')
plt.ylabel('Number of Products')
plt.title('Products per Brand')
plt.tight_layout()
plt.savefig('brand_count_plot.png')

# Category Count Plot
plt.figure()
category_counts.plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Products per Category')
plt.tight_layout()
plt.savefig('category_count_plot.png')

# Discount Percentage Distribution
plt.figure()
df['Discount_Percentage'].plot(kind='hist')
plt.xlabel('Discount Percentage')
plt.title('Discount Distribution')
plt.tight_layout()
plt.savefig('discount_distribution.png')

""" REPORT TEXT FILE """

report = f'''
RELIANCE TRENDS DATA ANALYSIS REPORT

1. DATA CLEANING PERFORMED:
- Removed spaces in column names
- Converted price columns to numbers
- Removed duplicates
- Removed missing values
- Created new column: Discount_Percentage

2. SUMMARY:
Total Products: {len(df)}
Total Brands: {df['Brand'].nunique()}
Total Categories: {df['Category'].nunique()}

Top Brands:
{brand_counts.to_string()}

Top Categories:
{category_counts.to_string()}

Gender-based Distribution:
{gender_counts.to_string()}

3. INSIGHTS:
- Highest discount percentage shows how pricing strategy helps improve sales.
- Brands with more products show stronger presence and better inventory strategy.
- Category-wise distribution shows what sells the most.

4. RECOMMENDATIONS:
- Increase stock for top selling categories.
- Provide more discounts on slow-moving brands.
- Improve visibility for low-count categories.
- Focus on the gender category that shows lower count to increase sales.

Charts Saved:
- brand_count_plot.png
- category_count_plot.png
- discount_distribution.png
'''

with open('analysis_report.txt', 'w') as f:
    f.write(report)

print("Cleaning + Analysis + Plots Completed Successfully!")
print("Generated files: brand_count_plot.png, category_count_plot.png, discount_distribution.png, analysis_report.txt")
print()


