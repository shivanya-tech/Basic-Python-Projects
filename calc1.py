def calculator():
    while True:
        print("\n------ SIMPLE CALCULATOR ------")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting... Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter numbers only.")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} × {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("❌ Division by zero is not allowed.")
            else:
                print(f"Result: {num1} ÷ {num2} = {num1 / num2}")
        else:
            print("❌ Invalid choice! Please select 1-5.")

# Run the calculator
calculator()











