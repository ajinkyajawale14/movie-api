# fynd-movie-api

python backend developement using rest-api. This api is serving django backend architecture

    • Python backend developement using django rest framework
    • RestApi for search movies functionality
    • uses imbd.json data 

Setting up the project

To access the API please follow below steps:-

1. Clone the github repo to localhost

    • Create a folder- mkdir fynd-movie-api
    • Go to folder-  cd fynd-movie-api
    • if you already have git then just clone the github project- 
      https://github.com/ajinkyajawale14/fynd-movie-api.git
    • Extract the folder contents

2. Create Virtual Environment fynd-env
    • virtualenv fynd-env
    • source fynd-env/bin/activate
you should able to see the changed environment like this-
      

    • install dependencies- pip install -r requirements.txt
    • make migrations- python manage.py migrate
    • fire up the app to localhost by starting the server-
       python manage.py runserver 
      open the browser and visit- http://127.0.0.1:8000/
      you will able to see the app like this 


Api Documentation:

    • api root- root movie search api
      link- http://127.0.0.1:8000/
    • To list all the movies
      link- http://127.0.0.1:8000/movies/
      
    • At the bottom To add the movie-
      you can see the added movie in the data
      




    • For Search movie by their name, search for the movie:
    • http://127.0.0.1:8000/movies/?search=The+Godfather

      



















    • for searching extensively- added the filter feature such as ordering for e.g. ascending popularity
      http://127.0.0.1:8000/movies/?ordering=-popularity



this will sort the list by the ascending and descending order

filer the api according to the search query:-
http://127.0.0.1:8000/movies/?ordering=-popularity&search=love

returns all the movie contains string “love” and sequencing them in ascending popularity
