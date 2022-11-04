import pandas as pd
import random

music = pd.read_csv("music.csv")
music = music.sample(frac = 1)
#music.head()

name = pd.read_csv("names.csv")

unique_genres = music["genre"].unique().tolist()
#print(unique_genres)
tracks = music["track_name"].unique().tolist()[0:994]
users = name["name"].tolist()[0:299]

df = pd.DataFrame(columns = ['id', 'label', 'name', '_start', '_end', '_type', 'rating'])

for i in range(0,7):
    df.loc[i] = [i, ":genre", unique_genres[i], '', '', '', '']


for i in range(7, 1001):
	df.loc[i] = [i, ":track", tracks[i-7], '', '', '', '']

for i in range(1001, 1301):
    df.loc[i] = [i, ":user", name["name"][i - 1001], '', '', '', '']

row_no = 1301


for i in tracks:
    df.loc[row_no] = [ '', '', '', df.loc[df['name'] == i]['id'].iat[0], unique_genres.index(music.loc[music['track_name'] == i]['genre'].iat[0]), 'BELONGS_TO', '']
    row_no+=1

for i in range(0, len(tracks)):
	k = random.randrange(300)
	df.loc[row_no] = [ '', '', '', k + 1001, i + 7, 'LISTENS_TO', '']
	row_no += 1

df.to_csv('graph_dataset.csv')
