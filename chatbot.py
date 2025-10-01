def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()  # make lowercase

        if "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hi!")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm fine, thanks!")

        elif "bye" in user_input:
            print("🤖 Chatbot: Goodbye!")
            break  # exit loop

        else:
            print("🤖 Chatbot: I don’t understand that.")

# Run chatbot
chatbot()
