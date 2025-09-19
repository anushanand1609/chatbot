# Simple Rule-Based Chatbot
def chatbot():
    print("Chatbot: Hi! I am your friendly chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I am Chatbot, your virtual assistant.")
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you rephrase?")

chatbot()
