#This is Day 2
#Stylish Bio Generator for Instagram
import textwrap
name = input("Enter your name: ").strip()
passion = input("Enter your passion or hobby: ").strip()
emoji = input("Enter an emoji that represents you: ").strip()
website = input("Enter your website: ").strip()

print("\n Choose your style: ")
print("1. Simple and Elegant")
print("2. Vertical Flair")
print("3. Emoji Sandwich")

style = input("Enter the 1, 2, 3: ").strip()
def generate_bio(style):
 if style == "1":
    return f"{name} | {passion} {emoji} | {website}"
 elif style == "2":
    return f"{name}\n{passion} {emoji}\n{website}"
 elif style == "3":  
   return f"\n {emoji} {name} {emoji}\n{emoji} {passion} {emoji}\n{emoji} {website} {emoji}\n"

bio = generate_bio(style)
print("\nYour Stylish Instagram Bio:\n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)

save = input("Do you want to save this bio to a text file ? (y/n): ").strip().lower()
if save == 'y':
    with open("instagram_bio.txt", "w") as file:
        file.write(bio)
    print("Bio saved to instagram_bio.txt") 