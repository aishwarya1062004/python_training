try:
    action = input("Enter action: ").strip().lower()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if action == "sub":
        result = num1 - num2
        print("Result:", result)
    else:
        print("Unsupported action.")
except Exception as e:
    print(e)
    