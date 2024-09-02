import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r'C:\Users\JodaBook\Documents\Python\Python\names.csv')
#print(df.head())

name = "Natalie"
gender = "F"
State = "CA"

df2 = df[df["Name"] == name]
df3 = df2[df["Gender"] == gender]
df4 = df3[df["State"] == State]

df5 = (df4.sort_values("Year"))

plt.plot(df5["Year"], df5["Count"], color="violet", label = "Name/ Year")
plt.legend()
plt.show()