def calculator():
    print("Welcome to Calculator!")
    
    while True:
        print("\nOperations:")
        print("+ : Addition")
        print("- : Subtraction")
        print("* : Multiplication")
        print("/ : Division")
        print("% : Modulus")
        print("x2 : Square")
        print("√ : Square Root")
        print("e : Exit")
        
        operation = input("Enter operation: ")
        
        if operation == 'e':
            print("Exit Calculator")
            break
        
        num1 = float(input("Enter first number: "))
        
        if operation in ['x2', '√']:
            if operation == 'x2':
                result = num1 ** 2
            elif operation == '√':
                result = num1 ** 0.5
        else:
            num2 = float(input("Enter second number: "))
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error! Cannot Divide by zero")
                    continue
            elif operation == '%':
                result = num1 % num2
            else:
                print("Invalid operation!")
                continue
        
        if result.is_integer():
            result = int(result)
        
        print("Result:", result)

calculator()
