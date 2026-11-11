
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("greenhouse.csv")

print(df.head())
print(df.shape)
df.info()



print(df.isnull().sum())

print("Rows after dropna:", len(df.dropna()))


df["Plant_Type"] = df["Plant_Type"].fillna("Unknown")

df["Soil_Moisture"] = df["Soil_Moisture"].fillna(
    round(df["Soil_Moisture"].mean())
)

df["Temperature_C"] = df["Temperature_C"].fillna(
    round(df["Temperature_C"].mean(), 1)
)

print("Total Missing Values:", df.isnull().sum().sum())




print(df.loc[0])

print(df.iloc[0:3])

print(df.loc[df["Soil_Moisture"] < 40,
             ["Plant_ID", "Soil_Moisture"]])

print("Tomato Plants:",
      len(df[df["Plant_Type"] == "Tomato"]))




def check_status(moisture):

    if moisture < 40:
        return "Needs Water"
    else:
        return "OK"


df["Status"] = df["Soil_Moisture"].apply(check_status)

print(df.sort_values("Height_cm", ascending=False).head(3))

print(df["Status"].value_counts())

print(df.groupby("Plant_Type")["Soil_Moisture"].mean())

df.to_csv("greenhouse_clean.csv", index=False)


df = pd.read_csv("greenhouse_clean.csv")

df = df.sort_values(["Row", "Pot_No"])

grid = np.array(df["Soil_Moisture"]).reshape(3, 5)

print("Grid:")
print(grid)

print("Grid Shape:")
print(grid.shape)

print("Average Moisture of Each Row:")
print(np.mean(grid, axis=1))

print("Driest Row:")
print(np.argmin(np.mean(grid, axis=1)) + 1)

print("Pots Needing Water:")
print(np.sum(grid < 40))

after = grid + 15

after[after > 100] = 100

print("After Rain:")
print(after)


df.groupby("Plant_Type")["Soil_Moisture"].mean().plot(kind="bar")

plt.title("Average Soil Moisture by Plant Type")
plt.xlabel("Plant Type")
plt.ylabel("Average Soil Moisture")
plt.show()




plt.scatter(df["Sunlight_Hours"], df["Soil_Moisture"])

plt.title("Sunlight vs Soil Moisture")
plt.xlabel("Sunlight Hours")
plt.ylabel("Soil Moisture")
plt.show()



sns.countplot(data=df, x="Plant_Type", hue="Status")

plt.title("Plants by Type and Status")
plt.xlabel("Plant Type")
plt.ylabel("Number of Plants")
plt.show()


sns.heatmap(grid, annot=True, cmap="Blues")

plt.title("Greenhouse Moisture Heatmap")
plt.xlabel("Pot Number")
plt.ylabel("Row Number")
plt.show()
