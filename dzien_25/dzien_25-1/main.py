# Without csv library
# weather_lines =[]
#
# with open("weather_data.csv") as weather_file:
#     for line in weather_file:
#         data = line.strip()
#         weather_lines.append(data)
#
# print(weather_lines)

# With csv library
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if  row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# With Pandas library

# import pandas
# from numpy.ma.extras import average
#
# data = pandas.read_csv("weather_data.csv")

# print(data)
# print(type(data))
# print(data["temp"])

# Convert data to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# Convert data to list
# temp_list = data["temp"].tolist()
# print(temp_list)

# print average value
# avg_temp = average(temp_list)
# print(round(avg_temp, 2))

# print max temperature
# max_temp = data["temp"].max()
# print(max_temp)

#Get data in row
# print(data[data["day"] == "Monday"])

#print data in row which have the highest temperature
# print(data[data["temp"] == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp
# monday_temp = monday_temp * 9/5 +32
# print(monday_temp)

#Create dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "Scores" : [76, 56, 65]
# }
#
# pandas.DataFrame(data_dict).to_csv("students.csv")

#Working with 2018_Central_Park_Squirrel_Census

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

pandas.DataFrame(data_dict).to_csv("Squirrels_Count.csv")
