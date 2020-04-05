text = open("file.txt","r").read()

# Scan the string, to print only alphabet letters print (str1)

# My initial solution:
finalString = ""

for c in text:
    if c.isalpha():
       finalString = finalString + c 

print(finalString)

# A more "python" solution
print("".join([char for char in text if char.isalpha()]))
