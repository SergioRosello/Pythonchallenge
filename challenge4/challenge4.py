# It seems to be a linked list, but we have to request the information to the server, no?
# While the return value has no key in my dict, ask for another index more

import requests
import re

def getValueforIndex(i):
    body = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={i}".format(i=i))
    print ( body.text )
    return re.search(r'[0-9]+', body.text).group(0)

#value = 12345
#value = 16044/2
value = 63579
while True:
    value = getValueforIndex(value)

