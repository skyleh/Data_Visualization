import csv
from setting import Settings

data_settings = Settings()
filename = data_settings.forest_area
with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    row_reader = next(reader)
    #print(row_reader)

    for row in reader:
        try:
            forest_areas = int(float(row[29]))
        except ValueError:
            continue
        else:
            print(str(forest_areas))
