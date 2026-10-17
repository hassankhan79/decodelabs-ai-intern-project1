responses = {
    "hello": "Hi! How can I help you?",
    "help": "You can say hello, time, or exit.",
    "who are you": "I'm a simple rule-based chatbot.",
}

def sanitize(raw_input):
    return raw_input.strip().lower()

def process(clean_input):
    return responses.get(clean_input, "Sorry, I didn't understand that.")

def main():
    print("Bot started. Type 'exit' to quit.")
    while True:
        clean_input = sanitize(input("You: "))
        if clean_input == "":
            continue
        if clean_input == "exit":
            print("Bot: Goodbye!")
            break
        print("Bot:", process(clean_input))

if __name__ == "__main__":
    main()