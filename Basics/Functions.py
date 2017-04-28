#procedures

def sum(a, b):
    return a+b

# print(sum('Hello ', 'World'))
# print(sum(5, 6.5))


#if Statements

def bigger(x,y):
    if(x>y):
        return x
    return y

# print('The Greater number is ', bigger(10,20))

#Palindrome
def isPalindromeString(string):
    if string == '':
        return True
    else:
        n = len(string)-1
        count = 0
        for i in range(0, n):
            if string[i] == string[n-i]:
                count += 1
        if count == len(string)/2:
            return True
        else:
            return False

# print(isPalindromeString('Bovoovb'))

def fibonacciNumber(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    beforePrev = 0
    prev       = 1

    for i in range(0, n-1):
        next       = prev + beforePrev
        beforePrev = prev
        prev       = next

    return next

# print(fibonacciNumber(36))
'''
    Recursive Function
'''
#Factorial
def factorial(n):
    if(n == 0 or n == 1):
        return 1
    else:
        result = n * factorial(n-1)
        return result

# print(factorial(5))

#Palindrome

def isPalindrome(string):
    if string == '':
        return True
    else:
        if string[0] == string[-1]:
            return isPalindrome(string[1:-1])
        else:
            return False
# print(isPalindrome('bob'))

#Fibonacci Number
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(36))