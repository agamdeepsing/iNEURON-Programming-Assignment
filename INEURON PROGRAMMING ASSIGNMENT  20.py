
# Ques 1
def integer(lst):
    output = []
    for i in lst:
        if isinstance(i, int):
            output.append(i)
    return output 

integer([1, 2, 3, "a", "b", 4])
integer(["A", 0, "Edabit", 1729, "Python", "1729"]) 
integer(["Nothing", "here"]) 



# Ques 2
def add_indexes(list1):
    output = []
    for ele in range(len(list1)):
        output.append(ele+list1[ele])
    print(f'{output}')
        
add_indexes([0, 0, 0, 0, 0])
add_indexes([1, 2, 3, 4, 5])
add_indexes([5, 4, 3, 2, 1])



# ques 3
import math

def cubevolume(height, radius):
    output = ((math.pi)*pow(radius,2))*(height/3)
    print(f'{output:.2f}')

cubevolume(3,2) 
cubevolume(15,6)    
cubevolume(18,0)  



# ques 4
def triangle(inputnumber):
    print(f'{int((inputnumber)*((inputnumber+1)/2))}')

triangle(1)
triangle(6)
triangle(215)




# Ques 5
def missing_number(numbers):
    n = len(numbers) + 1
    target = (n * (n + 1)) // 2  
    actual = sum(numbers)  
    missing_number = target - actual
    return missing_number

numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]
missing_number = missing_number(numbers)
print(missing_number)
