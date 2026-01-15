#This is day 1 
#Self Intro Script Generator
import datetime
name = input("What is your name? ").strip()
age = input("How old are you? ").strip()
city = input("Which city do you live in? ").strip()
profession = input("What is your profession? ").strip()
hobby = input("What is your favorite hobby? ").strip()

intro_script = ( 
 f"\n hello! my name is {name}. I am {age} years old"
 f", living in {city}.\n I work as a {profession}."
 f"\n In my free time, I love to {hobby}."
 f"\n Nice to meet you all! \n" 
 )
border = "*" * 80
current_date = datetime.date.today().isoformat()
intro_script +=  f"\n Logged on: {current_date}"
print(border + "\n" + intro_script + "\n" + border)

