# with open("weather_data.csv")as data_file:
#     data=data_file.readlines()
# print(data)

# import csv
# with open("weather_data.csv")as data_file:
#     data=csv.reader(data_file)
#     tempratures=[]
#     for row in data:
#         if row[1]!="temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)

import pandas
data=pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])
