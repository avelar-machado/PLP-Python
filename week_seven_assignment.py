import pandas as pd
import matplotlib.pyplot as plt
import os

# 0️⃣ Criar sales_data.csv se não existir
if not os.path.exists("sales_data.csv"):
    sample_data = """Date,Product,Quantity Sold,Revenue ($)
2025-03-01,Laptop,5,5000
2025-03-01,Mouse,15,300
2025-03-02,Laptop,3,3000
2025-03-02,Keyboard,8,800
2025-03-03,Mouse,10,200
2025-03-03,Laptop,2,2000
"""
    with open("sales_data.csv", "w") as f:
        f.write(sample_data)

# 1️⃣ Carregar CSV
df = pd.read_csv("sales_data.csv")

# 2️⃣ Calcular receita total
total_revenue = df["Revenue ($)"].sum()

# 3️⃣ Melhor produto em quantidade vendida
best_product = df.groupby("Product")["Quantity Sold"].sum().idxmax()
best_quantity = df.groupby("Product")["Quantity Sold"].sum().max()

# 4️⃣ Dia com maior receita
best_day = df.groupby("Date")["Revenue ($)"].sum().idxmax()
best_day_revenue = df.groupby("Date")["Revenue ($)"].sum().max()

# 5️⃣ Guardar resumo em ficheiro
summary = (
    f"Total Revenue: ${total_revenue:,.0f}\n"
    f"Best-Selling Product: {best_product} ({best_quantity} units sold)\n"
    f"Highest Sales Day: {best_day} (${best_day_revenue:,.0f})\n"
)

with open("sales_summary.txt", "w") as f:
    f.write(summary)

# 6️⃣ Mostrar no terminal
print("📊 Sales Summary")
print(summary)

# 🎯 Bonus: Visualizar tendência de vendas
daily_sales = df.groupby("Date")["Revenue ($)"].sum()

plt.figure(figsize=(8, 4))
plt.plot(daily_sales.index, daily_sales.values, marker="o", color="b")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.show()
