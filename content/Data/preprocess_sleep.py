import pandas as pd
import random

sleep = pd.read_csv("/Users/cyrilwendl/Documents/Documents/KLW/Unterricht/00 Varia/Unterrichtsmaterial Naoki OFI/4 - Jahr 4, Semester 2/02 Data Science/1 Daten analysieren und visualisieren/jupyter/Data/sleep_orig.csv")

sleep["Daily Steps"] = sleep['Daily Steps'].apply(lambda x: x + random.randint(-500, 500))
for col in ["Sleep Duration", "Stress Level"]:
    sleep[col] = sleep[col].apply(lambda x: x + random.uniform(-0.5, 0.5))

sleep = sleep[sleep["Daily Steps"] < 8000]
print(sleep.head())

sleep.to_csv("/Users/cyrilwendl/Documents/Documents/KLW/Unterricht/00 Varia/Unterrichtsmaterial Naoki OFI/4 - Jahr 4, Semester 2/02 Data Science/1 Daten analysieren und visualisieren/jupyter/Data/sleep processed.csv", index=False)


