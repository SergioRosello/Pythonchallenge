import re

text = open("file.txt","r").read()

print ("".join(re.findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", text) ))

