import random
from datetime import datetime, timedelta

def generate_weather_data(year=2018):
    station = "USW00025333"
    location = "SITKA AIRPORT, AK US"
    start_date = datetime(year, 1, 1)
    days_in_year = 366 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 365

    data = []
    for day in range(days_in_year):
        date = (start_date + timedelta(days=day)).strftime("%Y-%m-%d")
        prcp = round(random.uniform(0.0, 1.5), 2)  # random precipitation
        tmax = random.randint(45, 70)              # high temp
        tmin = random.randint(tmax - 15, tmax - 5) # low temp (5–15° less than TMAX)
        line = f'"{station}","{location}","{date}","{prcp}",,"{tmax}","{tmin}"'
        data.append(line)
    
    return data

# Generate and save to file
weather_data = generate_weather_data(2018)
with open("CSV/sitka_weather_2018.csv", "w") as f:
    f.write("\n".join(weather_data))

print("Generated", len(weather_data), "rows.")
