#INPUT

num1 = float(input("ENTER NUM1: "))
num2 = float(input("ENTER NUM1:  "))
operation = input("ENTER     (+, -, *, /):  ")

#ANALYZE

if operation == "+" :
    result = num1 + num2
elif operation == "-" :
    result = num1 - num2
elif operation == "/" :
    result = num1 / num2
elif operation == "*" :
    result = num1 * num2

else:
    result = "invalid"

#DISPLAY

print(f"RESULT: {result}")