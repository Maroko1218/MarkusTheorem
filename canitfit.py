from math import ceil
from random import randint

SIMULATIONS = 100000 #Amount of times tasks will be randomly created and checked against my method and the real one

TASKS_LOWER_LIMIT = 1 #The amount of tasks is randomly generated between the lower and upper limit
TASKS_UPPER_LIMIT = 10

EXECUTION_TIME_LOWER_LIMIT = 1 #Execution time for each individual task is randomly generated between the lower and upper limit
EXECUTION_TIME_UPPER_LIMIT = 500

PERIOD_TIME_LOWER_LIMIT = 1 #Period time for each individual task is randomly generated between the lower and upper limit
PERIOD_TIME_UPPER_LIMIT = 500

class Task:
    def __init__(self, C, T):
        self.c = C
        self.t = T

def firstCalculation(arr):
    return sum([t.c for t in arr])

def repeatCalculation(arr, specialTask, value, count=1):
    total = specialTask.c
    total += sum(ceil(value/t.t) * t.c for t in arr)
    if value == total or total >= specialTask.t:
        return True if total <= specialTask.t else False, count
    return repeatCalculation(arr, specialTask, total, count+1)

def markusTheorem(arr, specialTask):
    total = specialTask.c
    total += sum(ceil(specialTask.t/t.t) * t.c for t in arr)
    if total <= specialTask.t:
        return True
    return False

def main():
    markuscount = 0
    wastedcount = 0
    potentiallyskippedcalculations = 0
    for _ in range(SIMULATIONS):
        arr = []
        for i in range(randint(TASKS_LOWER_LIMIT, TASKS_UPPER_LIMIT)):
            arr.append(Task(randint(EXECUTION_TIME_LOWER_LIMIT, EXECUTION_TIME_UPPER_LIMIT), randint(PERIOD_TIME_LOWER_LIMIT, PERIOD_TIME_UPPER_LIMIT)))
        biggest = max([t.t for t in arr])
        for i, task in enumerate(arr):
            if task.t == biggest:
                biggest = arr.pop(i)
                break
        markus = markusTheorem(arr, biggest)
        real, count = repeatCalculation(arr, biggest, firstCalculation(arr))
        if markus:
            markuscount += 1
            potentiallyskippedcalculations += count - 1 #The -1 is because we're adding 1 calculation by testing my method
        if real and not markus:
            wastedcount += 1
        if markus and not real: #If this outcome would ever be true my Theorem falls apart
            print("Markus has said this should be valid but it wasn't so it's proven false")
    print("Times the full calculation could be skipped:", markuscount, "\nTimes my theorem lead to no answer:", wastedcount, "\nCalculation steps that could've been skipped:", potentiallyskippedcalculations)

if __name__ == "__main__":
    main()