from itertools import groupby

#a = [1, 11, 21, 1211, 111221]

class LookAndSaySequence:
    def __iter__(self):
        self.nextElement = 1
        return self

    def __next__(self):
        x = self.nextElement
        self.nextElement = self.getNextElement()
        return x

    def getNextElement(self):
        groups = groupby(str(self.nextElement))
        counts = [(label, sum(1 for _ in group)) for label, group in groups]
        return int("".join("{}{}".format(count, label) for label, count in counts))

LASSeq = LookAndSaySequence()
iterator = iter(LASSeq)

i = 0
while i < 30:
    next(iterator)
    i += 1
print(len(str(next(iterator))))

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
