import pandas as pd

#loading data
students = pd.read_csv("students.csv")
grades = pd.read_csv("grades.csv")

#merge data on ID
merged = pd.merge(students, grades, on="student_id")

#pivot table avg grade per student
pivot = merged.pivot_table(
    index="student_name",
    values="grade",
    aggfunc="mean"
    )
#print merged data
print("Merged Data:")
print(merged)

#print pivot table
print("--------------pivot table (avg/student)-------------")
print(pivot)

#save 
merged.to_csv("merged_data.csv", index=False)
pivot.to_csv("pivot_table.csv")
