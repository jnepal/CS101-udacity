#While loop

i = 0
while(i != 10):
    i = i+1
    print(i)

# For Loop

def sumList(number):
    sum = 0
    for n in number:
        sum = sum+n

    return sum

print(sumList([1,7,4]))

'''
    For Loop using Range
    range(start, stop) gives the number start to stop-1
'''

for j in range(0,10):
    print(j)