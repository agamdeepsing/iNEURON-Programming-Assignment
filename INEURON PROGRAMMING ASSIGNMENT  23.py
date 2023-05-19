
# Ques 1
def symmetrical(inputnum):
    if str(inputnum) == str(inputnum)[::-1]:
        print(f'{inputnum} ➞ {True}')
    else:
        print(f'{inputnum} ➞ {False}')

symmetrical(7227)
symmetrical(12567)
symmetrical(44444444)
symmetrical(9939)
symmetrical(1112111)


# Ques 2
def multiply_nums(inputstring):
    outstring = inputstring.replace(' ','').split(',')
    output = 1
    for i in outstring:
        output *= int(i)
    print(f'{in_string} ➞ {output}')
    
multiply_nums("2, 3")
multiply_nums("1, 2, 3, 4")
multiply_nums("54, 75, 453, 0")
multiply_nums("10, -2")


# Ques 3
def squares(num):
    output = 0
    for i in str(num):
        y = int(i) * int(i)
        output += y 
    return output

squares(9119)
squares(2483)
squares(3212)


# Ques 4
def sorts(inputlist):
    output = sorted(set(inputlist))
    print(f'{inputlist} ➞ {output}')
    
sorts([1, 3, 3, 5, 5]) 
sorts([4, 4, 4, 4])
sorts([5, 7, 8, 9, 10, 15])
sorts([3, 3, 3, 2, 1])


# Ques 5
def meandigits(number):
    if number == 0:
        return 0  # Special case when the number is 0
    
    digit1 = [int(digit) for digit in str(abs(number)) if digit.isdigit()]
    digit_sum = sum(digit1)
    mean = digit_sum / len(digit1)
    return mean

meandigits(42)
meandigits(12345)
meandigits(666)

