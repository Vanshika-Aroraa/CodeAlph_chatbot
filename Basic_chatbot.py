def chatbot():
    print("Hi! I'm ChatBot. Type 'bye' to end the chat.")

    while True:
        msg = input("You: ").lower()

        if msg == "bye":
            print("ChatBot: Bye! Have a great day 😊")
            break
        elif "hello" in msg or "hi" in msg:
            print("ChatBot: Hello! How can I help you?")
        elif "name" in msg:
            print("ChatBot: My name is ChatBot.")
        elif "how are you" in msg:
            print("ChatBot: I'm just code, but I'm running fine!")
        elif "help" in msg:
            print("ChatBot: You can ask me about my name, mood, or say hello.")
        else:
            print("ChatBot: Sorry, I didn't understand that.")

chatbot()
