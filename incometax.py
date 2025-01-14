while True:
    try:
        income = input("Enter your annual income (or type 'exit' to quit): ")
        if income.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break

        annual_income = float(income)
        if annual_income < 0:
            print("Income cannot be negative. Please enter a valid amount.")
        else:
            if annual_income <= 250000:
                tax = 0  
            elif annual_income <= 500000:
                tax = (annual_income - 250000) * 0.05  
            elif annual_income <= 1000000:
                tax = (250000 * 0.05) + (annual_income - 500000) * 0.1  
            else:
                tax = (250000 * 0.05) + (500000 * 0.1) + (annual_income - 1000000) * 0.2  

            print(f"For an annual income of ₹{annual_income:,.2f}, the calculated income tax is: ₹{tax:,.2f}\n")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
