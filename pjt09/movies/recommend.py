import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df_a = pd.read_json('movies/fixtures/genre_data.json')
# df_a = pd.read_json('movies/fixtures/genre_data2.json')
# df_b = pd.read_json('movies/fixtures/movie_data2.json')
df_b = pd.read_json('movies/fixtures/movie_data.json')
# print(df_a)
# print(df_b)

df_final = pd.DataFrame()
newdata = {}
newdata = {'id': [], 'title': [],'genres': [], 'vote_average': []}
    
for i in range(len(df_b)):
    # newdata['id'].append(df_b.iloc[i]['fields']['movie_id'])
    newdata['id'].append(df_b.iloc[i]['pk'])
    # newdata['id'].append(i)
    newdata['title'].append(df_b.iloc[i]['fields']['title'])
    genre_list = []
    for j in df_b.iloc[i]['fields']['genres']:
        for k in range(len(df_a)):
            # if df_a.iloc[k]['pk'] == j:
            if df_a.iloc[k]['pk'] == j:
                genre_list.append(df_a.iloc[k]['fields']['genre_name'])
    newdata['genres'].append(" ".join(genre_list))
    newdata['vote_average'].append(df_b.iloc[i]['fields']['vote_average'])
df_new = pd.DataFrame(newdata)

count_vect = CountVectorizer(min_df=0, ngram_range=(1,3))
genre_mat = count_vect.fit_transform(df_new['genres'])
genre_sim = cosine_similarity(genre_mat, genre_mat)
# genre_sim_sorted_ind = genre_sim.argsort()[:, ::-1]
genre_sim_sorted_ind = genre_sim.argsort()


def recommendation(df, movie_title, top=11):
    # 특정 영화정보 뽑아내기 
    tmi = df[df['title'] == movie_title].index.values
    # 타겟 영화와 비슷한 코사인 유사도값
    sim_index = genre_sim_sorted_ind[tmi, :top].reshape(-1)
    # 본인 제외
    sim_index = sim_index[sim_index != tmi]
    # data frame으로 만들고 vote_count 값으로 정렬한 뒤 return
    result = df.iloc[sim_index].sort_values('vote_average', ascending=False)[:11]
    return result

# a = recommendation(df_new, '007 노 타임 투 다이')
# print(a)

# for i in a.id:
#     print(i)

def recommended_movie_info(recommended):
    movie_info_list = []
    for i in recommended.id:
        # for j in range(357):
        for j in range(601):
            # if df_b.iloc[j]['fields']['movie_id'] == i:
            if df_b.iloc[j]['pk'] == i:
                movie_info_list.append({"movie_id": i, "title": df_b.iloc[j]['fields']['title'], "poster_path": 'https://image.tmdb.org/t/p/w500' + df_b.iloc[j]['fields']['poster_path'], "original_title": df_b.iloc[j]['fields']['original_title'], "release_date": df_b.iloc[j]['fields']['release_date'], "vote_average": df_b.iloc[j]['fields']['vote_average']})
    return movie_info_list        

# b = recommended_movie_info(a)
# print(b)