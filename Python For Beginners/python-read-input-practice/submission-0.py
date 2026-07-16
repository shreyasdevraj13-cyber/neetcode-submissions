def add_two_numbers() -> int:
    sum = 0
    nums = input().split(",")
    for i in nums:
        sum += int(i)
    return sum




# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
