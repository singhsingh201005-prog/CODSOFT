print("Hello! I'm CodBot 🤖. How can I help you today?")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("CodBot: Hello there! 😊 How can I assist you?")
    
    elif "how are you" in user_input:
        print("CodBot: I'm just a bot, but I'm doing great! Thanks for asking.")
    
    elif "your name" in user_input:
        print("CodBot: I'm CodBot — your AI assistant created for CodSoft internship!")

    elif "what can you do" in user_input:
        print("CodBot: I can chat with you and give rule-based responses. Try asking me something!")

    elif "bye" in user_input or "exit" in user_input:
        print("CodBot: Goodbye! 👋 Have a great day.")
        break
    
    else:
        print("CodBot: I'm not sure how to respond to that. Can you rephrase?")
