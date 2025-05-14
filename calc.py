def calculator():
    print("Простий калькулятор")
    print("Операції: +, -, *, /")
    
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Введіть операцію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Помилка: Ділення на нуль!"
            result = num1 / num2
        else:
            return "Помилка: Невірна операція!"
            
        return f"Результат: {result}"
        
    except ValueError:
        return "Помилка: Введіть числові значення!"

print(calculator())