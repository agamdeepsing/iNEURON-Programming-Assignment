
# Ques 1
sentence = "hello my name is agamdeep singh and I am currently learning data science(proficient in python,Sql,data analytics,little bit of machine learning)"
length = 4
s = sentence.split()
print([a for i, a in enumerate(s) if len(a) > length])


# Ques 2

inputstring = input("Enter the String: ")
inputnum = int(input("Enter the ith Character: "))
outputstring = ''
for i in range(len(inputstring)):
    if i != inputnum:
        outputstring = outputstring + inputstring[i]
print(outputstring)
    


# Ques 3
s = "Ineuron full stack data science course"
print(s.split(" "))
print("-".join(s.split()))


# Ques 4
string = input("Enter the integer value")
if all(i in ['0','1']for i in string):
    result = "binary string"
else:
    result = "not a binary string"
print(f'{string} {result}')


# Ques 5
string1 = set(input("Enter the String : ").split(' '))
string2 = set(input("Enter the String : ").split(' '))
output = (string1.union(string2)).difference(string1.intersection(string2))
print(output)

# Ques 6

string = input("enter any sentense: ")
x = []
for i in string:
    if i not in x and string.count(i)>1:
        x.append(i)
print("".join(x))

# Ques 7

import string
 
def check_string(s):
    for i in s:
        if i in string.punctuation:
            print("String not accepted")
            return
    print("String is accepted")
 
check_string(input("enter string with special character to check whether it is running or not"))