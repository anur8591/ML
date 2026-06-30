# importing required libraries
import pandas as pd
import requests

url = "https://api.themoviedb.org/3/movie/popular?api_key="
response = requests.get(url)

df = pd.DataFrame() 

for i in range(1,1001):
  response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=")
  a_temp_df = pd.DataFrame(response.json()['results'])
  df = pd.concat([df, a_temp_df], ignore_index=True)

for i in range(1001,2001):
  response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=")
  b_temp_df = pd.DataFrame(response.json()['results'])
  df = pd.concat([df, b_temp_df], ignore_index=True)
  
for i in range(2001,3001):
  response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=")
  c_temp_df = pd.DataFrame(response.json()['results'])
  df = pd.concat([df, c_temp_df], ignore_index=True)

for i in range(3001,4001):
  response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=")
  d_temp_df = pd.DataFrame(response.json()['results'])
  df = pd.concat([df, d_temp_df], ignore_index=True)

for i in range(4001,5001):
  response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=")
  e_temp_df = pd.DataFrame(response.json()['results'])
  df = pd.concat([df, e_temp_df], ignore_index=True)

for i in range(5001,5762):
  response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=")
  f_temp_df = pd.DataFrame(response.json()['results'])
  df = pd.concat([df, f_temp_df], ignore_index=True)

df.to_csv("TMDB_movies.csv")