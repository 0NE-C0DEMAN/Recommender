import streamlit as st
import requests


import pandas as pd
import pyarrow.parquet as pq

# streamlit run C:/Users/Siddhant/PycharmProjects/Projects/Recommender/app.py --server.address=127.0.0.1


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def fetch_cover(title_author):
    cover = booksinfo.loc[booksinfo["title_author"] == title_author, "coverImg"].iloc[0]
    return cover


def fetch_album(song_name_artist):
    cover = songsinfo.loc[
        songsinfo["song_name_artist_name"] == song_name_artist, "images"
    ].iloc[0]
    return cover


def recommendmovie(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = sorted(
        list(enumerate(moviesimilarity[index])), reverse=True, key=lambda x: x[1]
    )
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:9]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


def recommendbook(book):
    index = books[books["title_author"] == book].index[0]
    distances = sorted(
        list(enumerate(booksimilarity[index])), reverse=True, key=lambda x: x[1]
    )
    recommended_book_names = []
    recommended_book_posters = []
    for i in distances[1:9]:
        # fetch the book poster
        title_author = booksinfo.iloc[i[0]]["title_author"]
        recommended_book_posters.append(fetch_cover(title_author))
        recommended_book_names.append(booksinfo.iloc[i[0]]["title_author"])

    return recommended_book_names, recommended_book_posters


def recommendsong(song):
    index = songs[songs["song_name_artist_name"] == song].index[0]
    distances = sorted(
        list(enumerate(songsimilarity[index])), reverse=True, key=lambda x: x[1]
    )
    recommended_song_names = []
    recommended_song_posters = []
    for i in distances[1:9]:
        # fetch the song poster
        song_name_artist = songsinfo.iloc[i[0]]["song_name_artist_name"]
        recommended_song_posters.append(fetch_album(song_name_artist))
        recommended_song_names.append(songsinfo.iloc[i[0]]["song_name_artist_name"])

    return recommended_song_names, recommended_song_posters


# path = 'C:/Users/Siddhant/PycharmProjects/Projects/Recommender/'

movieinfo = pd.read_parquet("movieparquet/movie_info.parquet")
movies = pd.read_parquet("movieparquet/movie_list.parquet")

moviesimilarity_from_parquet = pq.read_table("movieparquet/movie_similarity.parquet")
moviesimilarity = moviesimilarity_from_parquet.to_pandas().T.to_numpy()


books = pd.read_parquet("bookparquet/book_list.parquet")
booksinfo = pd.read_parquet("bookparquet/booksinfo.parquet")

booksimilarity_from_parquet = pq.read_table("bookparquet/book_similarity.parquet")
booksimilarity = booksimilarity_from_parquet.to_pandas().T.to_numpy()


songs = pd.read_parquet("songparquet/song_list.parquet")
songsinfo = pd.read_parquet("songparquet/songinfo.parquet")

songsimilarity_from_parquet = pq.read_table("songparquet/song_similarity.parquet")
songsimilarity = songsimilarity_from_parquet.to_pandas().T.to_numpy()


def movie_details(movie):
    overview = movieinfo.loc[movieinfo["title"] == movie, "overview"].iloc[0]
    genres = movieinfo.loc[movieinfo["title"] == movie, "genres"].iloc[0]
    cast = movieinfo.loc[movieinfo["title"] == movie, "cast"].iloc[0]
    crew = movieinfo.loc[movieinfo["title"] == movie, "crew"].iloc[0]
    vote_average = movieinfo.loc[movies["title"] == movie, "vote_average"].iloc[0]
    genres = ", ".join(genres)
    cast = ", ".join(cast)
    crew = ", ".join(crew)
    return overview, genres, cast, crew, vote_average


def book_details(book):
    title = booksinfo.loc[booksinfo["title_author"] == book, "title"].iloc[0]
    author = booksinfo.loc[booksinfo["title_author"] == book, "author"].iloc[0]
    publisher = booksinfo.loc[booksinfo["title_author"] == book, "publisher"].iloc[0]
    genres = booksinfo.loc[booksinfo["title_author"] == book, "genres"].iloc[0]
    language = booksinfo.loc[booksinfo["title_author"] == book, "language"].iloc[0]
    description = booksinfo.loc[booksinfo["title_author"] == book, "description"].iloc[
        0
    ]
    rating = booksinfo.loc[booksinfo["title_author"] == book, "rating"].iloc[0]
    genres = ", ".join(genres)
    return title, author, publisher, genres, language, description, rating


def song_details(song):
    song_name = songsinfo.loc[
        songsinfo["song_name_artist_name"] == song, "song_name"
    ].iloc[0]
    artist_name = songsinfo.loc[
        songsinfo["song_name_artist_name"] == song, "artist_name"
    ].iloc[0]
    playlist = songsinfo.loc[
        songsinfo["song_name_artist_name"] == song, "playlist"
    ].iloc[0]
    genres = songsinfo.loc[songsinfo["song_name_artist_name"] == song, "genres"].iloc[0]
    lyrics = songsinfo.loc[songsinfo["song_name_artist_name"] == song, "lyrics"].iloc[0]
    popularity = songsinfo.loc[
        songsinfo["song_name_artist_name"] == song, "popularity"
    ].iloc[0]

    genres = ", ".join(genres)
    return song_name, artist_name, playlist, genres, lyrics, popularity


movie_list = movies["title"].values
book_list = books["title_author"].values
song_list = songs["song_name_artist_name"].values

st.set_page_config(layout="wide")
st.header("Recommender System")
menu = ["Movie", "Books", "Songs", "About"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Movie":
    st.subheader("Movie")
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown", movie_list
    )
    if st.button("Show Recommendation"):
        recommended_movie_names, recommended_movie_posters = recommendmovie(
            selected_movie
        )
        col1, col2, col3, col4 = st.columns(4)
        counter = 0
        for col in st.columns(4):
            with col:
                st.text(recommended_movie_names[counter])
                st.image(recommended_movie_posters[counter])
                with st.expander("Details"):
                    overview, genres, cast, crew, vote_average = movie_details(
                        recommended_movie_names[counter]
                    )
                    html_str = f"""
                    <h4 style="text-align:center;text-decoration: underline;">{recommended_movie_names[counter]}</h4>
                    <h5>Overview:</h5> <p>{overview}</p> 
                    <h5>Genres:</h5> <p>{genres}</p>
                    <h5>Cast:</h5> <p>{cast}</p> 
                    <h5>Director:</h5> <p>{crew}</p> 
                    <h5>Rating:</h5> <p style="font-size:26px;color:rgb(4, 217, 255)">{vote_average}</p> 
                    """
                    st.markdown(html_str, unsafe_allow_html=True)
            counter += 1
        counter = 4
        for col in st.columns(4):
            with col:
                st.text(recommended_movie_names[counter])
                st.image(recommended_movie_posters[counter])
                with st.expander("Details"):
                    overview, genres, cast, crew, vote_average = movie_details(
                        recommended_movie_names[counter]
                    )
                    html_str = f"""
                    <h4 style="text-align:center;text-decoration: underline;">{recommended_movie_names[counter]}</h4>
                    <h5>Overview:</h5> <p>{overview}</p> 
                    <h5>Genres:</h5> <p>{genres}</p>
                    <h5>Cast:</h5> <p>{cast}</p> 
                    <h5>Director:</h5> <p>{crew}</p> 
                    <h5>Rating:</h5> <p style="font-size:26px;color:rgb(4, 217, 255)">{vote_average}</p> 
                    """
                    st.markdown(html_str, unsafe_allow_html=True)
            counter += 1

elif choice == "Books":
    st.subheader("Books")
    selected_book = st.selectbox("Type or select a book from the dropdown", book_list)
    if st.button("Show Recommendation"):
        recommended_book_names, recommended_book_posters = recommendbook(selected_book)
        col1, col2, col3, col4 = st.columns(4)
        counter = 0
        for col in st.columns(4):
            with col:
                st.text(recommended_book_names[counter])
                st.image(recommended_book_posters[counter])
                with st.expander("Details"):
                    (
                        title,
                        author,
                        publisher,
                        genres,
                        language,
                        description,
                        rating,
                    ) = book_details(recommended_book_names[counter])
                    html_str = f"""
                    <h4 style="text-align:center;text-decoration: underline;">{title}</h4>
                    <h5>Author:</h5> <p>{author}</p> 
                    <h5>Publisher:</h5> <p>{publisher}</p>
                    <h5>Genres:</h5> <p>{genres}</p> 
                    <h5>Language:</h5> <p>{language}</p> 
                    <h5>Rating:</h5> <p style="font-size:26px;color:rgb(4, 217, 255)">{rating}</p> 
                    <h5>description:</h5> <p>{description}</p>
                    """
                    st.markdown(html_str, unsafe_allow_html=True)
            counter += 1
        counter = 4
        for col in st.columns(4):
            with col:
                st.text(recommended_book_names[counter])
                st.image(recommended_book_posters[counter])
                with st.expander("Details"):
                    (
                        title,
                        author,
                        publisher,
                        genres,
                        language,
                        description,
                        rating,
                    ) = book_details(recommended_book_names[counter])
                    html_str = f"""
                    <h4 style="text-align:center;text-decoration: underline;">{title}</h4>
                    <h5>Author:</h5> <p>{author}</p> 
                    <h5>Publisher:</h5> <p>{publisher}</p>
                    <h5>Genres:</h5> <p>{genres}</p> 
                    <h5>Language:</h5> <p>{language}</p> 
                    <h5>Rating:</h5> <p style="font-size:26px;color:rgb(4, 217, 255)">{rating}</p> 
                    <h5>description:</h5> <p>{description}</p> 
                    """
                    st.markdown(html_str, unsafe_allow_html=True)
            counter += 1

elif choice == "Songs":
    st.subheader("Songs")
    selected_song = st.selectbox("Type or select a song from the dropdown", song_list)
    if st.button("Show Recommendation"):
        recommended_song_names, recommended_song_posters = recommendsong(selected_song)
        col1, col2, col3, col4 = st.columns(4)
        counter = 0
        for col in st.columns(4):
            with col:
                st.text(recommended_song_names[counter])
                st.image(recommended_song_posters[counter])
                with st.expander("Details"):
                    (
                        song_name,
                        artist_name,
                        playlist,
                        genres,
                        lyrics,
                        popularity,
                    ) = song_details(recommended_song_names[counter])
                    html_str = f"""
                    <h4 style="text-align:center;text-decoration: underline;">{song_name}</h4>
                    <h5>Artist:</h5> <p>{artist_name}</p> 
                    <h5>Playlist:</h5> <p>{playlist}</p>
                    <h5>Genres:</h5> <p>{genres}</p> 
                    <h5>Popularity:</h5> <p style="font-size:26px;color:rgb(4, 217, 255)">{popularity}</p> 
                    <h5>Lyrics:</h5> <p>{lyrics}</p> 
                    """
                    st.markdown(html_str, unsafe_allow_html=True)
            counter += 1
        counter = 4
        for col in st.columns(4):
            with col:
                st.text(recommended_song_names[counter])
                st.image(recommended_song_posters[counter])
                with st.expander("Details"):
                    (
                        song_name,
                        artist_name,
                        playlist,
                        genres,
                        lyrics,
                        popularity,
                    ) = song_details(recommended_song_names[counter])
                    html_str = f"""
                    <h4 style="text-align:center;text-decoration: underline;">{song_name}</h4>
                    <h5>Artist:</h5> <p>{artist_name}</p> 
                    <h5>Playlist:</h5> <p>{playlist}</p>
                    <h5>Genres:</h5> <p>{genres}</p> 
                    <h5>Popularity:</h5> <p style="font-size:26px;color:rgb(4, 217, 255)">{popularity}</p> 
                    <h5>Lyrics:</h5> <p>{lyrics}</p> 
                    """
                    st.markdown(html_str, unsafe_allow_html=True)
            counter += 1

else:
    st.subheader("About")
