
# ques 1
def operation(start,end,divisor):
    output = []
    for i in range(start,end+1):
        if i%divisor == 0:
            output.append(i)
    print(f'Output: ➞ {output}')

operation(1, 10, 3)
operation(7, 9, 2)
operation(15, 20, 7)



# Ques 2
def simonsays(list1, list2):
    if len(list1) >= 2 and len(list2) >= 2:
        if list1[:-1] == list2[1:]:
            return True
    return False
           
simonsays([1, 2], [5, 1])
simonsays([1, 2], [5, 5])
simonsays([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])
simonsays([1, 2, 3, 4, 5], [5, 5, 1, 2, 3])


# Ques 3
def society(inputlist):
    output = []
    for i in inputlist:
        output.append(i[0])
    output = ''.join(sorted(output))
    print(f'{output}')

society(["Adam", "Sarah", "Malcolm"])
society(["Harry", "Newt", "Luna", "Cho"])
society(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])


# Ques 4
def isogram(string):
    checklower = string.lower()
    if len(checklower) == len(set(checklower)):
        print(f'{True}')
    else:
        print(f'{False}')


isogram("Algorism")
isogram("PasSword")
isogram("Consecutive")


# QUes 5
def order(string):
    sorted1 = ''.join(sorted(string))
    if string == sorted1:
        print(f'{string} ➞ {True}')
    else:
       print(f'{string} ➞ {False}')

order("abc")
order("edabit")
order("123")
order("xyzz")


