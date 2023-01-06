import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)


# Below is the Output :

      calories  duration
day1       420        50
day2       380        40
day3       390        45
