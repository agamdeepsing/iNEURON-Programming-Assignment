
# Ques 1
def double(string):
    output = ''
    for i in string:
        output += i*2
    return output

print(f'{double("String")}') 
print(f'{double("Hello World!")}')
print(f'{double("1234!_")}')



# Ques 2
def reverse(inputbool):
    if type(inputbool) == bool:
        return not inputbool
    else:
        return "Boolean Expected"

print(f'{reverse(True)}')
print(f'{reverse(False)}')
print(f'{reverse(0)}')
print(f'{reverse(None)}')


# Ques 3
def numbers(number):
    output = 0.5
    for i in range(number):
        output *= 2
    print(f'{output/1000}m')
    
numbers(1)
numbers(4)
numbers(21)


# Ques 4
def indexcaps(inputstring):
    outputstring = []
    for i in inputstring:
        if i.isupper():
            outputstring.append(inputstring.index(i))
    print(f'{outputstring}')

indexcaps("eDaBiT")
indexcaps("eQuINoX")
indexcaps("determine")
indexcaps("STRIKE")
indexcaps("sUn")



# Ques 5
def findevennums(inputnumber):
    output = [i for i in range(1,inputnumber+1) if i%2 == 0]
    print(f'Output ➞ {output}')
    
findevennums(8)
findevennums(4)
findevennums(2)