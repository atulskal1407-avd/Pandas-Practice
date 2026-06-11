```python
import pandas as pd

# =====================
# DATAFRAME CREATION
# =====================

data = {
    "Emp_ID": [101, 102, 103, 104, 105],
    "Name": ["Atul", "Rahul", "Priya", "Neha", "Amit"],
    "Salary": [45000, 55000, 60000, 65000, 70000]
}

df = pd.DataFrame(data)

# =====================
# BASIC OPERATIONS
# =====================

print("First 5 Rows")
print(df.head())

print("\nName Column")
print(df["Name"])

print("\nName and Salary Columns")
print(df[["Name", "Salary"]])

# =====================
# FILTERING
# =====================

print("\nEmployees with Salary Greater Than 60000")
print(df[df["Salary"] > 60000])

# =====================
# AGGREGATION
# =====================

print("\nAverage Salary")
print(df["Salary"].mean())

print("\nMaximum Salary")
print(df["Salary"].max())

print("\nMinimum Salary")
print(df["Salary"].min())

# =====================
# NEW COLUMN CREATION
# =====================

df["Bonus"] = df["Salary"] * 0.10

print("\nDataFrame with Bonus Column")
print(df)

# =====================
# GROUPBY PRACTICE
# =====================

data2 = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Atul", "Rahul", "Priya", "Neha", "Amit", "Sneha"],
    "Department": ["Sales", "HR", "IT", "IT", "Sales", "HR"],
    "Salary": [45000, 55000, 60000, 65000, 70000, 52000]
}

df2 = pd.DataFrame(data2)

print("\nEmployee Data")
print(df2)

print("\nDepartment Wise Average Salary")
print(df2.groupby("Department")["Salary"].mean())

print("\nDepartment Wise Maximum Salary")
print(df2.groupby("Department")["Salary"].max())

print("\nDepartment Wise Employee Count")
print(df2.groupby("Department")["Salary"].count())

print("\nDepartment Wise Statistics")
print(df2.groupby("Department")["Salary"].agg(["mean", "max", "min", "count"]))

# =====================
# DESCRIBE FUNCTION
# =====================

print("\nSummary Statistics")
print(df2.describe())
