import pandas as pd

headers = ['color_code', 'color_name', 'hexcode', 'r', 'g', 'b']

dataframe = pd.read_csv("colors.csv", names = headers, header = None)

print(dataframe.loc[12, 'color_name'])

r = 160
g = 200
b = 199

def get_color_name():
    minimum = 768
    for i in range(len(dataframe)):
        distance = abs((r-dataframe.loc[i, 'r']) + (g-dataframe.loc[i, 'g']) + (b-dataframe.loc[i, 'b']))
        if distance < minimum:
            minimum = distance
            color_name = dataframe.loc[i, 'color_name']
    print(color_name)

get_color_name()