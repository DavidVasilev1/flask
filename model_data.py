import random
from xml.etree.ElementPath import get_parent_map

college_data = []
college = [
    {"college": "Brown University", "gpa": "3.94", "ec": "7", "award": "9", "lead": "5", "white": "43", "hispanic": "11", "africanamerican": "7", "asian": "17", "otherrace": "22", "cs": "10", "business": "4", "bio": "10", "politics": "5", "engineer": "6", "ss": "18", "english": "6", "othermajor": "41", "acceptrate": "7.7", "sat": "1420", "act": "32", "gendermale": "48", "genderfemale": "52", "essay": "9"},
    {"college": "Columbia University", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "english": "", "othermajor": "", "acceptrate": "5.9", "sat": "1450", "act": "33", "gendermale": "49", "genderfemale": "51", "essay": "8"},
    {"college": "Cornell University", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "english": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""},
    {"college": "Dartmouth College", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "english": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""},
    {"college": "Harvard University", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "english": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""},
    {"college": "UPenn", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "english": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""},
    {"college": "Princeton University", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "english": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""},
    {"college": "Yale University", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "english": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""}
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