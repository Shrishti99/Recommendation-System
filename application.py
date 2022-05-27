import streamlit as st # import the packages
import pickle
import pandas as pd
# display the image using st.image() function in streamlit
st.image("https://media.istockphoto.com/photos/popcorn-and-clapperboard-picture-id1191001701?k=20&m=1191001701&s=612x612&w=0&h=uDszifNzvgeY5QrPwWvocFOUCw8ugViuw-U8LCJ1wu8=")
# set the title
st.title('Movie Recommendation System')
# load the .pkl file into the movies
movies = pickle.load(open('movie_dict.pkl', 'rb'))
# create a dataframe of the file and store in movieL
movieL = pd.DataFrame(movies)
#load the similarity.pkl file into the movies
similarity = pickle.load(open('similarity.pkl', 'rb'))
#create a recommend function for movie recommendation
def recommended_movies(movie):
    movie_index = movieL[movieL['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    rec_movies = []
    for i in movies_list:
        rec_movies.append(movieL.iloc[i[0]].title)
    return rec_movies

# set a selectbox to type the movie name or select from the drop down menu
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown", movieL['title'].values)
if st.button('Recommend'): #set a button
    recommendations = recommended_movies(selected_movie)
    st.write("The recommended movies for you are as:")
    for i in recommendations:
        st.write(i) #write the recommened movies to the screen


