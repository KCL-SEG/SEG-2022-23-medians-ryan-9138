"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def mediancalc():
    numbers.sort()
    if len(numbers) % 2 != 0:
        mean = numbers[int((len(numbers) - 1) / 2)]
    else:
        mean = (numbers[int((len(numbers) // 2))-1] + numbers[int(len(numbers)//2)]) /2
    return mean


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
run = mediancalc()
print(run)
