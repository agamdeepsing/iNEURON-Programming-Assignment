
# Ques 1
def Div(number):
    for i in range(0,number ):
        if (i%5 == 0) and (i%7 == 0):
            yield ele
for i in Div(250):
    print(i,end="  ")



# Ques 2
def even(number):
    for i in range(number+1):
        if i %7 == 0:
            yield i


for i in even(100):
    print(i,end = " ")



# Ques 3
def fib(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fib(number-1)+fib(number-2)
    
print([fib(x) for x in range(20)])


# Ques 4
def Usernames():
    string = input('Enter Email Address(es): ')
    output = string.split('@')
    print(f'{output[0]}')

for i in range(3):
    Usernames()



# ques 5
class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self,length):
        self.length = length
        def area(self):
            return self.length*self.length
        
sq = Square(25)
print(sq.area())