
# Ques 1
dict = {"1":"Microsoft","2":"Gooogle","3":"facebook","4":"meta","5":"cognizant","6":"KPMG","7":"Google","8":"Microsoft"}
print(dict.values())
print(f'Unique Values: {list(set(dict.values()))}')


# Ques 2
dict = {'iphone':180000,'Samsung':125000,'oneplus':60000,'jio':4000,'xiomi':10000}
print('Sum of All items: ',sum(dict.values()))


# Ques 3
course_details = {
    'company_name':'Ineuronpvtld'
}
course = {
    'details':"full stack data science"
}

instructors = {
    'course_instructors':['Sudhanshu sir','Krish sir','paul sir','Bappy','Avnish']
}
course_details.update(instructors)
print(course_details)


# Ques 4
list = [('A',10),('B',20),('C',30),('D',40),('E',50),('F',60),('G',70),('H',80),('I',90),('J',100)]

dict(list)


# Ques 5
from collections import OrderedDict

def insert_at_beginning(od, key, value):
    od[key] = value
    od.move_to_end(key, last=False)

# Creates an OrderedDict
od = OrderedDict()
od['1'] = 'Microsoft'
od['2'] = 'Google'
od['3'] = 'Facebook'

print("Original OrderedDict:")
for key, value in od.items():
    print(f"{key}: {value}")


insert_at_beginning(od, '0', 'Apple')


print("\nUpdated OrderedDict:")
for key, value in od.items():
    print(f"{key}: {value}")



# Ques 6
from collections import OrderedDict

list = {'a': 1, 'h': 2, 'g': 3, 'v': 4, 'x': 5, 'b': 6}
print(list)

finallist = OrderedDict(dict(sorted(list.items())))
print(finallist)


# Ques 7

d_items = {'apple': 100000, 'samsung': 22000, 'motorola': 6000, 'gionee': 13000}

def sort_dict(in_dict, sort_type):
    if sort_type == 'key':
        print(dict(sorted(in_dict.items(), key=lambda x: x[0], reverse=False)))
    else:
        print(dict(sorted(in_dict.items(), key=lambda x: x[1], reverse=True)))

sort_dict(d_items, 'key')
sort_dict(d_items, 'value')
