initial_investment = int(input("Please provide a number for the initial investment: "))
interest_rate = 2
compound_period = 3
years = 5



final_amount = initial_investment * (1 + ((interest_rate / compound_period)**(compound_period*years)))
print("The final amount of interest is: ", final_amount)