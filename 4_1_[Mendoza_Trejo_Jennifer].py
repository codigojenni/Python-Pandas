import pandas as pd

#loading csv

df = pd.read_csv("students_again.csv")

#print first 5 rows
print(df.head())

#select only name & math columns
selected_columns = df[['Name', 'Math_Score']]
print(selected_columns)

filtered_students = df[df['Math_Score'] > 80]
print(filtered_students)

#filter names of students who scored above 80 in math
high_math_scores = df[df['Math_Score']> 80] ['Name']
print(high_math_scores)
