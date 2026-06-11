#PHASE-1 DATA UNDERSTANDING AND DATA EXPLORATION
import pandas as pd
df = pd.read_csv (r"E:\python\nageshwar sir python\datasets1\titanic.csv")
print(df.head())

print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())


#PHASE-2 START
print("\n=== Survival Count ===")
print(df['Survived'].value_counts())
print("\n=== Gender Count ===")
print(df['Sex'].value_counts())
print("\n=== Survival Rate by Gender ===")
print(df.groupby('Sex')['Survived'].mean())
print("\n=== Survival Rate by Passenger Class ===")
print(df.groupby('Pclass')['Survived'].mean())
print("\n=== Average Age ===")
print(df['Age'].mean())
print("\n=== Youngest Passenger ===")
print(df['Age'].min())

print("\n=== Oldest Passenger ===")
print(df['Age'].max())

print("\n=== Highest Fare Paid ===")
print(df['Fare'].max())

print("\n=== Lowest Fare Paid ===")
print(df['Fare'].min())

df.groupby('Sex')['Age'].mean()

df.groupby('Pclass')['Fare'].mean()

df.groupby('Sex')['Fare'].max()

df.groupby('Pclass')['Age'].agg(['mean','min','max'])
print(df.groupby('Pclass')['Age'].agg(['mean','min','max']))


# phase 3
df.isnull().sum()
df["Age"] = df["Age"].fillna(df["Age"].mean())
df.isnull().sum()

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df.isnull().sum()


# Group by
df.groupby("Pclass")["Age"].agg(["mean", "min", "max", "count"])
df.groupby(["Pclass", "Sex"])["Fare"].mean()