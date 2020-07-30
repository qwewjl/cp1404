"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the input is not a integer.


2. When will a ZeroDivisionError occur?
At least one of the input is 0, and if it is the 2nd input, the 1st input must be an integer.


3. Could you change the code to avoid the possibility of a ZeroDivisionError?
yes, i hv changed in 'if'
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))


if numerator == 0 and denominator == 0:
    print('No zero pls, retry')
else:
    fraction = numerator / denominator
    print(fraction)
