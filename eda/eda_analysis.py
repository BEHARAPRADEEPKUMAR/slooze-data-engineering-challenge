import pandas as pd
import matplotlib.pyplot as plt


# Load Dataset
df = pd.read_csv("data/clean_products.csv")

print("DATASET OVERVIEW")


print("\nFirst 5 Rows:")
print(df.head())

print("\nTotal Products Collected:", len(df))

print("\nColumns Available:")
print(df.columns)

# Summary Statistics
print("SUMMARY STATISTICS")

print("\nProducts per Page:")
print(df["Page"].value_counts())

print("\nCategory Distribution:")
print(df["Category"].value_counts())


# Keyword / Product Type Trends
print("TOP PRODUCT KEYWORDS")

# Extract first keyword from product title
df["Keyword"] = df["Product_Name"].apply(lambda x: x.split()[0])

print("\nTop 10 Frequent Keywords:")
print(df["Keyword"].value_counts().head(10))

# Plot Keyword Frequency
plt.figure()
df["Keyword"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Product Keywords")
plt.xlabel("Keyword")
plt.ylabel("Frequency")
plt.show()


# Supplier Insights
if "Supplier" in df.columns:
    print("🏢 SUPPLIER ANALYSIS")

    # Drop missing supplier values
    supplier_data = df["Supplier"].dropna()

    if supplier_data.empty:
        print("\n Supplier data is missing in scraped dataset.")
        print("Supplier analysis skipped.\n")

    else:
        top_suppliers = supplier_data.value_counts().head(10)

        print("\nTop 10 Suppliers:")
        print(top_suppliers)

        # Plot Supplier Contribution
        plt.figure()
        top_suppliers.plot(kind="bar")
        plt.title("Top 10 Suppliers by Product Listings")
        plt.xlabel("Supplier")
        plt.ylabel("Number of Products")
        plt.show()


# Data Quality Checks
print("DATA QUALITY ISSUES")

print("\nMissing Values Per Column:")
print(df.isnull().sum())

# Check for duplicate products
duplicates = df.duplicated(subset=["Product_Name"]).sum()
print("\nDuplicate Product Titles:", duplicates)

# Products with very short names (possible noise)
short_titles = df[df["Product_Name"].str.len() < 10]
print("\nShort/Incomplete Titles Found:", len(short_titles))

# Insights Summary

print("KEY INSIGHTS :")


print("""

1. The dataset contains electronics product listings scraped from a B2B marketplace (Made-in-China).

2. Keyword analysis shows frequent terms like 'Custom', 'PCB', and 'High-Performance',
   indicating strong demand for industrial electronics and manufacturing components.

3. Supplier, Price, MOQ, and Product URL fields were missing in the scraped HTML response,
   highlighting common real-world marketplace scraping limitations.

4. Duplicate product titles were observed, suggesting repeated listings or similar products
   being offered by multiple vendors.

5. Data quality gaps such as missing attributes can impact deeper analysis like supplier ranking
   or pricing intelligence.

6. Overall, the collected electronics category shows clustering around customized and prototype
   electronic products, making it useful for trend-based marketplace insights.
""")

