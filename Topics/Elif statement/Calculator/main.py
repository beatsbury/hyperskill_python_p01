# put your python code here
num1 = float(input())
num2 = float(input())
op = input()

if (op in ["/", "mod", "div"]) & (num2 == 0.0):
    answer = "Division by 0!"
elif op == "+":
    answer = num1 + num2
elif op == "-":
    answer = num1 - num2
elif op == "/":
    answer = num1 / num2
elif op == "*":
    answer = num1 * num2
elif op == "mod":
    answer = num1 % num2
elif op == "pow":
    answer = num1 ** num2
elif op == "div":
    answer = num1 // num2

print(answer)
