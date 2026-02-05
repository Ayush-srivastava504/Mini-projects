#This is Day11
#Building a Caesar Cipher
def encrypt(message, key):
    result = ""
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
         result += char 
    return result

def decrypt(message, key):
    return encrypt(message, -key)

print("Secret Message Program")
choice = input("Do you want E or D").strip().lower()

if choice == 'e':
    text = input("Enter your message: \n ")
    try:
     key = int(input("Enter a number between 1 to 25:"))
     encrypted = encrypt(text, key)
     print("Encrypted message")
     print(encrypted)
    except ValueError:
        print("Invalid key")
elif choice == 'd':
    text = input("Enter your Encrypted message: \n ")
    try:
     key = int(input("Enter a number between 1 to 25:"))
     decrypted = decrypt(text, key)
     print("Decrypted message")
     print(decrypted)
    except ValueError:
        print("Invalid key")
else:
    print("Invalid Choice")
     

        