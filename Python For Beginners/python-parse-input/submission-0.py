from typing import List

def read_integers() -> List[int]:
    num = []
    numbers = input().split(",")
    for x in numbers:
        num.append(int(x))
    return num

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
