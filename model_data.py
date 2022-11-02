import random

college_data = []
college = [
    "Brown University",
    "Brown University",
    "Columbia University",
    "Cornell University",
    "Dartmouth College",
    "Harvard University",
    "UPenn",
    "Princeton University",
    "Yale University"
]

# Initialize jokes
def initData():
    # setup jokes into a dictionary with id, joke, haha, boohoo
    for item in college:
        college_data.append({"college": item})
        
# Return all jokes from jokes_data
def getJokes():
    return(college_data)

# Joke getter
def getJoke(id):
    return(college_data[id])

# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['joke'], "\n")

# Number of jokes
def countJokes():
    return len(college_data)

# Test Joke Model
if __name__ == "__main__": 
    initData()  # initialize jokes
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))