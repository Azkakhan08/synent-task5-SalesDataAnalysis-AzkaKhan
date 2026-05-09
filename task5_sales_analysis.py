# Task 5 - Sales Data Analysis
# Dataset  - Superstore Sales Dataset
# Language - Python
# Run      - python task5_sales_analysis.py

import matplotlib.pyplot as plt
import pandas as pd

# define monthly sales data
data = {
    "month"   : ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "revenue" : [45000, 52000, 48000, 61000, 55000, 67000,
                 72000, 69000, 58000, 74000, 88000, 95000],
    "profit"  : [9000, 11000, 9500, 13000, 11500, 14000,
                 15000, 14500, 12000, 16000, 19000, 21000]
}

# define product data
data2 = {
    "product" : ["Phones", "Chairs", "Binders", "Tables", "Storage",
                 "Copiers", "Accessories", "Paper", "Bookcases", "Machines"],
    "sales"   : [95000, 74000, 42000, 68000, 32000,
                 55000, 48000, 22000, 36000, 61000],
    "profit"  : [15000, 8000, 9000, -5000, 6000,
                 18000, 12000, 7000, -2000, 14000]
}

# define region data
data3 = {
    "region"  : ["West", "East", "Central", "South"],
    "revenue" : [120000, 135000, 98000, 85000],
    "profit"  : [25000, 28000, 18000, 14000]
}

# create dataframes
df  = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)

# show monthly data
print("==============================")
print("     MONTHLY SALES DATA")
print("==============================")
print(df)
print()

# summary
print("==============================")
print("         SUMMARY")
print("==============================")
print("Total Revenue :", df["revenue"].sum())
print("Total Profit  :", df["profit"].sum())
print("Best Month    :", df.loc[df["revenue"].idxmax(), "month"])
print("Worst Month   :", df.loc[df["revenue"].idxmin(), "month"])
print()

# top products
print("==============================")
print("   TOP 3 PRODUCTS BY SALES")
print("==============================")
top3 = df2.sort_values("sales", ascending=False).head(3)
print(top3[["product", "sales"]])
print()

# setup figure and subplots
plt.figure(figsize=(14, 10))

# bar chart - monthly revenue
plt.subplot(2, 2, 1)
plt.bar(df["month"], df["revenue"],
        color="skyblue", edgecolor="black")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.title("Monthly Revenue Trend")
plt.xticks(rotation=45)

# line chart - monthly profit
plt.subplot(2, 2, 2)
plt.plot(df["month"], df["profit"],
         color="green", marker="o", linewidth=2)
plt.xlabel("Month")
plt.ylabel("Profit ($)")
plt.title("Monthly Profit Trend")
plt.xticks(rotation=45)

# horizontal bar chart - top 5 products
plt.subplot(2, 2, 3)
top5 = df2.sort_values("sales", ascending=False).head(5)
plt.barh(top5["product"], top5["sales"],
         color="lightgreen", edgecolor="black")
plt.xlabel("Sales ($)")
plt.title("Top 5 Products by Sales")

# bar chart - profit by region
plt.subplot(2, 2, 4)
plt.bar(df3["region"], df3["profit"],
        color="lightpink", edgecolor="black")
plt.xlabel("Region")
plt.ylabel("Profit ($)")
plt.title("Profit by Region")

# display
plt.tight_layout()
plt.savefig("task5_output.png")
plt.show()
print("Saved : task5_output.png")
