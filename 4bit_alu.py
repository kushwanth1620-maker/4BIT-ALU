number=int(input("Enter  number: (0 to 15)"))
number2=int(input("Enter another number: (0 to 15)"))
if number <0 and number>15 and number2<0 and number2>15:
    print("Please enter the number in the range 0 to 15")

else:
    print("1:Addition")
    print("2:Subtraction")
    print("3:XOR")
    print("4:AND")
    print("5:OR")
    carry =0
    borrow=0

    choice =input("choose an option from above:-")
    if choice == 1:
        result=number+number2
        carry = int(result > 15)
        result =  result & 15
    elif choice ==2:
        result=number-number2
        borrow = int(number < number2)
        result = (number - number2) & 15

    elif choice ==3:
        result=number^number2
    elif choice ==4:
        result=number & number2
    elif choice == 5:
        result=number | number2 
    else:
        print("invalid Operation")
        result=None

    if result is not None:
        print('Result:',result)
        print("Binary:",format(result,"04b"))
        print("Carry:",carry)
        print("Borrow:",borrow)