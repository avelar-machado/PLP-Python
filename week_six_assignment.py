import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# 1️⃣ NumPy: array de 1 a 10 e calcular a média
arr = np.arange(1, 11)  # números de 1 a 10
print("NumPy Array:", arr)
print("Mean:", np.mean(arr))

# 2️⃣ Pandas: criar DataFrame e mostrar estatísticas
data = {
    "Name": ["Ana", "Carlos", "Beatriz", "David"],
    "Age": [23, 35, 29, 41],
    "Score": [89, 72, 95, 68]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)
print("\nSummary statistics:")
print(df.describe())

# 3️⃣ Requests: buscar dados de uma API pública (JSONPlaceholder)
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
if response.status_code == 200:
    todo = response.json()
    print("\nFetched from API:")
    print("Title:", todo["title"])
    print("Completed:", todo["completed"])
else:
    print("\nFailed to fetch data from API")

# 4️⃣ Matplotlib: plotar gráfico simples
y = [2, 4, 6, 8, 10]
x = range(1, 6)

plt.plot(x, y, marker="o", linestyle="-", color="b")
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
