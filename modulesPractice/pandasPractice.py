import pandas
data = {'name': ['Connie', 'Jessica', 'Dana'], 'extension': [4682, 4198, 4351], 'location': ['New York', 'Los Angeles', 'Chicago']}
dataF = pandas.DataFrame(data, columns=['name', 'extension'])
print(dataF)

df_with_location = pandas.DataFrame(data, columns=['name', 'extension', 'location'], index=['a', 'b', 'c'])

print(df_with_location)