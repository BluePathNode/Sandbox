#
print("Enter a number")
meaning = input(":> ")
choice = int(meaning)
if choice > 10:
    print(input("Number is greater than Ten!"))
elif choice == 10:
    print(input("Number is the same!"))
else:
    print(input("Number is less than Ten!"))
