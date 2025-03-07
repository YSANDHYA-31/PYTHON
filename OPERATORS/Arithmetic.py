def arithmetic_operations(X, Y, Operator):
    if Operator == '+':
        return X + Y
    elif Operator == '-':
        return X - Y
    elif Operator == '*':
        return X * Y
    elif Operator == '/':
        if Y == 0:
            return "Error: Division by zero!"
        return X / Y
    else:
        return "Invalid Operator!"

N1, N2 = map(int, input("Enter two numbers: ").split())
Operand = input("Enter Operator: ")
result = arithmetic_operations(N1, N2, Operand)
print(result)