from math import ceil
from random import randint

class Task:
    def __init__(self, C, T):
        self.c = C
        self.t = T

def firstCalculation(arr):
    return sum([t.c for t in arr])

def repeatCalculation(arr, specialTask, value):
    total = specialTask.c
    for task in arr:
        total += ceil(value/task.t) * task.c
    if value == total or total >= specialTask.t:
        return True if total <= specialTask.t else False
    return repeatCalculation(arr, specialTask, total)

def markusTheorem(arr, specialTask):
    total = specialTask.c
    for task in arr:
        total += ceil(specialTask.t/task.t) * task.c
    if total <= specialTask.t:
        return True
    return False

def main():
    markuscount = 0
    actualcount = 0
    for _ in range(100000):
        arr = []
        for i in range(5):
            arr.append(Task(randint(1,500), randint(250,1000)))
        biggest = max([t.t for t in arr])
        for i, task in enumerate(arr):
            if task.t == biggest:
                biggest = arr.pop(i)
                break
        markus = markusTheorem(arr, biggest)
        if markus:
            markuscount += 1
        real = repeatCalculation(arr, biggest, firstCalculation(arr))
        if real:
            actualcount += 1
        if markus and not real:
            print("Markus has said this should be valid but it wasn't so he's an idiot")
    print(markuscount, actualcount)

if __name__ == "__main__":
    main()