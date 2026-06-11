import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

df["Pclass"].value_counts().plot(kind="bar")

plt.title("Passenger Class Distribution")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")

plt.show()