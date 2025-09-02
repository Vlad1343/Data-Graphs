# import csv
# filename = 'CSV/sitka.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     for index, column_header in enumerate(header_row):
#         print(index, column_header)
    


# import csv
# filename = 'CSV/sitka.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
    
#     # Get high temperatures from this file.
#     highs = []
#     for row in reader:
#         high = int(row[5])
#         highs.append(high)
# print(highs)




# import csv
# from datetime import datetime
# import matplotlib.pyplot as plt

# filename = 'CSV/sitka.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
    
#     # Get dates and high temperatures from this file.
#     dates, highs = [], []
#     for row in reader:
#         current_date = datetime.strptime(row[2], "%Y-%m-%d")
#         high = int(row[5])
#         dates.append(current_date)
#         highs.append(high)
        
# # Make a graph for high temperatures.
# plt.style.use('ggplot')
# fig, ax = plt.subplots()
# ax.plot(dates, highs, c='red')

# # Format plot.
# plt.title("Daily high temperatures, July 2018", fontsize=24)
# plt.xlabel('', fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)

# plt.show()





##Best

# import csv
# from datetime import datetime
# import matplotlib.pyplot as plt

# filename = 'CSV/sitka_weather_2018.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
    
#     # Get the information from this file.
#     dates, highs, lows = [], [], []
#     for row in reader:
#         current_date = datetime.strptime(row[2], "%Y-%m-%d")
#         high = int(row[5])
#         low = int(row[6])
#         dates.append(current_date)
#         highs.append(high)
#         lows.append(low)

# # Sample the data to reduce clutter (e.g., every 7th day)
# sample_interval = 7
# sampled_dates = dates[::sample_interval]
# sampled_highs = highs[::sample_interval]
# sampled_lows = lows[::sample_interval]

# # Create subplots for better clarity
# plt.style.use('ggplot')
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# # Plot high temperatures
# ax1.plot(sampled_dates, sampled_highs, c='red', marker='o', linestyle='-', label='Highs')
# ax1.set_title("Daily High Temperatures - 2018", fontsize=16)
# ax1.set_ylabel("Temperature (F)", fontsize=12)
# ax1.legend(fontsize=10)
# ax1.grid(True, linestyle='--', alpha=0.5)

# # Plot low temperatures
# ax2.plot(sampled_dates, sampled_lows, c='blue', marker='o', linestyle='-', label='Lows')
# ax2.set_title("Daily Low Temperatures - 2018", fontsize=16)
# ax2.set_xlabel("Date", fontsize=12)
# ax2.set_ylabel("Temperature (F)", fontsize=12)
# ax2.legend(fontsize=10)
# ax2.grid(True, linestyle='--', alpha=0.5)

# plt.tight_layout()
# plt.show()







import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'CSV/sitka_weather_2018.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get the information from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
# Make a graph
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

