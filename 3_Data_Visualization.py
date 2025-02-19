# Data Visualization

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = sns.load_dataset("titanic")
df["sex"].value_counts().plot(kind='bar') # in categorical variables
plt.show() # displays the plot on the screen when using Matplotlib
# plt.show(block=True)  if plt.show() doesn't work you can use like this

plt.hist(df["age"]) # in numeric variables
plt.show()

df.head()

x = np.array([1, 4, 7, 9])
y = np.array([7, 9, 8, 12])

plt.plot(x, y)
plt.show()

plt.plot(x, y, "o")
plt.show()

plt.plot(y, marker="*")
plt.show()

y = np.array([7, 8, 9, 12])
plt.plot(y, linestyle="dashdot", color="r")
plt.title("Title")
plt.ylabel("y title")
plt.xlabel("x title")
plt.grid()
plt.show()

# subplot(): The function is used to divide a graphic area (figure) into multiple subplots
plt.subplot(2, 1, 1)  # 2 rows, 1 columns, 1. graph
plt.plot([1, 2, 3], [4, 5, 6])  # A simple line graph
plt.title("First Graph")

plt.subplot(2, 1, 2)  # 2 rows, 1 columns, 2. graph
plt.plot([1, 2, 3], [6, 5, 4])  # Second line graph
plt.title("Second Graph")

plt.show()

x = np.linspace(0, 10, 100) # create 100 equally spaced points between 0 and 10 for the x-axis
y1 = np.sin(x) 
y2 = np.cos(x)

plt.subplot(2, 1, 1)
plt.plot(x, y1, label="sin(x)")
plt.legend()
plt.title("sin function")

plt.subplot(2, 1, 2)
plt.plot(x, y2, label="cos(x)", color='r')
plt.legend()
plt.title("cos function")

plt.tight_layout()  # Prevents subplots from interfering with each other
plt.show()



df = sns.load_dataset("tips")
df["sex"].value_counts()
sns.countplot(x=df["sex"], data=df) # for categorical variables with seaborn
plt.show()

sns.boxplot(x=df["total_bill"]) # different graph type
plt.show()

df["total_bill"].hist() # different graph type
plt.show()

df.head()
df.select_dtypes(['category', 'object', 'bool'])
[col for col in df.columns if (str(df[col].dtypes) in ['category', 'object', 'bool'])]

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name : dataframe[col_name].value_counts(),
                        "radito" : 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("*************")

cat_summary(df, "sex")
cat_summary(df, "total_bill")


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name : dataframe[col_name].value_counts(),
                        "radito" : 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("--------------")

    sns.countplot(x=dataframe[col_name], data=dataframe)
    plt.show()


def summarize_categorical_columns(dataframe):
    cat_cols = [col for col in df.columns if (str(df[col].dtypes) in ['category', 'object', 'bool'])]
    for col in cat_cols:
        if df[col].dtype == "bool":
            df[col] = df[col].astype(int)

        cat_summary(df, col)

cat_summary(df, "size")
cat_summary(df, "total_bill")

summarize_categorical_columns(df)


import matplotlib.pyplot as plt

notes = [68, 74, 82, 90, 78, 85, 92, 88, 76, 61, 79, 73, 89, 81, 72, 95, 70, 83, 77, 75]

plt.hist(notes, bins=10, edgecolor='r', alpha=0.7)
plt.xlabel('Notes')
plt.ylabel('Frequency')
plt.title('Exam Scores Distribution')
plt.show()