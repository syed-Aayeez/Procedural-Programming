print("----------CALCULATOR----------")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("\nChoose type of operation\n")
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
operation=int(input("Enter the type of operation: "))
if operation == 1:
    print(a+b)
elif operation == 2:
    print(a-b)
elif operation == 3:
    print(a*b)
elif operation == 4:
    print(a/b)
else:
    print(" please Recheck the operation you want to perform")
   