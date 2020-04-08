import sys
a = [1, 11, 21, 1211, 111221]

class LookAndSaySequence:
    def __iter__(self):
        self.nextElement = 1
        return self

    def __next__(self):
        x = self.nextElement
        self.nextElement = self.getNextElement()
        return x

    def getNextElement(self):
        nextElement = self.nextElement
        stringed = str(self.nextElement)
        i = 0
        while i < stringed:
            # The element has already occoured once
            occouranceCount = 1
            # The value we have to look forward to
            value = int(stringed[i])
            if stringed[i]:
                i += 1

        return nextElement

LASSeq = LookAndSaySequence()
iterator = iter(LASSeq)

i = 0
while i < 3:
    print(next(iterator))
    i += 1

# Fuuuck...
# I thought this was a sequence in base 3, and it turns out
# it is not. It's the LOOK-AND-SAY SEQUENCE.
# In the end, it's my fault. For not looking it up on the Internet.
def baseToNumber(numberinBase, baseOfNumberInBase):
    number = 0
    i = len(numberinBase)
    for item in numberinBase:
        i = i - 1
        number = number + item * baseOfNumberInBase**(i)

    return number

#parseda = []
#for number in a:
#    parseda.append([int(x) for x in str(number)])
#
#for number in parseda:
#    print(baseToNumber(number, 3))


