import random
from datetime import datetime

def chatbot():
    print("Welcome to SmartBot! (Type 'bye' to exit)\n")

    greetings = ["Hello!", "Hi there!", "Hey!", "Namaste!", "How can i help you!"]
    farewell = ["Goodbye!", "See you later!", "Bye! Have a nice day!", "Take care!","Nice to meet you!!"]
    
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print(f"Bot: {random.choice(greetings)}")
        elif "how are you" in user_input:
            print("Bot: I'm just a program, but I'm doing great! How about you?")
        elif "what is your name" in user_input:
            print("Bot: I’m SmartBot, your intelligent virtual buddy!")
        elif " what about you" in user_input or "who are you" in user_input:
            print("Bot: I’m a Python-based chatbot built to chat, assist, and learn!")
        elif "what is the time now" in user_input:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Bot: The current time is {now}.")
        elif "what is the date" in user_input or "what is the day" in user_input:
            today = datetime.now().strftime("%A, %d %B %Y")
            print(f"Bot: Today is {today}.")
        elif "thank you" in user_input:
            print("Bot: You're most welcome! ")
        elif "who created you" in user_input:
            print("Bot: I was created by a Python developer. Maybe it was you? ")
        elif "i am fine" in user_input:
            print("Bot: That’s awesome to hear!")
        elif "what can you do" in user_input:
            print("Bot: I can chat with you, answer simple questions, and keep you company. ")
        elif "bye" in user_input or "exit" in user_input:
            print(f"Bot: {random.choice(farewell)}")
            break
        else:
            print("Bot: Hmm... I didn't understand that. Can you rephrase?")

chatbot()

