
# Ques 1
def sumlist():
    hey = int(input('Enter the No of Entries in a List: '))
    output = []
    for i in range(hey):
        output.append(int(input('Enter a element: ')))
    print(f'Sum of Elements: {sum(hey)}')

sumlist()

# Ques 2
def mullist():
    hey = int(input('Enter the No of Entries in a List: '))
    output = []
    mul = 1
    for i in range(hey):
        output.append(int(input('Enter a element: ')))
    for j in output:
        mul = mul * j 
    print(mul)

mullist()

# Ques 3
def smalllist():
    hey = int(input('Enter the No of Entries in a List: '))
    output = []
    for i in range(hey):
        output.append(int(input('Enter a element: ')))
    print(f'The Smallest Element in {output} is {sorted(output)[0]}')

smalllist()

# Ques 4
def largestlist():
    hey = int(input('Enter the No of Entries in a List: '))
    output = []
    for i in range(hey):
        output.append(int(input('Enter a element: ')))
    print(f'The largest in {output} is {sorted(output, reverse = True)[0]}')

largestlist()

# Ques 5
def seclargestlist():
    hey = int(input('Enter the No of Entries in a List: '))
    output = []
    for i in range(hey):
        output.append(int(input('Enter a element: ')))
    print(f'The seclargest in {output} is {sorted(output, reverse = True)[1]}')

seclargestlist()

# Ques 6
def Nlargestlist(k):
    hey = int(input('Enter the No of Entries in a List: '))
    output = []
    for i in range(hey):
        output.append(int(input('Enter a element: ')))
    print(f'The {k} largest in {output} is {sorted(output, reverse = True)[0:k]}')

Nlargestlist(5)

# Ques 7
def evenlist():
    hey = int(input('Enter the No of Entries in a List: '))
    output = []
    even = []
    for i in range(hey):
        output.append(int(input('Enter a element: ')))
    for i in output:
        if i%2 ==0:
            even.append(i)
    print(f'The even in {output} are {even}')

evenlist()

# Ques 8
def oddlist():
    hey = int(input('Enter the No of Entries in a List: '))
    output = []
    odd = []
    for i in range(hey):
        output.append(int(input('Enter a element: ')))
    for i in output:
        if i%2 !=0:
            odd.append(i)
    print(f'The odd in {output} are {odd}')

oddlist()


# Ques 9 
myList = [1, [], 2, 3, [], 4, 5, [], [], 9]
print("The original list is : " + str(myList))
result = list(filter(None, myList))
print ("List after empty list removal : " + str(result))

# Ques 10
import copy

def cloneList():
    list1 = eval(input('Enter a list'))
    print(list1, id(list1))
    clone = list1.copy()
    print(clone, id(clone))

cloneList()

# QUes 11
def count_occurrences(lst, ele):
    return lst.count(ele)


list3 = [1, 2, 3, 2, 4, 2, 5, 6]
ele = 2
print(f"The element {ele} appears {count_occurrences(list3, ele)} times in the list.")

