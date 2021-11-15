import pickle
import pandas as pd


knn = pickle.load(open("pickles/knn.p", "rb"))
movies = pickle.load(open("pickles/movies.p", "rb"))
final_dataset = pickle.load(open("pickles/final_dataset.p", "rb"))
csr_data = pickle.load(open("pickles/csr_data.p", "rb"))


def get_movie_recommendation(movie_name):
    n_movies_to_reccomend = 10
    movie_list = movies[movies["title"].str.contains(movie_name)]

    if len(movie_list):
        movie_idx = movie_list.iloc[0]["movieId"]
        movie_idx = final_dataset[final_dataset["movieId"] == movie_idx].index[0]
        distance, indices = knn.kneighbors(
            csr_data[movie_idx], n_neighbors=n_movies_to_reccomend + 1
        )
        rec_movie_indices = sorted(
            list(zip(indices.squeeze().tolist(), distance.squeeze().tolist())),
            key=lambda x: x[1],
        )[:0:-1]
        recommend_frame = []
        for val in rec_movie_indices:
            movie_idx = final_dataset.iloc[val[0]]["movieId"]
            idx = movies[movies["movieId"] == movie_idx].index
            recommend_frame.append(
                {"Title": movies.iloc[idx]["title"].values[0], "distance": val[1]}
            )
        df = pd.DataFrame(recommend_frame, index=range(1, n_movies_to_reccomend + 1))
        return df
    else:
        return "NO movies found in our server!!!"


print(get_movie_recommendation("Iron Man"))
