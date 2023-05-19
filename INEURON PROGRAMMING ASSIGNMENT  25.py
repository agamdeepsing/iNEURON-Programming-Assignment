
# Ques 1
def equal_function():
    if a == b == c:
        print(f'{3}')
    elif a==b or b==c:
        print(f'{2}')
    else:
        print(f'{0}')

equal_function(3,4,3)
equal_function(1,1,1)
equal_function(3,4,1)


# Ques 2
def dicttolist(dictionary):
    output = []
    for key,elements in dictionary.items():
        output.append((key,elements))
    print(f'{output}')


dicttolist({"D": 1,"B": 2,"C": 3})
dicttolist({"likes": 2,"dislikes": 3,"followers": 10})


# Ques 3
def mapping(in_list):
    output = {}
    for i in in_list:
        output[i] = i.upper()
    print(f'{output}')
    
mapping(["p", "s"])
mapping(["a", "b", "c"])
mapping(["a", "v", "y", "z"])


# Ques 4
def replace(string, replacement):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    replacedstring = ''
    for char in string:
        if char in vowels:
            replacedstring += replacement
        else:
            replacedstring += char
    return replacedstring



# Ques 5
def ascii_capitalize(in_string):
    output = ''
    for i in in_string.lower():
        if (ord(i)%2 == 0):
            output += i.upper()
        else:
            output += i
    print(f'{in_string} ➞ {output}')
        
ascii_capitalize("to be or not to be!")
ascii_capitalize("THE LITTLE MERMAID")
ascii_capitalize("Oh what a beautiful morning.")
