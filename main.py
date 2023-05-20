# tip-calculator
#For calculating how to  share money and if any with tip included 

print("welcome to tip calculator!")
bill = float(input("What is the total bill?\n$"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?"))
people = int(input("How many people to split the bill?"))

tip_in_percent = tip/100
bill_in_percentage = tip_in_percent * bill
total_bill = bill_in_percentage + bill
bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amount} Each")
