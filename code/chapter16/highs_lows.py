import csv
import matplotlib.pyplot as plt
from datetime import datetime
from settings import Settings

data_settings = Settings()
filename = data_settings.death_valley_2014
#打开csv文件
with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    row_header = next(reader)

    #获取气温，日期
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            low = int(row[3])
            high = int(row[1])
        except ValueError:
            print(current_date, "missing data")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

#绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#设置图像属性
plt.title("Daily high and low temperatures, 2014",fontsize=14)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)

plt.show()

