import pandas as pd
import numpy as np

print(pd.__version__)

data = {
    "product_id" : [101, 102, 103, 104, 105, 106, 107],
    "Product_name" : ['Laptop','Mouse','Keyboard','Monitor','Headphones','Printer','Tablet'],
    "Category": ['Electronics','Ascessories','Electronics','Ascessories','Electronics', 'Ascessories','Electronics'],
    'Price' : [70000,1200,2500,15000,3000,18000,25000],
    'Quantity': [5,50,40,10,35,7,15],
    'Discount': [10,5,5,8,10,15,7]
}

# df = pd.DataFrame(data)
# df['Revenue'] = df['Price'] * df['Quantity'] * (1-df['Discount']/100)
# df.head()


# df.to_csv("Sales_data_.csv", index=False)
# sales = pd.read_csv("Sales_data.csv")
# sales.head()


# df.tail()
# df.head()

# print(sales.describe())

# Selecting, indexing and filtering
# print(df['Product_name'] == 'laptop')


df1 = pd.read_csv("zomato.csv", encoding="latin-1")
# print(df1.info())

df2 = pd.read_excel("Country-code.xlsx")
print(df2.info())

# print("Rows : ", df1.shape[0])
# print("Columns : ",  df1.shape[1])

df_merge = pd.merge(df1, df2, how="left")
print(df1['Country Code'].unique)

# NA 
# Null
# NaN
# duplicate