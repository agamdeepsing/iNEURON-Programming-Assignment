
# Ques 1
def next_in_line(inputlist,number):
    if len(inputlist) > 1:
        inputlist.append(number)
        inputlist.remove(inputlist[0])
        print(f'{inputlist}')
    else:
        print('No list selected')

next_in_line([5, 6, 7, 8, 9], 1) 
next_in_line([7, 6, 3, 23, 17], 10)
next_in_line([1, 10, 20, 42 ], 6)
next_in_line([], 6)


# Ques 2
def budgets(dict):
    sum = 0
    for i in dict:
        sum += i["budget"]
    print(f' {sum}')
    
budgets([
{ "name": "John", "age": 21, "budget": 23000 },
{ "name": "Steve", "age": 32, "budget": 40000 },
{ "name": "Martin", "age": 16, "budget": 2700 }
])

budgets([
{ "name": "John", "age": 21, "budget": 29000 },
{ "name": "Steve", "age": 32, "budget": 32000 },
{ "name": "Martin", "age": 16, "budget": 1600 }
])


# Ques 3
def alphabet(inputstring):
    output = ''.join(sorted(inputstring))
    print(f'{inputstring} ➞ {output}')

alphabet("hello")
alphabet("edabit")
alphabet("hacker")
alphabet("geek")
alphabet("javascript")


# Ques 4
def interest(p,t,r,n):
    ci = p*(1+(r/n)**(n*t))
    print(f'{ci:.2f}')

interest(100, 1, 0.05, 1)
interest(3500, 15, 0.1, 4)
interest(100000, 20, 0.15, 365)


# Ques 5
def returnint(number):
    output = []
    for i in number:
        if type(i) == int:
            output.append(i)
        print(f'{output}')

returnint([9, 2, "space", "car", "lion", 16])
returnint(["hello", 81, "basketball", 123, "fox"])
returnint([10, "121", 56, 20, "car", 3, "lion"])
returnint(["String", True, 3.3, 1])