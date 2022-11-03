import random
from xml.etree.ElementPath import get_parent_map

college_data = []
college = [
    {"college": "Brown University", "gpa": "3.94", "ec": "7", "award": "9", "lead": "5", "white": "43", "hispanic": "11", "africanamerican": "7", "asian": "17", "otherrace": "22", "cs": "10", "business": "4", "bio": "10", "politics": "5", "engineer": "6", "ss": "18", "english": "6", "othermajor": "41", "acceptrate": "7.7", "sat": "1420", "act": "32", "gendermale": "48", "genderfemale": "52", "essay": "9"},
    {"college": "Columbia University", "gpa": "3.91", "ec": "5", "award": "9", "lead": "5", "white": "34", "hispanic": "14", "africanamerican": "7", "asian": "18", "otherrace": "27", "cs": "11", "business": "2", "bio": "5", "politics": "9", "engineer": "12", "ss": "26", "english": "5", "othermajor": "30", "acceptrate": "5.9", "sat": "1450", "act": "33", "gendermale": "49", "genderfemale": "51", "essay": "8"},
    {"college": "Cornell University", "gpa": "3.98", "ec": "5", "award": "8", "lead": "4", "white": "36", "hispanic": "14", "africanamerican": "7", "asian": "20", "otherrace": "23", "cs": "13", "business": "14", "bio": "13", "politics": "4", "engineer": "14", "ss": "9", "english": "1", "othermajor": "32", "acceptrate": "10.9", "sat": "1420", "act": "32", "gendermale": "46", "genderfemale": "54", "essay": "8"},
    {"college": "Dartmouth College", "gpa": "3.9", "ec": "4", "award": "6", "lead": "3", "white": "51", "hispanic": "11", "africanamerican": "6", "asian": "15", "otherrace": "17", "cs": "7", "business": "17", "bio": "8", "politics": "16", "engineer": "10", "ss": "35", "english": "3", "othermajor": "4", "acceptrate": "7.9", "sat": "1450", "act": "32", "gendermale": "51", "genderfemale": "49", "essay": "9"},
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
def getData():
    return(college_data)

# Joke getter
def getJoke(id):
    return(college_data[id])

# Pretty Print joke
def printJoke(joke):
    print(joke['id'], joke['joke'], "\n")

# Test Joke Model
if __name__ == "__main__": 
    initData()  # initialize jokes
    
    # Count of Jokes
    print("Jokes Count: " + str(countJokes()))