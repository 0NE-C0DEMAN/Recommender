# Build with
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/downloads/release/python-380/)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/static/v1?style=for-the-badge&message=Streamlit&color=FF4B4B&logo=Streamlit&logoColor=FFFFFF&label=)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/posts/hitesh-chaudhari-0259ba14a_project-collaboration-content-activity-6921523549367095296-iEiW?utm_source=linkedin_share&utm_medium=member_desktop_web)

# Recommender

A web App deployed on HEROKU CLOUD/Strealit CLoud ,that recommends MOVIES, SONGS and BOOKS.

You can try out this app [here.](https://share.streamlit.io/hitman-dev/recommender/main/app.py)

![Screenshot](images/UI_info.JPG)

### What are Recommendation systems

Recommender systems are the systems that are designed to recommend things to the user based on many different factors. These systems predict the most likely product that the users are most likely to purchase and are of interest to. Companies like Netflix, Amazon, etc. use recommender systems to help their users to identify the correct product or movies for them. 

The recommender system deals with a large volume of information present by filtering the most important information based on the data provided by a user and other factors that take care of the user’s preference and interest. It finds out the match between user and item and imputes the similarities between users and items for recommendation. 

### Project overview
In this project ,we have designed a recommendation system that recommends MOVIES, SONGS and BOOKS based on the input given by the user, this is a content based recommendation system.
This system also shows Details of the recommended output .In this system the recommendation is made by using Cosine Similarity function

### Datasets Used

Below are the links used to train the Recommender model

Movie dataset :- 'https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata'

Book dataset :- 'https://zenodo.org/record/4265096'

Song dataset :- 'https://www.kaggle.com/datasets/saurabhshahane/spotgen-music-dataset'

### Deployment 
This app can be deployed on Heroku Cloud and also Streamlit Cloud , this repo contains all the necessary files for deployment

### What is Cosine Similarity?

Mathematically Cosine similarity measures the similarity between two vectors of an inner product space. It is measured by the cosine of the angle between two vectors and determines whether two vectors are pointing in roughly the same direction. It is often used to measure document similarity in text analysis.

In Python the cosine similarity measures the similarity between vector lists by calculating the cosine angle between the two vector lists. If you consider the cosine function, its value at 0 degrees is 1 and -1 at 180 degrees. This means for two overlapping vectors, the value of cosine will be maximum and minimum for two precisely opposite vectors.

You can get more information about cosine Similarity [here.](https://www.delftstack.com/howto/python/cosine-similarity-between-lists-python/#use-the-scipy-module-to-calculate-the-cosine-similarity-between-two-lists-in-python)
Here we have used [cosine_similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) function from sklearn.

```python
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vector)
similarity
```

###  Feature extraction (or vectorization)
Scikit-learn’s CountVectorizer is used to convert a collection of text documents to a vector of term/token counts. It also enables the pre-processing of text data prior to generating the vector representation. This functionality makes it a highly flexible feature representation module for text.
You can get more information about cosine Similarity [here.](https://www.educative.io/edpresso/countvectorizer-in-python)
Here we have done vectorization using [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) function from sklearn

```python
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(stop_words='english')
vector = cv.fit_transform(new['tags']).toarray()
```


Than we made a function which gives the recommendation based on the given input.
```python
def recommend(movie):
    index = new[new['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:7]:
        print(new.iloc[i[0]].title)
```
 # Flow of Application
 ### Selection of Input
 The app assists in selection of input (Movie, Song, Book)
![Screenshot](images/select.JPG)
### Recommended Output
The app shows recommendation based on the given input.
![Screenshot](images/recommended_op.JPG)
### Detailed Recommended Output
The app also shows respective details based on the recommended output.
![Screenshot](images/Details.JPG)
# Theme
The app also has feature to change its Theme , we can select white theme or dark theme or device oriented theme
![Screenshot](images/theme.JPG)

 # Collaboration 
 This project is collaborative work of:-
 
#### Hitesh Chaudhari
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/hitesh-chaudhari-0259ba14a/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/hitman-dev)
 
#### Siddhant Mishra
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/siddhant-mishra-02aa50110/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/0NE-C0DEMAN)

