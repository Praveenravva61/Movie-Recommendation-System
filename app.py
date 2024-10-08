import streamlit as st
import pickle
import requests

API_KEY = 'a5e481384a7d0d4c05959d74bb981b50'

def fetch_movie_details_by_id(movie_id):
    """Fetch movie details (rating, cast, director) using the movie ID."""
    movie_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US"

    movie_response = requests.get(movie_url).json()
    credits_response = requests.get(credits_url).json()

    # Extract movie rating
    rating = movie_response.get('vote_average')

    # Extract cast (first 10 members)
    cast = [member['name'] for member in credits_response['cast'][:10]]

    # Extract director (from crew)
    director = next((crew['name'] for crew in credits_response['crew'] if crew['job'] == 'Director'), 'Unknown')

    return rating, cast, director


def fetch_poster_and_id_by_name(movie_name):
    """Fetch the movie poster and ID using the movie name."""
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(search_url)
    data = response.json()

    if data['results']:
        movie = data['results'][0]
        poster_path = movie.get('poster_path')
        movie_id = movie.get('id')  # Get the movie ID

        if poster_path:
            full_poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}"
            return full_poster_url, movie_id
        else:
            return None, movie_id  # No poster available
    return None, None  # No movie found


def recommended_movies(movie):
    """Fetch recommended movies, their posters, IDs, and ratings."""
    movie_index = list(movies_dict).index(movie)
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])

    Movies = []
    recommended_movie_posters = []
    recommended_movie_ids = []
    recommended_movie_ratings = []

    for i in movies_list[1:6]:  # Skip the first item since it's the movie itself
        movie_name = movies_dict[i[0]]
        Movies.append(movie_name)
        poster, movie_id = fetch_poster_and_id_by_name(movie_name)
        if movie_id:
            rating, _, _ = fetch_movie_details_by_id(movie_id)  # Fetch rating
            recommended_movie_ratings.append(rating)  # Add rating to the list
        recommended_movie_posters.append(poster)
        recommended_movie_ids.append(movie_id)
    return Movies, recommended_movie_posters, recommended_movie_ids, recommended_movie_ratings


# Load the movies dictionary and similarity matrix using pickle
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Display the header and the selectbox
st.header('Movie Recommendation System')

# Create a selectbox for movie selection
selected_movie_name = st.selectbox(label='Select a Movie', options=movies_dict)

if st.button('Recommend'):
    movies_titles, recommended_movie_posters, recommended_movie_ids, recommended_movie_ratings = recommended_movies(selected_movie_name)

    # Create columns for displaying recommended movies
    cols = st.columns(5)  # Create 5 columns
    for col, title, poster, movie_id, rating in zip(cols, movies_titles, recommended_movie_posters, recommended_movie_ids, recommended_movie_ratings):
        with col:
            st.text(title)  # Display movie title
            st.text(f"Rating: {rating}")  # Display movie rating
            if poster:  # Check if a poster is available
                st.image(poster, use_column_width=True)  # Display the poster

                # Expander to show more details on click (optional)
                with st.expander(f"More details about {title}"):
                    _, cast, director = fetch_movie_details_by_id(movie_id)
                    st.write(f"**Director**: {director}")
                    st.write("**Cast**:")
                    for actor in cast:
                        st.write(f"- {actor}")
                    full_poster_url = f"https://image.tmdb.org/t/p/original/{poster.split('/')[-1]}"
                    st.image(full_poster_url, caption=f"Poster of {title}", use_column_width=True)
            else:
                st.text("No poster available")  # Fallback if no poster is available
