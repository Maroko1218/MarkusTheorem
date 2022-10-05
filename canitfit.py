from math import ceil
from random import randint

class Task:
    def __init__(self, C, T):
        self.c = C
        self.t = T

def firstCalculation(arr):
    return sum([t.c for t in arr])

def repeatCalculation(arr, specialTask, value, count=1):
    total = specialTask.c
    for task in arr:
        total += ceil(value/task.t) * task.c
    if value == total or total >= specialTask.t:
        return True if total <= specialTask.t else False, count
    return repeatCalculation(arr, specialTask, total, count+1)

def markusTheorem(arr, specialTask):
    total = specialTask.c
    for task in arr:
        total += ceil(specialTask.t/task.t) * task.c
    if total <= specialTask.t:
        return True
    return False

def main():
    markuscount = 0
    wastedcount = 0
    possiblesavedcalculations = 0
    for _ in range(100000):
        arr = []
        for i in range(randint(1, 10)):
            arr.append(Task(randint(1, 500), randint(1, 500)))
        biggest = max([t.t for t in arr])
        for i, task in enumerate(arr):
            if task.t == biggest:
                biggest = arr.pop(i)
                break
        markus = markusTheorem(arr, biggest)
        real, count = repeatCalculation(arr, biggest, firstCalculation(arr))
        if markus:
            markuscount += 1
            possiblesavedcalculations += count - 1 #The -1 is because we're adding 1 calculation to check the upper bound
        if real and not markus:
            wastedcount += 1
        if markus and not real:
            print("Markus has said this should be valid but it wasn't so it's proven false")
    print("Times the full calculation could be skipped:", markuscount, "\nTimes my theorem lead to no answer:", wastedcount, "\nCalculation steps that could've been skipped:", possiblesavedcalculations)

if __name__ == "__main__":
    main()