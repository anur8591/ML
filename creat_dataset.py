import pandas as pd
import requests

# api_key = '84143a5419aad4efefa024f3c1a2c78a'
# df = pd.DataFrame()

# for i in range(1, 501):  # TMDB popular has a page limit around 500
#     url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&page={i}'
#     response = requests.get(url)
#     response.raise_for_status()
#     temp_df = pd.DataFrame(response.json()['results'])
#     df = pd.concat([df, temp_df], ignore_index=True)










# import pandas as pd 
# import requests

# response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a")

# temp_df = pd.DataFrame(response.json()['results'])


# df = pd.DataFrame()


# for i in range(1,10001):
#   response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a")
#   a_temp_df = pd.DataFrame(response.json()['results'])
#   df = pd.concat([df, a_temp_df], ignore_index=True)

# for i in range(10001,20001):
#   response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a")
#   b_temp_df = pd.DataFrame(response.json()['results'])
#   df = pd.concat([df, b_temp_df], ignore_index=True)

# for i in range(20001,30001):
#   response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a")
#   c_temp_df = pd.DataFrame(response.json()['results'])
#   df = pd.concat([df, c_temp_df], ignore_index=True)

# for i in range(30001,40001):
#   response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a")
#   d_temp_df = pd.DataFrame(response.json()['results'])
#   df = pd.concat([df, d_temp_df], ignore_index=True)

# for i in range(40001,50001):
#   response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a")
#   e_temp_df = pd.DataFrame(response.json()['results'])
#   df = pd.concat([df, e_temp_df], ignore_index=True)

# for i in range(50001,57623):
#   response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=84143a5419aad4efefa024f3c1a2c78a")
#   f_temp_df = pd.DataFrame(response.json()['results'])
#   df = pd.concat([df, f_temp_df], ignore_index=True)