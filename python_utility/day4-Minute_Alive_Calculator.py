# THis is Day 4
# Minute Alive Calculator
def calculate_minutes(age_years):
    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60

    total_days = age_years * DAYS_IN_YEAR
    total_hours = total_days * HOURS_IN_DAY
    total_minutes = total_hours * MINUTES_IN_HOUR
    
    return round(total_days), round(total_hours), round(total_minutes)

while True:
    try: 
        age = float(input("Enter your age in years: "))
        days, hours, minutes = calculate_minutes(age)
        print("\n You are approx:")
        print(f"  - {days} days")
        print(f"  - {hours} hours")
        print(f"  - {minutes} minutes")
        again = input("\nWould you like to calculate again? (yes/no): ").strip().lower()
        if again != 'yes':  
            print("Goodbye!")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number for age.")
        