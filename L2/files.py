
'''Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
'''
tem_file = open("name.txt","w")
name = input("Enter your name")
print(name,file=tem_file)
tem_file.close()

'''
Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).
'''
tem_file = open("name.txt","r")
name = in_file.read().strip()
tem_file.close()
print("Your name is",name)
'''another solution(using with)///
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("Your name is", name)
'''


