import requests
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

apiV3 = '238cdc4f15a5ca36e49a32dee96747c8'

url = 'https://api.themoviedb.org/3'

type = '/movie/popular'

total_movie_list = []
final_list = []
actor_final_list = []
director_final_list = []

for page_number in range(1,101):
# for page_number in range(1,50):

    params = {'api_key': apiV3, 'language':"ko-KR", 'page':page_number}
    URL = url + type
    res = requests.get(URL, params=params)
    movie_list = res.json()['results']
    total_movie_list += movie_list

# print(len(total_movie_list))



for idx, movie in enumerate(total_movie_list):
    # single_movie_data = {"model": "movies.movie", "pk": idx+1}
    single_movie_data = {"model": "movies.movie", "pk": movie["id"]}
    # print(single_movie_data)
    try:
        if not movie['release_date']:
            continue
        elif not movie['overview']:
            continue
        elif not movie['genre_ids']:
            continue
        else:
            n_movie = {
                # "movie_id": movie["id"],
                "title": movie["title"],
                "popularity": movie["popularity"],
                "poster_path": movie["poster_path"],
                "release_date": movie["release_date"],
                "vote_average": movie["vote_average"],
                "vote_count": movie["vote_count"],
                "overview": movie["overview"],
                "genres": movie["genre_ids"],
                "original_title": movie["original_title"],
            }
            params = {'api_key': apiV3, 'language':"ko-KR"}
            # URL = url + f'/movie/{n_movie["movie_id"]}/videos'
            URL = url + f'/movie/{movie["id"]}/videos'
            res = requests.get(URL, params=params)
            trailer = res.json()['results']
            for t in trailer:
                if t["type"] == "Trailer":
                    n_movie["trailer"] = t["key"]


            # URL = url + f'/movie/{n_movie["movie_id"]}/credits'
            URL = url + f'/movie/{movie["id"]}/credits'
            res = requests.get(URL, params=params)
            actors = res.json()['cast']
            # print(actors)
            a_list = []
            for a in actors[:5]:
                # actor_movie_data = {"model": "movies.actor"}
                actor_movie_data = {"model": "movies.actor", "pk": a['id']}
                if a['known_for_department'] == 'Acting':
                    a_dic = {}
                    # a_dic['actor_id'] = a['id']
                    a_dic['actor_name'] = a['name']
                    a_dic['profile_path'] = a['profile_path']
                    a_list.append(a['id'])
                actor_movie_data["fields"] = a_dic
                actor_final_list.append(actor_movie_data)
            n_movie['actors_info'] = a_list
            with open('actor_data.json', 'w', encoding='UTF-8') as f:
                json.dump(actor_final_list, f,ensure_ascii=False, indent=2)
            # print(len(actor_final_list))

            directors = res.json()['crew']
            director_info = []
            for d in directors:
                director_movie_data = {"model": "movies.director", "pk": d['id']}
                # print(director_movie_data)
                if d['known_for_department'] == 'Directing':
                    d_dic = {}
                    # d_dic['director_id'] = d['id']
                    d_dic['director_name'] = d['name']
                    d_dic['profile_path'] = d['profile_path']
                    director_info.append(d['id'])
                    director_movie_data["fields"] = d_dic
                    director_final_list.append(director_movie_data)
                    break
            if len(director_info) == 0:
                pass
            else:
                n_movie['director_info'] = director_info
            

            with open('director_data.json', 'w', encoding='UTF-8') as f:
                json.dump(director_final_list, f,ensure_ascii=False, indent=2)
            
            # if len(n_movie) >= 13:
            if len(n_movie) >= 12:
                single_movie_data["fields"] = n_movie
                final_list.append(single_movie_data)
    except KeyError:
        continue

# # print(final_list)
# print(len(actor_final_list))    #4095
# print(len(director_final_list)) #748


with open('movie_data.json', 'w', encoding='UTF-8') as f:
    json.dump(final_list, f,ensure_ascii=False, indent=2)
