import pandas as pd

df = pd.read_csv(r'C:\Users\JodaBook\Documents\Python\Python\astronauts.csv')

#print(df.head())
#print(len(df))
# for name in df["Name"]:
#     print(name)
#     break

person = df.iloc[0]
#print(person)
personData = df.iloc[1]
#print(personData)
#print(person["Space Walks"])

search = df.iloc[4:8] #Berreich
search = df.iloc[-5:] #die letzen 5 Zeilen
#print(search)

# for row in df.iterrows(): 
#     print(row)
#     print(type(row))

# for pos, d in df.iterrows(): 
#     print(pos)
#     print(d)
#     print(d["Status"])
#     break


df2 = df.sort_values("Name", ascending=False)

for pos, d in df2.iterrows():
    if d["Status"] == "Active" and d["Year"] > 1990:
        print(d["Name"])