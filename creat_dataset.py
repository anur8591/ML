# importing required libraries
import pandas as pd
import requests

# sending request to the website to collect the data 
url = "https://api.themoviedb.org/3/movie/popular?api_key="
response = requests.get(url)

# creating enpty Data_Frame to store fetched data
df = pd.DataFrame() 

# the Data is too much ~1.15 million so we cannot fetch that much data from API😭😭 and
# it taking a lot of computation power and storage cuz there is a high chance that the list
# reached it's limit.

# So we are using for loop to fetch the data in the chunks, so we collected ~~1.15lakh data
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

# Now saving the into the local folder in csv format 
df.to_csv("TMDB_movies.csv")