import os,json

    
directory = os.getcwd()

 
# Opening JSON file
f = open(directory + "/LiveSportsWebsite/data2.json")
 
# returns JSON object as
# a dictionary

data = f.read()


data = data.replace("'",'"' )

print(data)