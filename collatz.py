"""
Collatz Sequence.
Enter a number, and some jiggery pokery happens!
"""

def collatz(number):
    """Main function, if the number is even, // 2, if odd, * by 3 and add 1."""
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

print("Enter number:")

# This makes sure you give the program a number.
while True:
    try:
        giveme = int(input())
    except ValueError:
        print("Please enter an integer:")
        continue
    break

# Calls the function initially.
yougot = collatz(giveme)

# Loops the function whilst it's returning numbers other than 1, the end point.
while yougot != 1:
    yougot = collatz(yougot)

