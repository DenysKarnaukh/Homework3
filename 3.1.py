

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

operation = input("Введіть дію (+, -, *, /): ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b != 0:
        result = a / b
    else:
        result = "Помилка: ділення на 0!"
else:
    result = "Помилка: невідома операція!"

print("Результат:", result)
