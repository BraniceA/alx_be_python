#FUNCTION TO PERFORM ARITHMETIC OPERATIONS
def perform_operation(num1, num2, operation):
    
    if operation == 'add':
        return num1 + num2
    
    elif operation == 'subtract':
        return num1 - num2
    
    elif operation == 'divide':
            if num2 == 0:
                return "Cannot divide using 0!!!"
            return num1 / num2
            
    elif operation == 'multiply':
            if num2 == 0:
                print("Cannot multiply by zero!!!")
            else:
                result = num1 * num2
            
    else:
        print("Having trouble?")

    
    return result
