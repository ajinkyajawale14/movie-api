# fynd-movie-api

python backend developement using rest-api. This api is serving django backend architecture

    • Python backend developement using django rest framework
    • RestApi for search movies functionality
    • uses imbd.json data 

Setting up the project

To access the API please follow below steps:-

1. Clone the github repo to localhost

    1. Create a folder- mkdir fynd-movie-api
    2. Go to folder-  cd fynd-movie-api
    3. if you already have git then just clone the github project- 
      https://github.com/ajinkyajawale14/fynd-movie-api.git
    4. Extract the folder contents

2. Create Virtual Environment fynd-env
    1. virtualenv fynd-env
    2. source fynd-env/bin/activate

3. install dependecies-
    1. install dependencies- pip install -r requirements.txt
    2. make migrations- python manage.py migrate
    3. fire up the app to localhost by starting the server-
       python manage.py runserver 
      open the browser and run- http://127.0.0.1:8000/

Api Documentation:
    api root - root movie search api:
    link- http://127.0.0.1:8000/
    
   To list all the movies
      link- (http://127.0.0.1:8000/movies/)
      
   • At the bottom To add the movie-
      you can see the added movie in the data
      
   Name: Saw
   Director: James Wan
   Score: 7.0
   Popularity: 78

   • For Search movie by their name, search for the movie:
      http://127.0.0.1:8000/movies/?search=The+Godfather

   • for searching extensively- added the filter feature such as ordering for e.g. ascending popularity
      http://127.0.0.1:8000/movies/?ordering=-popularity

*this sort the list by the ascending and descending order

 #filer the api according to the search query:-
http://127.0.0.1:8000/movies/?ordering=-popularity&search=love

returns all the movie contains string “love” and sequencing them in ascending popularity

this app is deployed to heroku- 
    
   1. fynd-movie-api:
    https://fynd-movie-api.herokuapp.com/
    
   2. api for search movie:
    https://fynd-movie-api.herokuapp.com/movies/
    
   3. add the new movie:
        Name: Saw
        Director: James Wan
        Score: 7.0
        Popularity: 78
    
   4. Get the movie list resource in json format
    https://fynd-movie-api.herokuapp.com/movies/?format=json
    
   5. Get the movie list resource in api format
    https://fynd-movie-api.herokuapp.com/movies/?format=api
    
   6. get the movie as in search query (movie with sub-string love)
    https://fynd-movie-api.herokuapp.com/movies/?search=love
    
   7. order the movies in ascending order of the names:
    https://fynd-movie-api.herokuapp.com/movies/?ordering=name&search=love
    
   8. order the movies in descending order of the names:
    https://fynd-movie-api.herokuapp.com/movies/?ordering=-name&search=love
    
   9. order the movies in ascending order of the director names:
    https://fynd-movie-api.herokuapp.com/movies/?ordering=director&search=love
    
   10. order the movies in descending order of the director names:
    https://fynd-movie-api.herokuapp.com/movies/?ordering=-director&search=love
    
   11. order the movies in ascending order of the score:
    https://fynd-movie-api.herokuapp.com/movies/?ordering=score&search=love
    
   12. order the movies in descending order of the score:
    https://fynd-movie-api.herokuapp.com/movies/?ordering=-score&search=love
    
   13. order the movies in the ascending order of the Popularity:
    https://fynd-movie-api.herokuapp.com/movies/?ordering=popularity&search=love
    
   14. order the movies in descending order of the Popularity:
    https://fynd-movie-api.herokuapp.com/movies/?ordering=-popularity&search=love
    
   15. order the movies in ascending order of the Genre:
    https://fynd-movie-api.herokuapp.com/movies/?ordering=genres__name&search=love
    
   16. order the movies in descending order of the Genre:
    https://fynd-movie-api.herokuapp.com/movies/?ordering=-genres__name&search=love

   • Further work
    1. search the movies based on the genre
    2. add custome user model
       
      
