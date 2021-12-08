import requests
import json
import pprint

apiV3 = '238cdc4f15a5ca36e49a32dee96747c8'

url = 'https://api.themoviedb.org/3'

type = '/genre/movie/list'

URL = url + type
params = {'api_key': apiV3, 'language':"ko-KR"}
res = requests.get(URL, params=params)
# print(res.json())
genre_list = res.json()['genres']
# print(genre_list)
final_list = []

for genre in genre_list:
      single_genre = {"model":"movies.genre"}
      single_genre["pk"] = genre['id']
      single_genre["fields"] = {'genre_name' : genre['name']}
      final_list.append(single_genre)

print(final_list)
with open('genre_data2.json', 'w', encoding='UTF-8') as f:
  json.dump(final_list, f,ensure_ascii=False, indent=2)