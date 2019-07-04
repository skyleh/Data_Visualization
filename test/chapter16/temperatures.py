import csv
from setting import Settings
import matplotlib.pyplot as plt
from datetime import datetime

data_settings = Settings()
filename_1 = data_settings.sitka_weather_2014
filename_2 = data_settings.death_valley_2014

with open(filename_1) as f_obj_1:
    reader_1 = csv.reader(f_obj_1)
    row_header_1 = next(reader_1)

    dates_1, highs_1, lows_1 = [], [], []
    for row_1 in reader_1:
        try:
            current_date_1 = datetime.strptime(row_1[0], "%Y-%m-%d")
            low_1 = int(row_1[3])
            high_1 = int(row_1[1])
        except ValueError:
            print(current_date_1, "missing data")
        else:
            highs_1.append(high_1)
            lows_1.append(low_1)
            dates_1.append(current_date_1)

with open(filename_2) as f_obj_2:
    reader_2 = csv.reader(f_obj_2)
    row_header_2 = next(reader_2)

    dates_2, highs_2, lows_2 = [], [] ,[]
    for row_2 in reader_2:
        try:
            current_date_2 = datetime.strptime(row_2[0], "%Y-%m-%d")
            low_2 = int(row_2[3])
            high_2 = int(row_2[1])
        except ValueError:
            print(current_date_2, "missing data")
        else:
            dates_2.append(current_date_2)
            highs_2.append(high_2)
            lows_2.append(low_2)


#绘制图形
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates_1, highs_1, c='red', alpha=0.5)
plt.plot(dates_1,lows_1,c='blue', alpha=0.5)
plt.fill_between(dates_1, highs_1, lows_1, facecolor='blue', alpha=0.1)

plt.plot(dates_2, highs_2, c='purple', alpha=0.5)
plt.plot(dates_2,lows_2,c='green', alpha=0.5)
plt.fill_between(dates_2, highs_2, lows_2, facecolor='green', alpha=0.1)

#设置坐标轴
plt.title("Temperatures in 2014",fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',labelsize=16)

plt.show()
