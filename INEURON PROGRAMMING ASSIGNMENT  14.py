
# Ques 1

class divgen:
    def __init__(self,inputnumber):
        self.inputnumber = inputnumber
    def number(self):
        for i in range (0, self.inputnumber+1):
            if i % 7 == 0:
                yield i
output = divgen()
for i in output.numbers():
    print(i,end=' ')


# Ques 2
import operator

text = input("Type in: ")

freq = {}

for i in text.split(' '):
    if i.isalpha():
        if i not in freq:
            freq[i] = 1
        elif i in freq:
            freq[i] = freq[i] + 1
    else:
        pass

sorteddict = sorted(freq.items(), key = operator.itemgetter(0))
print(sorteddict)

for i in sorteddict:
    print(i[0], i[1])


# Ques 3
class person:
    def getGender():
        pass

class Male(person):
    def getGender():
        print("Male")

class Female(person):
    def getGender():
        print("Female")

Male.getGender()
Female.getGender()


# Ques 4
def generateSentences():
    subject = ['I','You']
    verb = ['Play','Love']
    object = ['Hockey','Football']
    for i in subject:
        for j in verb:
            for k in object:
                print(f'{i} {j} {k}')

generateSentences()


# ques 5
import zlib
s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s.encode('utf-8'))
print(t)
print(zlib.decompress(t))



# Ques 6
def binarysearch(array, target):
    lower1 = 0
    upper1 = len(array)
    print(upper1)
    while lower1 < upper1:
        x = (lower1 + upper1) // 2
        print('Middle Value:',x)
        value = array[x]
        if target == value:
            return x
        elif target > value:
            lower = x
        elif target < value:
            upper = x

Array = [1,5,8,10,12,13,55,66,73,78,82,85,88,99]
print(binarysearch(Array, 82))

