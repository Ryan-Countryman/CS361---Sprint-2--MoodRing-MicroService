# CS361 - Ryan Countryman
# Database management and tools utilized to select random song selection
import json
import random

class mood_DB:
    def __init__(self, filename): #Constructor, Upon class creation supply local JSON file containing DataBase
          self.filename = filename
          self.data = None
          
    def load_data(self): #Loads JSON file with error handling
        try:
            with open(self.filename,"r") as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as event:
            print(f"Error loading file {event}")

    def get_song_list(self,mood):#Intakes desired mood and returns array of corresponding songs
        if self.data is None:
              self.load_data()
        return self.data.get(mood,[])

def randomizer(max):
    randomizedIndex = random.randint(0,max)
    return randomizedIndex

def provideSong(mood):
    moodDb = mood_DB("moodring.json") #Change JSON to match DB file if needed
    results = moodDb.get_song_list(mood)
    if(len(results) > 1): #Safety check to ensure no reaching out of bounds
        selection = randomizer(len(results) - 1)
        results = results[selection]
    else:
        results = ""

    return results