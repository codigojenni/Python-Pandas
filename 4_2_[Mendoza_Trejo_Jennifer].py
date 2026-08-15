import pandas as pd
#load csv
df = pd.read_csv("students_again.csv")

#sort decending by math score
sorted_math_desc = df.sort_values('Math_Score', ascending=False)
print("Sorted Math Score (Descending):")
print(sorted_math_desc)

#sort by english score ascend.
sorted_english_asc = df.sort_values('English_Score', ascending = True)
print("Sorted English Score (Ascending):")
print(sorted_english_asc)

#reset index
sorted_math_reset = df.sort_values('Math_Score', ascending = False).reset_index(drop=True)
print("Index reset by Math Score:")
print(sorted_math_reset)

#sort science descending & math score ascending
sorted_science_math = df.sort_values(
    ['Science_Score', 'Math_Score'],
    ascending=[False, True]
    )
print("Science score descending & Math score ascending:")
print(sorted_science_math)
