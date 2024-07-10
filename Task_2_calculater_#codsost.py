def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        return num1 / num2
    else :
        return "Invalid operation"
    
if __name__=="__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation_choise = """Choose an operation: 
    1. Addtion
    2. Subtraction
    3. Multiplication
    4. Division """
    print(operation_choise)
    operation = input("Enter the number correspondig to the operation: ")

    result = calculate(num1, num2, operation)
    print("\nThe result is: ",result)