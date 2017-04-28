import time

def timeExecution(code):
    startTime = time.clock()
    result    = eval(code)
    runTime   = time.clock()-startTime

    return result, runTime

def spinLoop(n):
    i = 0
    while(i<n):
        i = i + 1

print(timeExecution('1+1'))
print(timeExecution('spinLoop(1000)'))