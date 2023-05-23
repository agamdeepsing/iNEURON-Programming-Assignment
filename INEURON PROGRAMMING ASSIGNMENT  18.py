
# Ques 1
def filter(list):
    output = []
    for ele in list:
        if type(ele) == int and ele >= 0:
            output.append(ele)
    return output
            
print(f'{filter([1, 2, "a", "b"])}')
print(f'{filter([1, "a", "b", 0, 15])}')
print(f'{filter([1, 2, "aasf", "1", "123", 123])}')



# Ques 2
def reverse(string):
    print(f'{string} ➞ {string[::-1].swapcase()}')
    
reverse('Hello World')
reverse("ReVeRsE")
reverse("Radar")



# Ques 3
first, *middle, last = [1,2,3,4,5,6]
print(f'{first}')
print(f'{middle}')
print(f'{last}')




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
def move(list,num):
    first = []
    second = []
    for ele in list:
        if ele == num:
            second.append(ele)
        else:
            first.append(ele)
    first.extend(second)
    return first
    
print(f'{move([1, 3, 2, 4, 4, 1], 1)}')
print(f'{move([7, 8, 9, 1, 2, 3, 4], 9)}')
print(f'{move(["a", "a", "a", "b"], "a")}')