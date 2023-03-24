import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
   url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
   data = requests.get(url)
   data = data.json()
   poster_path = data['poster_path']
   full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
   return full_path

def recommend(movie):
  index = movies[movies.title == movie].index[0]
  distance = sorted(list(enumerate(similarity[index])), reverse = True, key = lambda x:x[1])
  recommended_movies_name = []
  recommended_movies_poster = []
  for i in distance[1:6]:
     movies_id = movies.iloc[i[0]]['movie_id']
     recommended_movies_poster.append(fetch_poster(movies_id))
     recommended_movies_name.append(movies.iloc[i[0]]['title'])
  
  return recommended_movies_name, recommended_movies_poster



st.header("Movies Recommendation System Using ML")
movies = pickle.load(open("artifacts/movies_list.pkl", 'rb'))
similarity = pickle.load(open("artifacts/similarity.pkl", 'rb'))

movies_list = movies['title'].values
selected_movies = st.selectbox(
    "Type or Select a movei to get recommendation",
    movies_list
)


if st.button("Show Recommendation"):
    recommended_movie_names , recommended_movie_posters  = recommend(selected_movies)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

