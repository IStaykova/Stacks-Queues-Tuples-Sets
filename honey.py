from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

honey = 0

operators = {  #mapper
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,
}

while bees and nectar:
    if nectar[-1] >= bees[0]:
        honey += abs(operators[symbols[0]](bees[0], nectar[-1]))
        bees.popleft()
        nectar.pop()
        symbols.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
elif nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
