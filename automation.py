print("Simple Calculator For Daily Life!")
print('Write 1 To Add!')
print('Write 2 To Subtract!')
print('Write 3 To Multiply!')
print('Write 4 To Divide!')

choice =   int(input("Please Select Your Operation..."))
num1   =   int(input("Enter The First Number..."))
num2   =   int(input("Enter The Second Number..."))

addedNumber = float(num1 + num2)
subtractedNumber =float(num1 - num2)
multipliedNumber = float(num1 * num2)
dividedNumber = float(num1 / num2)

if choice == 1:
    print("Your Answer =", addedNumber)
elif choice == 2:
    print("Your Answer =",subtractedNumber)
elif choice == 3:
    print("Your Answer =",multipliedNumber)
elif choice == 4:
    print("Your Answer =",dividedNumber)
else:
    print("The Operation is invalid")    
