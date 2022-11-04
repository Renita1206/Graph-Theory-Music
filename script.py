import pandas as pd

data = pd.read_csv("./music.csv")
name = pd.read_csv("./name.csv")

df = pd.DataFrame(columns = ['id', 'label', 'name', '_start', '_end', '_type', '_rating'])
unique_genre = data["genre"].unique()


for i in range(1,8):
	df.loc[i] = [i - 1, ":genre", unique_genre[i - 1], '', '', '', '']

for i in range(8, 1002):
	df.loc[i] = [i - 1, ":track", data["track_name"][i - 8], '', '', '', '']

for i in range(1002, 1302):
	df.loc[i] = [i - 1, ":user", name["name"][i - 1000], '', '', '', '']



print(df)

