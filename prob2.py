import pandas as pd
df = pd.read_csv('cars.csv')
# a)
df.loc[[1,3,5,7,9]]
# b)
df[(df['Model']=='Mazda RX4')]
# c)
df.loc[[23],['cyl']]
# d)
df.loc[df['Model'] == 'Mazda RX4 Wag', ['cyl', 'gear']]
df.loc[df['Model'] == 'Ford Pantera L', ['cyl', 'gear']]
df.loc[df['Model'] == 'Honda Civic', ['cyl', 'gear']]