
import csv
import matplotlib.pyplot as plt
import numpy as np
from sys import argv
from os import path
from datetime import datetime

def split_date(data):
    data_splited = []
    for data in date:
        splited = data.split("/")
        data_splited.append(splited)
    return data_splited

def get_data_one_week(data_from_csv):
    statistics_date = []
    statistics_temperature = []
    statistics_time = []
    statistics_humidity = []
    for datum in data_from_csv:
        statistics_date.append(datum['date'])
        statistics_temperature.append(datum["temperature"])
        statistics_time.append(datum["time"])
        statistics_humidity.append(datum["humidity"])
    if len(statistics_date) > 2016:
        counter = (len(statistics_date) - 1016)
        date = []
        temp = []
        time = []
        humi = []

        while counter < len(statistics_date):
            date.append(statistics_date[counter])
            temp.append(statistics_temperature[counter])
            time.append(statistics_time[counter])
            humi.append(statistics_humidity[counter])
            print(counter)
            counter = (counter + 1)
    else:
        counter = 0
        date = []
        temp = []
        time = []
        humi = []
        while counter < len(statistics_date):
            date.append(statistics_date[counter])
            temp.append(statistics_temperature[counter])
            time.append(statistics_time[counter])
            humi.append(statistics_humidity[counter])
            print(counter)
            counter = (counter + 1)
        return date, temp, time, humi

def split_time(data):
    time_splited = []
    for x in data:
        splited = x.split(":")
        time_splited.append(splited)
    time_splited_named = []
    for data in time_splited:
        data = {
                        'hours': int(data[0]),
                        'minutes': int(data[1]),
                    }
        time_splited_named.append(data)
    return time_splited_named


def split_year_month_day(ydm):
    ''' spaltet die daten in month, day und year
    '''
    data_split_named = []
    for data in ydm:
        data = {
                        'month': int(data[0]),
                        'day': int(data[1]),
                        'year': int(data[2]) + 2000,
                    }
        data_split_named.append(data)
    return data_split_named


def read_csv(filename):
    """ 
    öffnet das csv file und gibt es als liste mit dicts aus.
    """
    stats = []

    with open(filename, 'r') as csv_file:
        csv_reader  = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                data = {
                    'date': row[0],
                    'time': row[1],
                    'temperature': row[2],
                    'humidity': row[3],

                }
                stats.append(data)
                line_count += 1
    return stats


def draw_plot(x, y, x_label, y_label, title):
    """Zeichnet einen Graphen mit der Hilfe von matplotlib

    Args:
        x - Eine Liste von Jahreszahlen (x Achse)
        y - Eine Liste von Werten (y Achse)
        x-lable - Horizontale Beschriftung
        y-lable - Vertikale Beschriftung
        title - Titel
    """
    plt.plot(x, y)
#    plt.xticks = np.arange(min(x), max(x), 2)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

humidity = read_csv("data.csv")
date, temp, time, humi = get_data_one_week(humidity)
print(date, temp, time, humi)
data_splited = split_date(date)
time_splited = split_time(time)
print(time_splited)
time_data_named = split_year_month_day(data_splited)
print(time_data_named)

daytime_last_weak = []
for item in time_data_named:
    daytime_one = datetime(item["year"], item["month"], item["day"])
    daytime_last_weak.append(daytime_one)
print(daytime_last_weak)

draw_plot(daytime_last_weak,temp,"hallo", "ca", "loool")













#for x in date:
#    x.replace("*C", "")
#temp = [ (x) for x in temp ]






    
