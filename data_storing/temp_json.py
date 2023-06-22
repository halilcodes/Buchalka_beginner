import json
import requests

# with open('temperature_anomaly.json', 'r', encoding='UTF8') as temp_data:
#     data = json.load(temp_data)

temp_data = requests.get(url='https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series'
                             '/globe/land_ocean/1/10/1880-2022.json')
data = temp_data.json()

for year, value in data['data'].items():
    year, value = int(year), float(value)
    print(f"{year} ... {value:6.2}")
