print("Chatbot: Hello! I am a simple chatbot.")
print("Type 'bye' to exit the chat.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello":
        print("Chatbot: Hi! How can I help you?")
    
    elif user_input == "how are you":
        print("Chatbot: I am fine. Thank you!")
    
    elif user_input == "what is your name":
        print("Chatbot: I am a rule-based chatbot.")
    
    elif user_input == "what can you do":
        print("Chatbot: I can answer simple questions.")
    
    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break
    
    else:
        print("Chatbot: Sorry, I don't understand that.")