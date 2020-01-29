import csv
import matplotlib.pyplot as plt
import numpy as np
from sys import argv
from os import path
from datetime import datetime
import matplotlib.dates as mdates
    
def split_date(data):
    data_splited = []
    for data in date:
        splited = data.split("/")
        data_splited.append(splited)
    return data_splited

def get_data_one_week(data_from_csv):

    data_last_week = []
    if len(data_from_csv) > 1016:
        data_last_week = data_from_csv[-1016:]
    else:
        data_last_week = data_from_csv

    return data_last_week

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
                print(row)
                if len(row) == 4:
                    data = {
                        'date': row[0],
                        'time': row[1],
                        'temperature': row[2],
                        'humidity': row[3],

                }
                stats.append(data)
                line_count += 1
    return stats


def draw_plot(x, y, x_label, y_label, title, title_doc):
    """Zeichnet einen Graphen mit der Hilfe von matplotlib

    Args:
        x - Eine Liste von Jahreszahlen (x Achse)
        y - Eine Liste von Werten (y Achse)
        x-lable - Horizontale Beschriftung
        y-lable - Vertikale Beschriftung
        title - Titel
    """
    time_x = []
    for item in x:
        np_time = np.datetime64(item)
        time_x.append(np_time)
    print(time_x)
    plt.clf()
    datemin = np.datetime64(x[0])
    datemax = np.datetime64(x[-1])
    plt.yticks = np.arange(1, 200, 2)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=2))
    plt.gcf().autofmt_xdate()
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(x,y)
    plt.savefig(title_doc)

def merge_date_time(date, time):
    month, day , year = date.split("/")
    hour, daytime = time.split(":")

    print(date, time)
    print(datetime(int(year)+ 2000, int(month), int(day), int(hour), int(daytime)))
    return datetime(int(year)+ 2000, int(month), int(day), int(hour), int(daytime))

humidity = read_csv("data.csv")
data_last_week = get_data_one_week(humidity)

for item in data_last_week:
    item['timestamp'] = merge_date_time(item['date'], item['time'])
    print(item)




print(data_last_week)
temp = []
time = []
humi = []
for item in data_last_week:
    temp.append(float(item["temperature"]))
    time.append(item["timestamp"])
    humi.append(item["humidity"])

draw_plot(time,humi ,"Datum", "Luftfeuchtigkeit in %", "Luftfeuchtigkeit in % über eine Woche", "humidity.png")
draw_plot(time,temp ,"Datum", "Temperatur in *C", "Temperatur in *C über eine Woche","temperatur.png")








