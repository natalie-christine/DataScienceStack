import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Daten laden
df = pd.read_csv(r'C:\Users\JodaBook\Documents\Python\Python\names.csv')

# Name, Geschlecht und Staat filtern
name = "Natalie"
gender = "F"
state = "CA"

df_filtered = df[(df["Name"] == name) & (df["Gender"] == gender) & (df["State"] == state)]

# Daten nach Jahr sortieren
df_sorted = df_filtered.sort_values("Year")

# Jahr und Anzahl als unabhängige und abhängige Variablen setzen
X = df_sorted[["Year"]].values.reshape(-1, 1)  # X muss eine 2D-Array sein
y = df_sorted["Count"].values  # y kann eine 1D-Array sein

# Lineares Regressionsmodell erstellen und anpassen
model = LinearRegression()
model.fit(X, y)

# Vorhersagen treffen
predicted = model.predict(X)

# Ergebnisse plotten
plt.plot(X, y, color="blue", label="Actual Count")
plt.plot(X, predicted, color="red", label="Predicted Count")
plt.xlabel("Year")
plt.ylabel("Count")
plt.title(f"Popularity of the Name '{name}' in {state}")
plt.legend()
plt.show()
