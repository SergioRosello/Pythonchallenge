import re
from zipfile import ZipFile
# Create a ZipFile Object and load sample.zip in it
with ZipFile('channel.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall("unzipped")

match = 90052
string = ""
while True:
    # Tenemos el archivo
    file= "./unzipped/{n}.txt".format(n=match)
    # Imprimimos su contenido
    #print(file.read())
    match = re.search(r'[0-9]+', open(file, 'r').read())
    #print(match.group(0))
    if match == None :
        break
    match = match.group(0)
    # join to the string that file's comment
    string = string + string.join(ZipFile('channel.zip', 'r').getinfo(file.split('/')[2]).comment.decode())

print(string)


# This has told me to collect the comments.
# I suppose I will iterate over every file, and collect the lines containing a #

# Reading the zipped file comments
