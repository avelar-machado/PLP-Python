# =============================================
# Assignment: Data Analysis with Pandas & Matplotlib
# Author: Avelar Machado
# Date: 27/08/2025
# =============================================

# ---- Import Libraries ----
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ---- Task 1: Load and Explore the Dataset ----
try:
    # Load Iris dataset
    iris = load_iris(as_frame=True)
    df = iris.frame

    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: File not found.")
except Exception as e:
    print("❌ An error occurred:", e)

# Show first rows
print("🔹 First 5 rows of the dataset:")
print(df.head())

# Dataset structure
print("\n🔹 Dataset information:")
print(df.info())

# Check for missing values
print("\n🔹 Missing values:")
print(df.isnull().sum())

# (If there were missing values, fill or drop them)
df = df.dropna()

# ---- Task 2: Basic Data Analysis ----
print("\n🔹 Descriptive statistics:")
print(df.describe())

# Group by species and calculate means
print("\n🔹 Mean values by species:")
grouped = df.groupby("target").mean()
print(grouped)

# Note: species (target) = 0 → setosa, 1 → versicolor, 2 → virginica

# ---- Task 3: Data Visualization ----

# Seaborn style
sns.set(style="whitegrid")

# 1️⃣ Line Chart - simulated time series with sepal length
plt.figure(figsize=(8,4))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Chart - Sepal Length Over Index")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2️⃣ Bar Chart - average sepal length by species
plt.figure(figsize=(6,4))
sns.barplot(x=iris.target_names, y=df["sepal length (cm)"], hue=df["target"], estimator="mean", dodge=False, palette="viridis")
plt.title("Bar Chart - Average Sepal Length by Species")
plt.xlabel("Species")
plt.ylabel("Avg Sepal Length (cm)")
plt.legend([],[], frameon=False)  # remove duplicate legend
plt.show()

# 3️⃣ Histogram - distribution of petal length
plt.figure(figsize=(6,4))
plt.hist(df["petal length (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Histogram - Petal Length Distribution")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4️⃣ Scatter Plot - relationship between sepal and petal length
plt.figure(figsize=(6,4))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue=df["target"], palette="Set1", data=df)
plt.title("Scatter Plot - Sepal vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species", labels=iris.target_names)
plt.show()
