message = "http://www.pythonchallenge.com/pc/def/map.html"
decoded = ""

for character in message:
    if ( ord(character) >= 97 and ord(character) < 122 ):
        decoded = decoded + chr(ord(character) + 2)
    else:
        decoded  = decoded + character

print ( decoded )

