
# Ques 1
from math import sqrt
def calculateD():
    number = eval(input("Enter the number: "))
    prints = []
    C= 50
    H = 30
    for i in number:
        Q = str(int(sqrt((2*C*i)/H)))
        prints.append(Q)
    print("Output: {}".format(','.join(prints)))

calculateD()

# Ques 2
def generateArray():
    x = int(input('Enter the No of Rows:'))
    y = int(input('Enter the No of Columns:'))
    
    out_array = [[ele * sub_ele for sub_ele in range(y)] for ele in range(x)]
    print(out_array)

generateArray()

# Ques 3
def sortString():
    string = input("Enter the Input String: ")
    outstring = ','.join(sorted(string.split(',')))
    print(f'Output: {outstring}')
    
sortString()


# Ques 4

def sort():
    string = input("Enter the Input String: ")
    outputstring = ' '.join(sorted(sorted(list(set(string.split(" "))))))
    print(f'Output: {outputstring}')
    
sort()


# Ques 5

def countLetterAndDigits():
    string = input("Enter the Input String: ")
    letters = sum(1 for i in string if i.isalpha())
    digits = sum(1 for i in string if i.isdigit())
    print(f'LETTERS: {letters}\nDIGITS: {digits}')
        
countLetterAndDigits()



# Ques 6

def password():
    string = input("Enter the string: ")
    smallletters = "abcdefghijklmopqrstuvwxyz"
    capitalletters = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
    specialletters = "$#@!%^&"
    number = "0123456789"
    '''The function password() is defined. It initializes some variables: smallletters, capitalletters, specialletters, and number. These variables contain the characters that define specific criteria for a valid password.'''

    for i in string.split(","):
        if len(i) <= 12 and len(i) >=6 :
            if any(j.isupper() for j in i):
                if any(i.islower() for j in i):
                    if any(j for j in i if j in specialletters):
                        print(i)
                               
password() 
#If a string meets all these criteria, it is printed out.
