#Lists

daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31] #no of days in Month

def getDaysInMonth(month):
    if(month > 12):
        return 'Please Enter a Valid Month'
    month = month-1

    return daysInMonth[month]

print(getDaysInMonth(2))

#Nested Lists

countries = [['China', 'Beijing', 1350],
             ['India', 'Delhi', 1210],
             ['United States', 'Washington', 307]];

print(countries[0][0])  #print()s China

#Append Method List Operation

p = [3,4]
q = [4,5]

p.append(q)
print(p)

print(len(p))

#Function on List

def findElement(set, keyword):
    i =0
    while(i<len(set)):
        if(keyword == set[i] ):
            return i;

        i = i+1

    return -1
print(findElement([1,2,3], 3))

"Using For Loop"

def find_element(set, keyword):
    i = 0
    for s in set:
        if(keyword == s):
            return i;
        i = i+1
    return -1

print(find_element([1,2,3], 3))

#List Operation

list = [1,2,3,4];

"index method returns the first position of the matched element in the list"
"if not found returns error message"

print(list.index(4))

# In  Method
'''
    List Operation
'''
print(3 in list)  #True if found in the list
print(5 in list)  #False if not found in the list

# Not In Method (Opposite to In Method)
print(3 not in list)

"Find ElementPostion Using In Method"

def findElementIndex(list, keyword):
    if keyword in list:
        return list.index(keyword)
    else:
        return -1

"Find ElementPosition Using Not in Method "

def find_element_position(list, keyword):
    if(keyword not in list):
        return -1
    else:
        return list.index(keyword)

def union(a,b):
    for n in b:
        if(n not in a):
            a.append(n)
    return a,b

print(union([1,2,3],[3,4,5,6]))