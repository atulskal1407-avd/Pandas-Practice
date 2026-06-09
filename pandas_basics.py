import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105],
    "Name": ["Atul", "Rahul", "Priya", "Neha", "Amit"],
    "Salary": [45000, 55000, 60000, 65000, 70000]
}

df = pd.DataFrame(data)
df.head()
print (df.head())
print (df['Name'])
print (df[["Name","Salary"]])
#"Salary":[45000,55000,60000,65000,70000]
print(df[df["Salary"]>60000])
print (df["Salary"].mean())
print(df["Salary"].max())
df["Bonus"]=df["Salary"] *0.10
print(df)
# GROUP BY
# Basic Pandas Practice

import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Atul", "Rahul", "Priya", "Neha", "Amit", "Sneha"],
    "Department": ["Sales", "HR", "IT", "IT", "Sales", "HR"],
    "Salary": [45000, 55000, 60000, 65000, 70000, 52000]
}

df = pd.DataFrame(data)

print(df)

print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].max())
df.groupby("Department")["Salary"].count()
print (df.groupby("Department")["Salary"].count())
print ((df.groupby('Department')) ["Salary"].agg(["mean","max","min","count"]))
print(df.describe())