#import csv
import pandas as pd
df = pd.read_csv("sales_data.csv")
print(df.to_string())

#100 záznamů, Date, Product, Quantuty, Price

#Zobrazit prvních 10 řádků
result = df.head(10)
print("First 10 rows of the DataFrame:")
print(result)

#Zobrazit statistiku pro sloupce Quantity and Price s použitím funkce .describe.

df['Quantity'].describe()
df['Price'].describe()
print(df.describe()) 

#Přidat nový sloupec: Total Sales

df['Total Sales'] = df['Quantity'] * df['Price']
print(df.to_string())

#Filtr (Total Sales větší než $50)
filtered_df = df[df["Total Sales"] > 50] 
print(filtered_df)

#Grupace
    #zgrovat dle produktu a spočítat total sales pro každý produkt.
    #order by Total sales (.sort_values())

grouped_df = filtered_df.groupby("Product").sum("Total Sales").reset_index().sort_values(by="Total Sales", ascending=False)
print(grouped_df)
#Dotaz: proč se používá reset_index: groupby mění index na index sloupce, kde se grupuje (produkt) - po resetu produkt (string) už není indexem, nově index je opět 0,1,2

    #určit top 3 nejprodávanějších produktů.
grouped_df = filtered_df.groupby("Product").sum("Total Sales").reset_index().sort_values(by="Total Sales", ascending=False).head(3)
print(grouped_df)

#Vizualizace
    #udělat bar chart prodejů pro každý produkt (sgrupovaná data) pomocí matplotlib barplot plt.bar

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.bar(grouped_df['Product'], grouped_df['Total Sales'], color="skyblue")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

#Uložit výsledky do nového csv: filtered_sales_analysis.csv.
grouped_df.to_csv("filtered_sales_analysis.csv", index=False)
print("yes")