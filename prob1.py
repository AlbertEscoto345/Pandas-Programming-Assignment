#Copy lines 2 to 5 first and paste them to console.
import pandas as pd
df = pd.read_csv('cars.csv')
print("First 5 rows:")
df.loc[[0,1,2,3,4]]
#Now, copy lines 7 and 8 then paste them to console.
print("Last 5 rows:")
df.loc[[27,28,29,30,31]]