
# Ques 1
def stutterWord():
    string = input('Enter the Word: ')
    output = f"{string[:2]}... {string[:2]}... {string}?"
    print(f'{string} ➞ {output}')

for i in range(3):
    stutterWord()


# Ques 2
import math
def Degree():
    inputnumber = int(input('Enter the angle in Radians: '))
    outputnumber = (180/math.pi)*inputnumber
    print(f'{outputnumber:.1f} degrees')

for x in range(3):
    Degree()


# Ques 3
def check():
    num = int(input("Enter a number: "))
    if (pow(2,num)+1)%((2*num)+1) == 0:
        print(f'{num} is a Curzon Number')
    else:
        print(f'{num} is Not a Curzon Number')

for x in range(4):
    check()



# Ques 4
import math
def areaOfHexagon():
    inputnumber = int(input('Enter the side length: '))
    outputnumber = ((3*math.sqrt(3))/2)*(pow(inputnumber,2))
    print(f'{outputnumber:.1f}')
    
for x in range(3):
    areaOfHexagon()



# Ques 5
def getBinary():
    inputnum = int(input("Enter a Number: "))
    outputnum = bin(inputnum).replace('0b','') 
    print(f'Binary of {inputnum} ➞ {outputnum}')

for x in range(3):
    getBinary()

