# this is day 3
# Bill Splitter
def get_float_input(prompt):
   while True: 
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

num_people = int(input("how many people are there in group? "))
names = []
for i in range(num_people):
    name = input(f"Enter the name of person {i + 1}: ").strip()
    names.append(name)
    
total_bill = get_float_input("What is the total bill amount?")
share = round(total_bill / num_people, 2)
print("\n" + "*" * 30)
print(f"Total bill: {total_bill}")
print(f"Each person should pay: {share}")
print(f"{names}, owes share: {share}")