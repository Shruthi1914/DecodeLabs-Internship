print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input == "bye" or user_input == "exit":
        print("Chatbot: Goodbye! Have a nice day.")
        break
    elif user_input == "hello":
        print("Chatbot: Hi there!")

    elif user_input == "how are you":
        print("Chatbot: yeah i am doing great!")

    elif user_input == "what is your name":
        print("Chatbot: I am a simple rule-based chatbot.")

    elif user_input == "help":
        print("Chatbot: You can greet me, ask my name, or say bye to exit.")

    else:
        print("Chatbot: Sorry, I don't understand that.")