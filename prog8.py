# A program that asks the user to enter 10 numbers and prints the number of odd numbers
print(sum(int(input("Enter a number: ")) % 2 == 1 for i in range(10)))
