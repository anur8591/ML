import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("TMDB_movies.csv") #origenal dataset


dff = df.drop(columns=["Unnamed: 0", "adult", 
                       "original_title", "softcore", 
                       "video", "backdrop_path", 
                       "poster_path"]) #dff dataset is for model training 
# a = df.value_counts(["adult", "original_language", "softcore", "video"])
# print(a)
dff.info()
print(dff.head())
