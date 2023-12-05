#!/usr/bin/env python

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt
import seaborn as sns

taylor = pd.read_csv("taylor_all_songs.csv")
#print(taylor)

#1-how does tempo change over time with track number?

new_data = taylor[["track_number", "tempo"]]
median_tempo = taylor.groupby(['track_number'])['tempo'].median().reset_index()

tracks = median_tempo["track_number"]
tempo = median_tempo["tempo"]
#print(tracks, tempo)
#interesting to see how tempo fluctuates between ~120 bpm and ~150 bpm between songs, the lowest median was 96!

#picture this in a line plot where track number is roughly time through the album
fig, ax = plt.subplots()
ax.plot(tracks, tempo, color = 'cornflowerblue')
ax.scatter(tracks, tempo, color = 'plum')
ax.set_xlabel('Track Number')
ax.set_ylabel('Tempo (bpm)')
plt.show()
fig.savefig( "tracks_and_tempo.png" )
plt.close(fig)

#2 how does danceability compare between taylor's intitla albums and the re-releases
#find the mean and standard deviation of danceability for each

taylor_modified = taylor[["album_name", "danceability"]]
taylor_f = taylor_modified.iloc[16: 60, :]
taylor_r = taylor_modified.iloc[78:129, :]
frames = [taylor_f, taylor_r]
taylor_combo = (pd.concat(frames)).reset_index()

album_stats = taylor_combo.groupby('album_name')['danceability'].agg(['mean', 'std']).reset_index()
album_stats = album_stats.rename(columns={'mean': 'danceability_mean', 'std': 'danceability_std'})
#print(album_stats)
#it looks like based on the mean, fearless did not really change danceability but SD decreased while
#for red mean danceability decreased but standard deviation increased

#density plot of danceability of each track by album to better visualize shape of data and spread
color_list = ['orange', 'goldenrod', 'crimson', 'brown']

fig, ax = plt.subplots()
sns.kdeplot(data = taylor_combo, x = 'danceability', hue = 'album_name', palette = color_list, fill = True, alpha = 0.1), 
plt.xlabel('Danceability')
plt.ylabel('Density')
plt.tight_layout()
plt.show()
fig.savefig("dancebility_and_re-releases.png")
plt.close(fig)

#3 #3 how does the energy compare across all albums
#find mean and stanard devaition as well as median for all albums
albums = taylor.iloc[0:235,:].reset_index()
energy_stats = albums.groupby('album_name')['energy'].agg(['mean', 'std']).reset_index()
#print(energy_stats)
#1989 was the highest mean energy while folklore was the lowest, lover had the largest SD though 
#(arguably most variable in energy levles)


#box and whisker for energy vs albums -- highlighting 1989 and folklore
fig, ax = plt.subplots()
colors = ['grey', 'grey', 'grey', 'grey', 'grey', 'grey', 'mediumturquoise', 'grey', 'grey', 'sandybrown', 'grey', 'grey']
# energyplt.boxplot(column = "energy", by = 'album_name', figsize = (15,15), notch = True)
sns.boxplot(y = albums['energy'], x = albums['album_name'], palette = colors)
plt.xticks(rotation ='vertical')
plt.xlabel("Album")
plt.ylabel("Energy")
plt.tight_layout()
plt.show()
plt.savefig("energy.png")
plt.close(fig)


