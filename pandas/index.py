# Pandas = working with structured/tabular data efficiently

# two Most important pandas objects that is, Series and Data frame
# Series is a single column data, A pandas 1-dimensional labeled array that can hold any data type. Think of it like single column in a spreadsheet(1-dimensional)
# DataFrame is the whole table

# So series and numpy are same thing right, because we can create data in both, like in numpy, we create an array and in series we give the data as same, BUT no its different because, the pandas gives your data an index, hell you can even make your own index

# A DataFrame is basically multiple Series placed side-by-side with a shared index. 

import pandas as pd

# data = [100.1, 102.2, 104.4, 'A', 'B', 'C', True, False]
# series = pd.Series(data, index=[1,2,3,4,5,6,7,8])

# series.loc[4] = "Bsdk"

# print(series)
# print(series.loc[2]) # loc - location by label
# print(series.iloc[4]) # location by integer



# data2 = [100,101,102,103,104]
# series2 = pd.Series(data2, index=["a","b","c","d","e"])
# print(series2[series2 <=101])


# ----- Dataframe
# data = {
#     "Name": ["SpongeBob", "Patrick","Squidward"],
#     "Age": [30, 35, 50]
#     }

# df = pd.DataFrame(data, index=[1,2,3])

# #Add a column
# df["Job"] = ["Cook", "N/A", "Cashier"]

# #Add a new row 
# new_row = pd.DataFrame(
#     [{"Name": "Sandy", "Age": 28, "Job": "Engineer"},
#     {"Name": "Anirudh", "Age": 20, "Job": "Intern"}], index=[4,5])
# df = pd.concat([df, new_row])

# print(df)


# --------- Importing
df = pd.read_csv("/mnt/Ad1Here/Python/Data File/data.csv", index_col="Name")

# Selection by column

# print(df["Name"].to_string())
# print(df["Weight"].to_string())
# print(df[["Name", "Height", "Weight"]].to_string())

# Selection by row 
# print(df.loc[25])
# print(df.loc[6:50, ["Height", "Name"]])

# print(df.iloc[0:11:2, 0:3])


# pokemon = input("Enter a Pokemon Name: ")
# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found")


# --------- FILTERING

# tall_pokemon = df[df["Height"] >= 2]
# heavy_poke = df[df["Weight"] >= 100]
#legend_poke = df[df["Legendary"] == 1]
# water_poke = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
# ff_poke = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]

# print(ff_poke)


# ---------- Aggregate Function = Reeduces a set of values into a single summary value used to summarize and analyze data. Often Used with the groupby() function

# -- Whole DataFrame
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# -- Single Column
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())

# group = df.groupby("Type1")  # groupby() splits your DataFrame into groups based on a column's values, lets you apply a function to each group, and combines the results.
# print(group["Height"].mean())
# print(group["Height"].sum())
# print(group["Height"].min())
# print(group["Height"].max())


# --------- Data Cleaning

# 1. Drop irrelevant columns
# df1 = df.drop(columns=["Legendary"])

# 2. Handle missing data
# df2 = df.dropna(subset=["Type2"])
# df2 = df.fillna({"Type2": "None"})

# 3. Fix inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS", "Fire": "FIRE", "Water": "WATER"})

# 4. standardize Text
# df["Name"] = df["Name"].str.lower()

# 5. Fix Data Types
# df["Legendary"] = df["Legendary"].astype(bool)

# 6. Removing Duplicate Values
df = df.drop_duplicates()

print(df)



