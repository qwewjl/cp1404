for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

'''use "end='' " to make sure the output shown on the same line'''
number_star = int(input("Enter a number:"))
for i in range(number_star):
    print('*', end='')
print()
'''use the string to time the number in terms to show the output in each line'''
for i in range(1, number_star + 1):
    print('*' * i)
print()