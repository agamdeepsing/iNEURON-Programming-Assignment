
# Ques 1
def DisariumNumber():
    num = input('Enter any Number: ')
    sum = 0
    for item in range(len(num)):
        sum = sum + int(num[item])**(item+1)
    if sum == int(num):
        print('is a Disarium Number')
    else:
        print('is Not Disarium Number') 

DisariumNumber()

# Ques 2

def disarium(start = 0,end = 100):
    output = []

    for i in range(start,end+1):
        sum = 0
        for item in range(len(str(i))):
            sum = sum + int(str(i)[item])**(item+1)
        if sum == i:
            output.append(i)
    return output
            
        
disarium(1,1000)


# Ques 3

def happynumber(i):
    happy = set()
    
    while i != 1 and i not in happy:
        happy.add(i)
        i = sum(int(digit) ** 2 for digit in str(i))
    
    return i == 1


numbers = [19, 23, 28, 68, 44, 6, 82, 100]
for i in numbers:
    if happynumber(i):
        print(f"{i} is a Happy Number")
    else:
        print(f"{i} is not a Happy Number")

# Ques 4

class HappyNumber:
    @staticmethod
    def is_happy_number(number):
        happy = set()

        while number != 1 and number not in happy:
            happy.add(number)
            number = sum(int(digit) ** 2 for digit in str(number))

        return number == 1

    @staticmethod
    def print_happy_numbers(start, end):
        print(f"Happy Numbers from {start} to {end}:")
        happy_numbers = [number for number in range(start, end + 1) if HappyNumber.is_happy_number(number)]
        print(happy_numbers)



start = input("enter the number: ")
end = input("enter the end number: ")
HappyNumber.print_happy_numbers(start, end)


# Ques 5

def checkHarshadNumber():
    num = input('Enter a Number: ')
    sum = 0
    for item in range(len(num)):
        sum = sum + int(num[item])
    if int(num)%sum == 0:
        print(f'{num} is a Harshad Number')
    else:
        print(f'{num} is a Not Harshad Number')
        
checkHarshadNumber()

# Ques 6

def printPronicNumbers(start=0, end=100):
    outputList = []
    if start > end:
        print("Invalid range. Start should be less than or equal to End.")
        return
    for ele in range(start, end + 1):
        outputList.append(ele * (ele + 1))
    print(outputList)

printPronicNumbers()


