# CS361---Sprint-2--MoodRing-MicroService
Microservice with utility to select random song from JSON DB matching criteria

For route handling the program uses Flask, so ensure a free port during testing.

a. How to make a request:
  The microservice can use both GET requests via URL and POST requests via text/json request bodies.

  GET Request:
    To make a GET request provide URL path of /mood/*insert-mood* Ex. http://localhost:3000/mood/Happy 
    This will activate the route handler to execute the microservice of aquiring a song that falls within the corresponding JSON Array DB

  POST Request:
    Originally we had discussed allowing retrieval via POST request, so there are two methods requesting via POST:
      text/plain: To make a POST request of content type text/plain submit the request to the path /mood Ex: http://localhost:3000/mood
                  The format for the plain text request body is solely the mood that is requested. Ex: Sad
      application/json: To make a POST request of content type application/json submit the request body to the path /mood Ex: http://localhost:3000/mood
                  The format for the json request body is {"mood" : *insert mood*}  Ex. {"mood" : "Angry"}
    Either form of request will be handled and then utilized in the same method as the GET request shown above


b. How to recieve data:
   After performing the process of obtaining a random song the route handler returns a response of a single JSON song that was found matching the criteria requested
   In the case where no song is found matching the criteria requested a response message of Content-Type:text/html "No Songs Found with mood: *Requested Mood* "


c.
