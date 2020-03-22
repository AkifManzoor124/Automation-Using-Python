# We will be using the subprocess library to invoke terminal commands
# using python

import subprocess
import json


paths = json.load(open('paths.json'))

helloWorldFile = paths["helloWorld Python File"]
print(helloWorldFile)

for i in range(5):
    subprocess.run(["py", helloWorldFile], shell=True)