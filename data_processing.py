import numpy as np
#from math import e
import matplotlib.pyplot as plt
import pandas as pd
import csv

data = pd.read_csv('complete_laptop_data0.csv', delimiter=',', encoding='ISO-8859-1')
newdata = data[data['Processor Brand'].isin(['Intel', 'AMD'])]
newdata2 = newdata[newdata['Processor Name'].isin(['Ryzen 7 Octa Core', 'Ryzen 7 Dual Core', 'Ryzen 3 Quad Core', 'Ryzen 9 Octa Core', 'Ryzen 5 Hexa Core', 'Ryzen 5 Quad Core', 'Ryzen 7 Hexa Core', 'Ryzen 7 Quad Core', 'Ryzen 5 Dual Core', 'Ryzen 3 Dual Core', 'Ryzen 5 Octa Core', 'Ryzen 3 Hexa Core', 'Core i9', 'Core i5', 'Core i7', 'Core i3', 'Hexa Core i5', 'Octa Core i7'])]
df2 = newdata2.copy()
df2["brand"] = df2["name"].str.split(" ").str[0]
df2["price"] = df2["Price"].str.replace("?", "").str.replace(",", "")
df2["processor clock speed"] = df2["Clock Speed"].str.extract(r"([-+]?\d*\.\d+|\d+)")
df2["SSD"] = df2["SSD"].str.replace(" ", "").str.replace("Yes", "true").str.replace("No", "false")
df2["drive capacity"] = df2["SSD Capacity"].combine_first(df2["HDD Capacity"])
df2["RAM"] = df2["RAM"].str.replace("GB", "").astype(int)
df2["screen size"] = df2["Screen Size"].str.split(" ").str[2].str.replace("(","")
df2["weight"] = df2["Weight"].str.split(" ").str[0]
df2["speakers"] = df2["Speakers"].isnull() == False
df2["touchscreen"] = df2["Touchscreen"].str.replace(" ", "").isnull() == False
df2["microphone"] = df2["Internal Mic"].isnull() == False
df2["webcam"] = df2["Web Camera"].isnull() == False
df2 = df2[["name", "brand", "price", "Processor Brand", "Processor Name", "Processor Generation", "processor clock speed", "Number of Cores", "SSD", "drive capacity", "RAM", "Dedicated Graphic Memory Capacity", "screen size", "Screen Resolution", "weight", "speakers", "touchscreen", "microphone", "webcam"]]
df2['drive capacity'] = df2['drive capacity'].str.replace(' TB', '000 GB').str.replace(' GB', '').astype(float)
print(df2.head())
df2.to_csv("processed_laptop_data2.csv", index=False)
