import random
from xml.etree.ElementPath import get_parent_map

college_data = []
college = [
    {"college": "Brown University", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "engineer": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""},
    {"college": "Columbia University", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "engineer": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""},
    {"college": "Cornell University", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "engineer": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""},
    {"college": "Dartmouth College", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "engineer": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""},
    {"college": "Harvard University", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "engineer": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""},
    {"college": "UPenn", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "engineer": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""},
    {"college": "Princeton University", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "engineer": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""},
    {"college": "Yale University", "gpa": "", "ec": "", "award": "", "lead": "", "white": "", "hispanic": "", "africanamerican": "", "asian": "", "otherrace": "", "cs": "", "business": "", "bio": "", "politics": "", "engineer": "", "ss": "", "engineer": "", "othermajor": "", "acceptrate": "", "sat": "", "act": "", "gendermale": "", "genderfemale": "", "essay": ""}
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