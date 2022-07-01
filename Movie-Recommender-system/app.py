import streamlit as st
import pickle
import pandas as pd
import requests
def get_poster(movie_id):
     url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=97c0abc1353598fddfb2e5268a6a5598"
     response=requests.get(url)
     data=response.json()
     poster_path=data["poster_path"]
     full_path="https://image.tmdb.org/t/p/w500"+poster_path
def recommend(movie):
     movie_index = movies[movies["title"] == movie].index[0]
     distances= sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
     recommended_movies=[]
     recommended_movies_posters=[]
     for movie in distances:
          id=movies.iloc[movie[0]].id
          poster=get_poster(id)
          recommended_movies_posters.append(poster)
          recommended_movies.append(movies.iloc[movie[0]].title)
          return recommended_movies,recommended_movies_posters

     return recommended_movies,recommended_movies_posters
movies_dict=pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
selected_movie_name= st.selectbox(
     'Select movie from dropdown menu',
     movies["title"].values)
if st.button('Recommend'):
     recommend_movies,recommend_movies_posters=recommend(selected_movie_name)
     col1, col2, col3,col4, col5= st.columns(5)

     with col1:
          st.header(recommend_movies[0])
          st.image(recommend_movies_posters[0])

     with col1:
          st.header(recommend_movies[1])
          st.image(recommend_movies_posters[1])

     with col1:
          st.header(recommend_movies[2])
          st.image(recommend_movies_posters[2])
     with col4:
          st.header(recommend_movies[3])
          st.image(recommend_movies_posters[3])
     with col5:
          st.header(recommend_movies[4])
          st.image(recommend_movies_posters[4])