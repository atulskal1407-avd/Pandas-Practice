# ===============================
# TITANIC DATA ANALYSIS PROJECT
# PHASE 1 - DATA UNDERSTANDING
# ===============================

import pandas as pd

# Load dataset
df = pd.read_csv(r"E:\python\nageshwar sir python\datasets1\titanic.csv")

# Basic exploration
print("=== HEAD ===")
print(df.head())

print("\n=== SHAPE ===")
print(df.shape)

print("\n=== COLUMNS ===")
print(df.columns)

print("\n=== INFO ===")
print(df.info())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())


# ===============================
# PHASE 2 - DATA ANALYSIS
# ===============================

print("\n=== SURVIVAL COUNT ===")
print(df['Survived'].value_counts())

print("\n=== GENDER COUNT ===")
print(df['Sex'].value_counts())

print("\n=== SURVIVAL RATE BY GENDER ===")
print(df.groupby('Sex')['Survived'].mean())

print("\n=== SURVIVAL RATE BY CLASS ===")
print(df.groupby('Pclass')['Survived'].mean())

print("\n=== AGE STATISTICS ===")
print("Mean Age:", df['Age'].mean())
print("Min Age:", df['Age'].min())
print("Max Age:", df['Age'].max())

print("\n=== FARE STATISTICS ===")
print("Max Fare:", df['Fare'].max())
print("Min Fare:", df['Fare'].min())

print("\n=== GROUPED ANALYSIS ===")

print("\nAge by Sex:")
print(df.groupby('Sex')['Age'].mean())

print("\nFare by Class:")
print(df.groupby('Pclass')['Fare'].mean())

print("\nMax Fare by Sex:")
print(df.groupby('Sex')['Fare'].max())

print("\nAge Stats by Class:")
print(df.groupby('Pclass')['Age'].agg(['mean', 'min', 'max']))


# ===============================
# PHASE 3 - DATA CLEANING
# ===============================

print("\n=== BEFORE CLEANING ===")
print(df.isnull().sum())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("\n=== AFTER CLEANING ===")
print(df.isnull().sum())


# ===============================
# FINAL GROUP ANALYSIS
# ===============================

print("\n=== AGE BY CLASS ===")
print(df.groupby("Pclass")["Age"].agg(["mean", "min", "max", "count"]))

print("\n=== FARE BY CLASS & GENDER ===")
print(df.groupby(["Pclass", "Sex"])["Fare"].mean())


#=========================================
#GROUP BY +SUM
#=========================================
print ("\n==TOTAL FARE BY CLASS==")
print (df.groupby("Pclass")["Fare"].sum())
#print(df.columns)
print("Program Started")
print("\n=== PASSENGER COUNT BY CLASS ===")

print(df.groupby("Pclass").size())
