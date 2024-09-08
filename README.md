Na kurzu jsme si připoměli pandas (práci s data frame) a matplotlib pro tvorbu grafu: 
Steps:
**1. Load the data:**
    ○ Read the sales_data.csv file into a Pandas DataFrame.
**2. Basic information:**
    ○ Display the first 10 rows of the DataFrame.
    ○ Show basic statistics for the numerical columns (Quantity and Price) using
the function .describe.
**3. Add new column:**
    ○ Create a new column called Total Sales that calculates the total sales amount
    for each transaction (Quantity * Price).
**4. Filter data:**
    ○ Filter the DataFrame to include only sales where the Total Sales is greater
    than $50.
**5. Grouping and aggregation:**
    ○ Group the filtered data by Product and calculate the total sales amount for each
    product.
    ○ Order by Total sales (use function .sort_values())
    ○ Identify top 3 products by total sales amount and display them.
**6. Simple data visualization:**
    ○ Plot a bar chart of the total sales for each product (from the grouped data).
    i. Use matplotlib barplot plt.bar
**7. Save the results:**
    ○ Save the filtered and grouped DataFrame into a new CSV file named
    filtered_sales_analysis.csv.
