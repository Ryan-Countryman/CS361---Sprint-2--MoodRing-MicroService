# CS361 - Ryan Countryman
# Route Handling for HTTP request for communication to Microservice
# Accepts GET Requests via URL // POST Requests via JSON or Text
# GET URL FORMAT: *insert domain*/mood/*desired mood for song*
# POST JSON FORMAT: {"mood": "*insert desired mood*"}
# POST TEXT FORMAT: *insert desired mood*
# See Test-Requests.http for testing examples 
from flask import Flask, request
from AquireMoodTools import provideSong

app = Flask(__name__)

@app.route("/mood/<string:mood>" , methods=['GET'])
def microMain(mood):
    mood.lower() #Lower full string to maintain consistency of request
    selectedSong = provideSong(mood.capitalize()) #Invoke database operation to select random song with matching criteria
    if(selectedSong != ""):
        return selectedSong
    else:
        return f"No Songs Found with mood: {mood}"

@app.route("/mood" , methods=['POST'])
def postContentHandling():
    
    reqType = request.content_type

    if(reqType == 'text/plain'): #TEXT Handling
        mood = request.data.decode('utf-8')
  
    elif(reqType == 'application/json'): #JSON Handling
        reqData = request.json
        mood = reqData.get('mood','')
    else:
        return "DATA TYPE NOT SUPPORTED"
  
    mood.lower() 
    selectedSong = provideSong(mood.capitalize()) 
    if(selectedSong != ""): #Song Found
        return selectedSong
    else:
        return f"No Songs Found with mood: {mood}"
    
#Change host and Port for application usage
if __name__ == '__main__':
    app.run(host='localhost', port=3000)