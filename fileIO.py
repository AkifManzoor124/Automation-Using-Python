# Open the file inputFile.txt from the exercise file
# We will be using the open function and find the file within the exercise folder

import json

def print_contents_of_file(path):
    f = open(path, 'r')
    print(f.read())
    f.close()

def find_within_file(path, find):
    found = []
    f = open(path, 'r')
    for content in f:
        if(find in content):
            found.append(content)
    return found

paths = json.load(open('paths.json'))

inputFilePath = paths["Input File"]
passFailFilePath =  paths["passFail File Path"]

# ## The following function successfully opens the file inputFile
# ## Reads the content and then prints it into terminal
# ## Then closes the file

print_contents_of_file(inputFilePath)


# ## Now we are going to find all the people who passed and failed
# ## Put them into an array

passed = find_within_file(inputFilePath, "P")
failed = find_within_file(inputFilePath, "F")

print(passed)
print(failed)

# ## We are going to be writing a file using python
# ## We're going to save all the passes and failed into the file

passFailFile = open(passFailFilePath, 'w')

for person in passed:
    passFailFile.write(person)

for person in failed:
    passFailFile.write(person)

print_contents_of_file(passFailFilePath)