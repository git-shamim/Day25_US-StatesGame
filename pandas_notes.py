
# open
with open("weather_data.csv", 'r') as data_file:
    data = data_file.readlines()
    print(data)

# csv
import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# pandas
import pandas_notes as pd
data = pd.read_csv("weather_data.csv")

print(data["temp"])

print(type(data))
print(type(data["temp"]))

temp_list = data["temp"].to_list()
print(temp_list)

avg_temp = sum(temp_list) / len(temp_list)
print(avg_temp)

print(data["temp"].mean())
print(data["temp"].max())

print(data["condition"])
print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday_row = data[data.day == "Monday"]
print(monday_row.condition)

monday_temp = int(monday_row.temp)
monday_temp_f = monday_temp * 9/5 + 32
print(monday_temp_f)

data_dictionary = data.to_dict()
print(data_dictionary)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new_data_file.csv")