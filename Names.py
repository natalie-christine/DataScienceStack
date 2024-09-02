import os
from collections import defaultdict

folder = r'C:\Users\JodaBook\Documents\Python\Kursmaterialien\13, 14, 15 - Diverses\PythonProjekt\names'

#os.path.join(os.path.dirname(__file__), "names")
files = os.listdir(folder)
#print(files)

p = defaultdict(int)

for filename in files:
    file_path = os.path.join(folder, filename)
    with open(file_path,"r", encoding= "utf-8", ) as file:
        #print(filename) 
        for line in file:
            #print(line.split(" "))
            forname = line.split(" ")[0] #forname, surname = line.strip().split(" ") 
            p[forname] += 1
            
print(f"Natalie: {p['Natalie']}")
        

