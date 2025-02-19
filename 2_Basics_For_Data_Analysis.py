import seaborn as sns

print(sns.__version__)

df = sns.load_dataset("car_crashes")
df.columns

numeric_df = df.select_dtypes(include=['number']).columns # for numeric columns

df.columns = [f"NUM_{col}" if col in numeric_df else col for col in df.columns]
df.columns = [col.upper() for col in df.columns]
# output Index(['NUM_TOTAL', 'NUM_SPEEDING', 'NUM_ALCOHOL', 'NUM_NOT_DISTRACTED',
#       'NUM_NO_PREVIOUS', 'NUM_INS_PREMIUM', 'NUM_INS_LOSSES', 'ABBREV'],
#      dtype='object')

df = sns.load_dataset("car_crashes")
df.columns

df.columns = [f"{col.upper()}_FLAG" if col.lower().startswith('no') else col.upper() for col in df.columns]
# output Index(['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED_FLAG',
#       'NO_PREVIOUS_FLAG', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV'],
#      dtype='object')

import pandas as pd
df = sns.load_dataset("car_crashes")
df.head()

pd.set_option('display.max_rows', None) #show all rows
pd.set_option('display.max_columns', None) # show all columns
df.head()

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.info()
# output RangeIndex: 51 entries, 0 to 50
# Data columns (total 6 columns):
# #   Column          Non-Null Count  Dtype  
# ---  ------          --------------  -----  
# 0   total           51 non-null     float64
# 1   speeding        51 non-null     float64
# 2   alcohol         51 non-null     float64
# 3   not_distracted  51 non-null     float64
# 4   ins_premium     51 non-null     float64
# 5   ins_losses      51 non-null     float64
#dtypes: float64(6)
#memory usage: 2.5 KB


import seaborn as sns
import pandas as pd

df = sns.load_dataset("titanic")
df.head()
df.info
pd.set_option('display.max_columns', None)

df.nunique() # show uniqe data
df['who'].nunique()
df['embark_town'].nunique()
df[['parch', 'pclass']].nunique()

df['embarked'].describe().T
# output 
# count     889
# unique      3
# top         S
# freq      644
# Name: embarked, dtype: object

df['embarked'].dtype
# output object

df['embarked'] = df['embarked'].astype('category') # change the type

df['embarked'].dtype
# output category

df[df['embarked'] == "C"].head(5) # Shows those with embarked value C

df[df['embarked'] != "S"].head(5)

df[(df['age'] < 30) & (df['sex'] == "female")]

df[(df['fare'] > 500) | (df['age'] > 70)]
df[df['age'] > 70]

df.isnull().sum() # sum of null values ​​in each variable

df.drop("who", axis=1, inplace=True) # axis=1 columns, axis=0 rows, inplace=True changes the current dataframe
# We need to specify whether the item you want to delete is a row or a column
df.head()

df["deck"].mode()[0] # took the most repeated value
df["deck"].fillna(df["deck"].mode()[0], inplace=True) # placed the null values

df["age"].fillna(df["age"].median, inplace=True) # The median function calculates the middle value of a set of numeric values

df.groupby(["pclass", "sex"]).agg({"survived" : ["sum", "count", "mean"]})
df.groupby(["embarked", "sex"]).agg({"survived" : ["sum", "count", "mean"]})
# The agg() (aggregate) function is used to perform aggregate calculations after grouping operations in Pandas.

df["age_flag"] = df["age"].apply(lambda x: 1 if x < 30 else 0)
# apply(), used in the pandas library to apply functions on a DataFrame or Series.
df.head()




import seaborn as sns
df = sns.load_dataset("tips")
import pandas as pd

df.head()
pd.set_option("display.max_rows", None)
df["time"].describe().T
df["time"].nunique()
df["time"].value_counts()
df["time"]

df.groupby("time").agg({"total_bill" : ["sum", "min", "max", "mean"]})
df.groupby(["day", "time"]).agg({"total_bill" : ["sum"]})

df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill" : ["sum", "min", "max", "mean"],
                                                                          "tip" : ["sum", "min", "max", "mean"]})

df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"]
df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()

df.loc[(df["size"] < 3) & (df["total_bill"] > 10), ["total_bill", "size"]]
df.loc[(df["size"] < 3) & (df["total_bill"] > 10), ["total_bill", "size"]].mean()
# output loc is a label-based data selection method in Pandas. It is used to select rows and columns by their names.


df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df.head()

new_df = df.sort_values(by="total_bill_tip_sum", ascending=False)[:30]
# ascending=True → Sorts in ascending order (smallest to largest).
# ascending=False → Sorts in descending order (largest to smallest).
new_df.shape
new_df.head()
