with open("weather_data.csv") as weather:
    data = weather.readlines()
    print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    # print(data)
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)
