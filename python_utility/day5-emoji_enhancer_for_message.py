#THis is day 5
# Emoji Enhancer for Messages
   
# get a dictionary
emoji_map_dict = {
    "happy": "😊",
    "sad": "😞",
    "wink": "😉",
    "laugh": "😄",
    "tongue": "😛",
    "love": "❤️"
}

# get user message
message = input("Enter your message: ")

updated_message = []

#process each word
for word in message.split():
    cleaned = word.lower().strip(",!.?")
    emoji = emoji_map_dict.get(cleaned, "")
    if emoji:
        updated_message.append(f"{word}, {emoji}")
    else:
        updated_message.append(word)

updated_word = " ".join(updated_message)
        
print("\n Enhanced_message \n")
print(updated_word)
                                                                                                                                                                                                                              