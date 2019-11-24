#Kindly copy and paste the lines below one-by-one in order to avoid problems in displaying the outputs.
import pandas as pd
cars = pd.read_csv('cars.csv')
# a)
soln_a = cars.loc[[1,3,5,7,9]]
print(soln_a)
# b)
soln_b = cars[(cars['Model']=='Mazda RX4')]
print(soln_b)
# c)
soln_c = cars.loc[[23],['cyl']]
print(soln_c)
# d)
cars.loc[cars['Model'] == 'Mazda RX4 Wag', ['cyl', 'gear']]
cars.loc[cars['Model'] == 'Ford Pantera L', ['cyl', 'gear']]
cars.loc[cars['Model'] == 'Honda Civic', ['cyl', 'gear']]