import requests
import matplotlib.pyplot as plt
import json
import pandas as pd

response = requests.get("https://api.nasa.gov/DONKI/FLR?startDate=2021-09-01&endDate=2021-10-01&api_key=zSbjNFJgVZ45n9AZcGLzR9GiNx2C8Ttd50oOf0hA")
json_data = response.json()
print(json_data)

df = pd.json_normalize(json_data)
df['duringTime'] = (pd.to_datetime(df.endTime) - pd.to_datetime(df.beginTime))
df['duringTimeHighPoint'] = (pd.to_datetime(df.peakTime) - pd.to_datetime(df.beginTime))
print(df['duringTime'])

data_nasa = [df["flrID"], df["duringTime"], df["duringTimeHighPoint"], df["classType"], df["sourceLocation"], df["activeRegionNum"]] #create data
data_frame_nasa = pd.concat(data_nasa, axis=1) #create data frame from data
print(data_frame_nasa)
print(data_frame_nasa.duringTimeHighPoint)
print(data_frame_nasa.duringTime)

