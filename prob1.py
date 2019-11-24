#Copy lines 2 to 5 first and paste them to console.
import pandas as pd
cars = pd.read_csv('cars.csv')
print("First 5 rows:")
cars.loc[[0,1,2,3,4]]
#Now, copy lines 7 and 8 then paste them to console.
print("Last 5 rows:")
cars.loc[[27,28,29,30,31]]
#Copy and paste the lines of code below to console in order to display the answers to the subproblem b.
soln_b1 = cars.loc[[0,1,2,3,4]] 
soln_b2 = cars.loc[[27,28,29,30,31]]