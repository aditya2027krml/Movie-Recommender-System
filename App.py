#DEPLOYING OUR MODEL AS WEB APP

import pickle as pk
import streamlit as st

st.text("AUTHOR : <ADITYA KUMAR>")
st.text("TASK 2")
st.text("MOVIE RECOMMENDER")



st.header("Movie Recommender")

movie_dataset = pk.load(open('D:\Bharat Intern\Movie_Recommender\movie_dataset.pk1', 'rb'))
similarity = pk.load(open('D:\Bharat Intern\Movie_Recommender\similarity.pk1', 'rb'))

def recommend_movie(movie_name):
    # Check if the movie exists in the DataFrame
    if movie_name not in movie_dataset['title'].values:
        print(f"The movie '{movie_name}' does not exist in the dataset.")
        return
    
    # Get the index of the movie
    movie_index = movie_dataset[movie_dataset['title'] == movie_name].index[0]
    
    # Assuming 'similarity' and 'data' are defined elsewhere in your code
    similar_movies = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda vector: vector[1])
    recommendations = []
    # Print recommendations
    print(f"Recommendations for '{movie_name}':")
    for i in similar_movies[1:11]:
        recommendations.append(movie_dataset.iloc[i[0]].title + ' with similarity of ' + str(i[1] * 100)[:5])  # Fixed the parenthesis here

        # Assuming 'i[1]' is the similarity score
    return recommendations
# Call the function with the movie name
#recommend_movie('Ganglands')




selected_movie = st.selectbox('Select movie/Tv Show', movie_dataset['title'])

if st.button('Recommend'):
    result = recommend_movie(selected_movie)
    st.text(result[0])
    st.text(result[1])
    st.text(result[2])
    st.text(result[3])
    st.text(result[4])
    st.text(result[5])
    st.text(result[6])
    st.text(result[7])
    st.text(result[8])
    st.text(result[9])
    
    
st.success("SUCCESFULLY DONE!")