
# Ques 1
def amplify(inputnum):
    output = []
    for i in range(1,inputnum+1):
        if i%4 == 0:
            output.append(i*10)
        else:
            output.append(i)
    print(f'{output}')

amplify(4)
amplify(3)
amplify(25)



# Ques 2
numbers = [1, 2, 2, 3, 3, 4, 5]
unique = list(set(numbers))
print(unique)

            OR  

numbers = [1, 2, 2, 3, 3, 4, 5]


def uniquenumbers(numbers):

    list1 = []

    unique_numbers = set(numbers)

    for number in unique_numbers:
        list1.append(number)

    return list1


print(uniquenumbers(numbers))


# Ques 3
import math

def getArea(radius):
    return math.pi * radius**2

def getPerimeter(radius):
    return 2 * math.pi * radius

radius1 = 11
area1 = getArea(radius1)
perimeter1 = getPerimeter(radius1)
print(f"Area: {area1}") 
print(f"Perimeter: {perimeter1}")  

radius2 = 4.44
area2 = getArea(radius2)
perimeter2 = getPerimeter(radius2)
print(f"Area: {area2}")  
print(f"Perimeter: {perimeter2}")  



# Ques 4
def sortlength(in_list):
    print(sorted(in_list,key=len))

sortlength(["Google", "Apple", "Microsoft"])
sortlength(["Leonardo", "Michelangelo", "Raphael", "Donatello"])
sortlength(["Turing", "Einstein", "Jung"])


# Ques 5
def is_triplet(a,b,c):
    if ((a**2+b**2) == (c**2)):
        print(f'{a,b,c} ➞ {True}')
    else:
        print(f'{a,b,c} ➞ {False}')
        
is_triplet(3, 4, 5)
is_triplet(3, 4, 5)
is_triplet(1, 2, 3)

