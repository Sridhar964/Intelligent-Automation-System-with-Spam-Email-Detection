import json
import random
import nltk
from nltk.tokenize import word_tokenize

# -------------------------------
# LOAD INTENTS
# -------------------------------
with open("intents.json") as file:
    data = json.load(file)

# -------------------------------
# TEXT PREPROCESSING
# -------------------------------
def preprocess(text):
    tokens = word_tokenize(text.lower())
    return tokens

# -------------------------------
# MATCH USER INPUT
# -------------------------------
def get_response(user_input):
    user_tokens = preprocess(user_input)

    best_match = None
    max_score = 0

    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            pattern_tokens = preprocess(pattern)

            # Simple matching score
            score = len(set(user_tokens) & set(pattern_tokens))

            if score > max_score:
                max_score = score
                best_match = intent

    if best_match:
        return random.choice(best_match["responses"])
    else:
        return "Sorry, I didn't understand that."

# -------------------------------
# CHAT LOOP
# -------------------------------
print(" Chatbot is running! Type 'quit' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    response = get_response(user_input)
    print("Bot:", response)