# importing required libraries
import pandas as pd
import requests

url = "https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a"
response = requests.get(url)

df = pd.DataFrame() 

for i in range(1,1001):
  response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a")
  a_temp_df = pd.DataFrame(response.json()['results'])
  df = pd.concat([df, a_temp_df], ignore_index=True)

for i in range(1001,2001):
  response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a")
  b_temp_df = pd.DataFrame(response.json()['results'])
  df = pd.concat([df, b_temp_df], ignore_index=True)
  
for i in range(2001,3001):
  response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a")
  c_temp_df = pd.DataFrame(response.json()['results'])
  df = pd.concat([df, c_temp_df], ignore_index=True)

for i in range(3001,4001):
  response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a")
  d_temp_df = pd.DataFrame(response.json()['results'])
  df = pd.concat([df, d_temp_df], ignore_index=True)

for i in range(4001,5001):
  response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a")
  e_temp_df = pd.DataFrame(response.json()['results'])
  df = pd.concat([df, e_temp_df], ignore_index=True)

for i in range(5001,5762):
  response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a")
  f_temp_df = pd.DataFrame(response.json()['results'])
  df = pd.concat([df, f_temp_df], ignore_index=True)

df.to_csv("TMDB_movies.csv")