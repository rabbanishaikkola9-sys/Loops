#  Write a program to print multiplication table of a given number using for loop.
number=int(input("Enter the number that you wanna multiply"))
for i in range(1,11):
    print(f"{number} X {i} = {number*i}")