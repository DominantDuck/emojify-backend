import json
import random

with open("journal/modified_image_mapping.json", "r") as file:
    data = json.load(file)

def assign_emojis(text):
    assigned_emojis = []
    words = text.lower().split()
    i = 0
    while i < len(words):
        if i < len(words) - 1:
            phrase = ' '.join([words[i], words[i + 1]])
            if phrase in data:
                assigned_emojis.extend(random.choice(data[phrase]))
                i += 1
            else:
                if words[i] in data:
                    assigned_emojis.extend(random.choice(data[words[i]]))
        else:
            if words[i] in data:
                assigned_emojis.extend(random.choice(data[words[i]]))
        i += 1
    return assigned_emojis[:4]

# while True:
#     text_input = input("Enter your text (type 'exit' to quit): ")
#     if text_input.lower() == 'exit':
#         break
#     assigned_emojis = assign_random_emojis(text_input)
#     if assigned_emojis:
#         print("Assigned emojis:", assigned_emojis)
#     else:
#         print("No emojis found for the input.")
