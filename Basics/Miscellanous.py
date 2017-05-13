'''
    ord() returns the ASCII value of the character
'''
print(ord('a'))
print(ord('z'))

'''
    chr() returns the character specified by the ASCII value
'''

print(chr(97))

'''
    str() converts the integer into character
'''

print(ord(str(3)))
print(ord('3'))

# Nested Function Example
greeting = "Hello"

def makeGreeting(greeting):
    def greeter(person):
        print(greeting + person)
    return greeter

sayHello = makeGreeting("Hello from the other side ")
sayHello("Adele")

# Handling and Raising exception
try:
    print("Joseph")
    # raise(Exception(22))
    print(1/0)
except Exception as problem:
    print("Didn't Work: We Caught")
    print(problem)

# lambda function
#function for finding sum
def sum(a, b):
    return a+b

print(sum(2,3))

#could be also expressed as lambda function
#similar to analogy of anonymous function in functional programming
#lambda returns iterables

sumVariable = lambda a,b: a+b
anotherVariable = sumVariable

print(sumVariable(2, 3))
print(anotherVariable(2,5))

#Map Function
numberList = [1, 2, 3, 4]

def square(x):
    return x*x

#map() returns iterables
squareList = list(map(square, numberList))
# for item in squareList:
#     print(item)

#also can be done as
nextSquareList = list(map(lambda x: x*x, numberList))
for item in nextSquareList:
    print(item)


#Filter Function
# also returns iterables

def oddNumber(number):
    return number % 2 == 1

oddNumber = list(filter(oddNumber, [1,2,3,4,5]))
print(oddNumber)

evenNumber = list(filter(lambda number: number % 2 == 0, [1,2,3,4,5]))
print(evenNumber)
