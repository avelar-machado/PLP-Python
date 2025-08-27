import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Working with numpy
my_array = np.array([1, 9, 2, 8]);

print("Array: ", my_array);
print("");
print("Array * 2: ", my_array * 2);

print("Mean: ", np.mean(my_array));
print("Median: ", np.median(my_array));
print("Square Roots: ", np.sqrt(my_array));
print("Sort: ", np.sort(my_array));

new_array = np.array([i * 10 for i in range(1, 11) ]);
print("New array: ", new_array);
print("Max element using array: ", new_array.max());
print("Max element using numpy: ", np.max(new_array));

other_array = np.arange(10, 101, 10);
print("Other array: ", other_array);


# Working with pandas

# Create a DataFrame (table like structure)
data = {
    'Name' : ['Avelar', 'Manuel', 'Machado'],
    'Age': [21, 23, 25],
    'Score': [80, 90, 100]
}

print("");
print("Data: ", data);
print("Only Names: ", data["Name"]);

df = pd.DataFrame(data);

print("Data Frame: ", df);
print("Names: ", df['Name']);
print(df[df['Score'] > 80]);

dataFrame = pd.read_csv('dataset.csv');
print(dataFrame.head());


# Working with matplotlib

# 📈 Basic Line Plot
# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a line plot
plt.plot(x, y);
plt.title("Simple line Plot");
plt.xlabel("X-axis");
plt.ylabel("Y-axis");
plt.show();

# 📊 Bar Chart Example
# Sample data
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

plt.bar(names, scores, color='skyblue')
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()

# Pie Chart Example
# Sample data
activities = ['Sleeping', 'Eating', 'Coding', 'Gaming']
hours = [8, 2, 8, 6]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title("Daily Activities")
plt.show()

# Histogram Example
# Sample data
# Example: showing frequency of values
ages = [22, 21, 20, 23, 24, 22, 20, 21, 22, 25, 23]

plt.hist(ages, bins=5, color='purple')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Combine with Pandas Example
# Create a DataFrame
data = {
    'Year': [2021, 2022, 2023],
    'Users': [1500, 3000, 5000]
}

df = pd.DataFrame(data)

# Plot using pandas + matplotlib
plt.plot(df['Year'], df['Users'], marker='o')
plt.title("User Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Users")
plt.grid(True)
plt.show()