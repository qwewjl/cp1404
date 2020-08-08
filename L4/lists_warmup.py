'''1.Change the first element of numbers to "ten" (the string, not the number 10)'''
numbers = [3, 1, 4, 1, 5, 9, 2]
placeholder = "ten"
number_one = numbers + [placeholder]
print(number_one)

'''2.Change the last element of numbers to 1'''
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
print(numbers)


'''3.Get all the elements from numbers except the first two (slice)'''
print(numbers[2:])


'''4.Check if 9 is an element of numbers'''
if 9 in numbers:
    print("9 is in the list")
else:
    print("9 is not in the list")
