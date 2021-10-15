import requests
import matplotlib.pyplot as plt
import json
from datetime import datetime
response = requests.get("https://api.nasa.gov/DONKI/FLR?startDate=2021-09-01&endDate=2021-10-01&api_key=zSbjNFJgVZ45n9AZcGLzR9GiNx2C8Ttd50oOf0hA")
json_data = response.json()
print(json_data)

#TEST TEST TEST

items = json_data[:]
active_region_num_arr = []
begin_time_arr = []
date_time_obj_arr = []
for item in items:
	flrID = item['activeRegionNum']
	active_region_num = item['beginTime']
	date_time_str = item['beginTime']
	date_time_obj = datetime.fromisoformat(date_time_str[:-1])

	active_region_num_arr.append(flrID)
	begin_time_arr.append(active_region_num)
	date_time_obj_arr.append(date_time_obj)
	#print(flrID)

print(active_region_num_arr)
print(begin_time_arr)
print(date_time_obj_arr)

#plt.plot(begin_time_arr, active_region_num_arr)
#plt.xlabel('Time (hr)')
#plt.ylabel('Position (km)')
#plt.show()

