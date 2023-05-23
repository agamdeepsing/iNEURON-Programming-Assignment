
# Ques 1
def evenDiv(a,b,c):
    divList = []
    for num in range(a,b+1):
        if num%c == 0:
            divList.append(num)
    print(f'{sum(divList)}')

evenDiv(1,10,20)
evenDiv(1,10,2)
evenDiv(1,10,3)




# Ques 2
def checkEquality():
    string = input('Enter the inequality: ')
    output = eval(string)
    print(f'{output}')

for x in range(3):
    checkEquality()


# Ques 3
def replaceVowels():
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    string = input("String: ")
    string_copy = string
    char = input('Replacement character: ')
    for i in string:
        if i in vowels:
            string = string.replace(i,char)
    print(f' {string}')
            
for x in range(3):
    replaceVowels()


# Ques 4
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

print(f'{factorial(5)}')
print(f'{factorial(3)}')
print(f'{factorial(1)}')
print(f'{factorial(0)}')



# Ques 5
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")
    
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    
    return distance

str1 = "abcbba"
str2 = "abcbda"
distance = hamming_distance(str1, str2)
print(distance)
